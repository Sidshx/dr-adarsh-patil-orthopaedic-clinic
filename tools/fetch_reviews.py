#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Refresh data/reviews.json from the clinic's Google Business Profile.

Run by .github/workflows/update-reviews.yml on a schedule. Uses the Business
Profile API (the owner's own review data) rather than the Places API, because
Places caps out at 5 reviews and its policies forbid storing review content.

Required environment variables (set as GitHub Actions secrets):
    GBP_CLIENT_ID       OAuth 2.0 client ID
    GBP_CLIENT_SECRET   OAuth 2.0 client secret
    GBP_REFRESH_TOKEN   Refresh token for an account that manages the listing

Optional:
    GBP_LOCATION_NAME   e.g. "accounts/123/locations/456" to skip discovery
    REVIEWS_MAX         how many reviews to publish (default 15)
    REVIEWS_MIN_STARS   minimum star rating to publish (default 4)
"""

import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "reviews.json")
PROFILE_URL = "https://share.google/PiXCMrwgPo3YnYGQm"

STAR_WORDS = {"ONE": 1, "TWO": 2, "THREE": 3, "FOUR": 4, "FIVE": 5}
TOKEN_URL = "https://oauth2.googleapis.com/token"
ACCOUNTS_URL = "https://mybusinessaccountmanagement.googleapis.com/v1/accounts"
LOCATIONS_URL = "https://mybusinessbusinessinformation.googleapis.com/v1/{account}/locations"
REVIEWS_URL = "https://mybusiness.googleapis.com/v4/{location}/reviews"


def api(url, token=None, params=None, data=None):
    if params:
        url += ("&" if "?" in url else "?") + urllib.parse.urlencode(params)
    body = urllib.parse.urlencode(data).encode() if data else None
    req = urllib.request.Request(url, data=body)
    if token:
        req.add_header("Authorization", "Bearer " + token)
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")[:600]
        raise SystemExit("API error %s on %s\n%s" % (e.code, url.split("?")[0], detail))


def access_token():
    for key in ("GBP_CLIENT_ID", "GBP_CLIENT_SECRET", "GBP_REFRESH_TOKEN"):
        if not os.environ.get(key):
            raise SystemExit("Missing environment variable: %s" % key)
    tok = api(TOKEN_URL, data={
        "client_id": os.environ["GBP_CLIENT_ID"],
        "client_secret": os.environ["GBP_CLIENT_SECRET"],
        "refresh_token": os.environ["GBP_REFRESH_TOKEN"],
        "grant_type": "refresh_token",
    })
    return tok["access_token"]


def find_location(token):
    preset = os.environ.get("GBP_LOCATION_NAME")
    if preset:
        return preset
    accounts = api(ACCOUNTS_URL, token).get("accounts", [])
    if not accounts:
        raise SystemExit("No Business Profile accounts visible to this token.")
    for acct in accounts:
        locs = api(LOCATIONS_URL.format(account=acct["name"]), token,
                   {"readMask": "name,title", "pageSize": 100}).get("locations", [])
        if locs:
            loc = locs[0]
            print("Using %s (%s)" % (loc.get("title", "?"), loc["name"]))
            return "%s/%s" % (acct["name"], loc["name"])
    raise SystemExit("No locations found on any account.")


def relative_time(iso):
    """Render an absolute timestamp the way Google labels it ('4 months ago')."""
    if not iso:
        return ""
    try:
        when = datetime.fromisoformat(iso.replace("Z", "+00:00"))
    except ValueError:
        return ""
    days = (datetime.now(timezone.utc) - when).days
    if days < 1:
        return "today"
    if days < 7:
        return "%d day%s ago" % (days, "" if days == 1 else "s")
    if days < 31:
        w = max(1, days // 7)
        return "%d week%s ago" % (w, "" if w == 1 else "s")
    if days < 365:
        m = max(1, days // 30)
        return "%d month%s ago" % (m, "" if m == 1 else "s")
    y = days // 365
    return "a year ago" if y == 1 else "%d years ago" % y


def collect(token, location):
    """Page through every review on the listing."""
    out, page, average, total = [], None, None, None
    while True:
        params = {"pageSize": 50, "orderBy": "updateTime desc"}
        if page:
            params["pageToken"] = page
        res = api(REVIEWS_URL.format(location=location), token, params)
        if average is None:
            average = res.get("averageRating")
            total = res.get("totalReviewCount")
        out.extend(res.get("reviews", []))
        page = res.get("nextPageToken")
        if not page:
            break
    return out, average, total


def main():
    max_n = int(os.environ.get("REVIEWS_MAX", "15"))
    min_stars = int(os.environ.get("REVIEWS_MIN_STARS", "4"))

    token = access_token()
    location = find_location(token)
    raw, average, total = collect(token, location)
    print("Fetched %d reviews from the API." % len(raw))

    picked = []
    for r in raw:
        stars = STAR_WORDS.get(str(r.get("starRating", "")).upper())
        text = (r.get("comment") or "").strip()
        if not stars or stars < min_stars or not text:
            continue
        # Google appends machine translations after this marker; keep the original.
        for marker in ("\n\n(Original)\n", "(Original)"):
            if marker in text:
                text = text.split(marker)[-1].strip()
                break
        if text.startswith("(Translated by Google)"):
            continue
        picked.append({
            "author": (r.get("reviewer") or {}).get("displayName") or "Google user",
            "rating": stars,
            "when": relative_time(r.get("createTime") or r.get("updateTime")),
            "text": " ".join(text.split()),
        })
        if len(picked) >= max_n:
            break

    if not picked:
        print("No publishable reviews returned; leaving the existing file untouched.")
        return 0

    payload = {
        "source": "Google Business Profile",
        "profile_url": PROFILE_URL,
        "rating": round(float(average), 1) if average else None,
        "total": total,
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "reviews": picked,
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("Wrote %d reviews to %s (rating %s of %s total)."
          % (len(picked), os.path.relpath(OUT, ROOT), payload["rating"], total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
