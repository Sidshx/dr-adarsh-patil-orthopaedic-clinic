#!/usr/bin/env python3
"""Prepare the inauguration photographs for the gallery.

Reads the originals once, writes a web-sized copy plus a 4:3 thumbnail that
matches the existing gallery tiles. Re-runnable: it always works from SRC.
"""
import os
from PIL import Image, ImageOps

SRC = "/home/user/workspace/uploaded_attachments/39ee75f7561c4912b422dde683e2999b"
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets", "inauguration"))
os.makedirs(OUT, exist_ok=True)

# (source file, output slug) — ordered as the ceremony unfolded
PHOTOS = [
    ("80e5e1db-ec38-4dbe-bdd3-b6b4e39550ee.jpeg", "ribbon-cutting"),
    ("69e9f46d-6ae6-49a8-b94e-fcb86c3a5f56.jpeg", "chief-guest-address"),
    ("6d196a57-6f62-42d1-b6d6-a74b74f21689.jpeg", "address-wide"),
    ("3d17a208-f61e-49b2-be11-56c48365584d.jpeg", "guests-on-dais"),
    ("edf616a5-c6af-4305-a2f1-013bf2e34463.jpeg", "guests-seated"),
    ("82c5b51b-a263-4264-baf3-e160bfeb3cab.jpeg", "felicitation"),
    ("715b113d-5097-45ba-b636-580867190d22.jpeg", "group-photograph"),
    ("ed58faa5-63bb-4a67-a080-3ecc0a21bf61.jpeg", "family-at-signage"),
    ("23a36ad8-b079-405b-8962-85366b3dc8b1.jpeg", "consulting-room-guests"),
    ("f110c8f5-1b88-40b7-88ed-e311207fb40c.jpeg", "consulting-room-visit"),
    ("0215d870-323b-4ad1-ba33-1c5ad4acc161.jpeg", "consulting-room-gathering"),
    ("af7bf65c-7290-4250-a557-d66e0aa1e0ad.jpeg", "bouquet-presentation"),
]

FULL_W = 1400
THUMB = (700, 525)  # 4:3, matching the existing gallery tiles

total = 0
for src_name, slug in PHOTOS:
    src = os.path.join(SRC, src_name)
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")

    full = im.copy()
    if full.width > FULL_W:
        full = full.resize((FULL_W, round(full.height * FULL_W / full.width)), Image.LANCZOS)
    fp = os.path.join(OUT, slug + ".jpg")
    full.save(fp, "JPEG", quality=78, optimize=True, progressive=True)

    thumb = ImageOps.fit(im, THUMB, Image.LANCZOS, centering=(0.5, 0.4))
    tp = os.path.join(OUT, "thumb-" + slug + ".jpg")
    thumb.save(tp, "JPEG", quality=76, optimize=True, progressive=True)

    kb = (os.path.getsize(fp) + os.path.getsize(tp)) // 1024
    total += kb
    print("%-28s full %sx%s  %4d KB" % (slug, full.width, full.height, kb))

print("\n%d photographs, %d KB total" % (len(PHOTOS), total))
