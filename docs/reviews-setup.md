# Keeping the Google reviews section up to date

The reviews carousel on the homepage renders from `data/reviews.json`. Nothing in the
HTML is hand-written, so refreshing the reviews only means refreshing that one file.

`.github/workflows/update-reviews.yml` does that automatically once a week
(Mondays, 01:30 UTC / 07:00 IST) by calling `tools/fetch_reviews.py`. Until the credentials
below are added, the workflow skips itself with a note in the run summary and the
committed `data/reviews.json` continues to be served — the site never breaks.

## Why the Business Profile API and not the Places API

| | Places API | Business Profile API |
|---|---|---|
| Reviews returned | 5, relevance-sorted only | all of them, paginated |
| Storing the text | [prohibited by policy](https://developers.google.com/maps/documentation/places/web-service/policies) | permitted — it is your own listing data |
| Access | any API key | OAuth as the listing owner/manager |

Because the workflow commits review text into the repo, the Places API is not an
option. The Business Profile API is.

## One-time setup

1. **Create a Google Cloud project** and enable these three APIs:
   - Google My Business API (this one needs an
     [access request form](https://developers.google.com/my-business/content/prereqs);
     approval usually takes a few days)
   - My Business Account Management API
   - My Business Business Information API

2. **Create an OAuth 2.0 Client ID** of type *Desktop app*. Note the client ID and secret.

3. **Authorise with the Google account that manages the clinic listing**
   (the account Dr. Patil uses for the Business Profile) and request the scope
   `https://www.googleapis.com/auth/business.manage`. Use `access_type=offline`
   and `prompt=consent` so Google returns a **refresh token**. Save that token.

4. **Add four repository secrets** under Settings → Secrets and variables → Actions:

   | Secret | Value |
   |---|---|
   | `GBP_CLIENT_ID` | OAuth client ID |
   | `GBP_CLIENT_SECRET` | OAuth client secret |
   | `GBP_REFRESH_TOKEN` | refresh token from step 3 |
   | `GBP_LOCATION_NAME` | optional, e.g. `accounts/123/locations/456` — skips lookup |

5. **Run it once by hand** from the Actions tab (*Update Google reviews* →
   *Run workflow*) to confirm it works. A successful run commits `Sync Google reviews`
   if anything changed.

## Tuning

Set these in the workflow's `env:` block:

- `REVIEWS_MAX` — how many reviews to publish (default 15)
- `REVIEWS_MIN_STARS` — minimum rating to publish (default 4)

## Editing reviews by hand

Edit `data/reviews.json` directly and push. The shape is:

```json
{
  "rating": 5.0,
  "total": 174,
  "updated": "2026-08-07",
  "reviews": [
    { "author": "Name", "rating": 5, "when": "2 months ago", "text": "…" }
  ]
}
```

Note that a manual edit will be overwritten the next time the workflow runs
successfully.

## A note on medical advertising rules

Indian doctors are governed by the
[Indian Medical Council (Professional Conduct, Etiquette and Ethics) Regulations, 2002](https://www.nmc.org.in/rules-regulations/code-of-medical-ethics-regulations-2002/),
which the NMC re-adopted after the 2023 conduct regulations were
[held in abeyance](https://medicaldialogues.in/health-news/nmc/breaking-news-nmc-puts-its-controversial-registered-medical-practitioner-professional-conduct-regulations-2023-put-on-hold-116314)
on 23 August 2023.

Regulation 6.1.1 states that a physician shall not "boast of cases, operations, cures
or remedies or permit the publication of report thereof through any mode."

Publishing patient reviews on the clinic's own site was a decision taken knowingly by
Dr. Patil. Two things follow from that, and they matter more once updates are automatic:

- `REVIEWS_MIN_STARS` controls quality, not content. **New reviews are published
  without anyone reading them first.** A future review describing a specific cure or
  surgical outcome would go live on its own. Consider reviewing the workflow's commits
  periodically, or lowering `REVIEWS_MAX` and curating `data/reviews.json` by hand.
- The disclaimer under the carousel — that reviews are the authors' own opinions and
  are not a promise of any medical outcome — should stay.
