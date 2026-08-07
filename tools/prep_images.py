from PIL import Image
import os

A = os.path.join(os.path.dirname(__file__), '..', 'assets')
A = os.path.abspath(A)

def save(im, name, q=80, maxw=None):
    if maxw and im.width > maxw:
        h = round(im.height * maxw / im.width)
        im = im.resize((maxw, h), Image.LANCZOS)
    p = os.path.join(A, name)
    im.convert('RGB').save(p, 'JPEG', quality=q, optimize=True, progressive=True)
    print(name, im.size, os.path.getsize(p) // 1024, 'KB')

# --- compress photos in place (keep originals under -orig) ---
photos = {
    'doctor-photo.jpg': 1000,
    'clinic-exterior.jpg': 1100,
    'clinic-reception.jpg': 1400,
    'clinic-exam-room.jpg': 1100,
    'banner-waiting-area.jpg': 1600,
    'banner-active-walking.jpg': 1600,
}
for f, w in photos.items():
    src = os.path.join(A, f)
    orig = os.path.join(A, f.replace('.jpg', '-orig.jpg'))
    if not os.path.exists(orig):
        os.rename(src, orig)
    im = Image.open(orig)
    save(im, f, 78, w)

# --- hero crop of doctor: portrait-ish tall crop focused on subject ---
d = Image.open(os.path.join(A, 'doctor-photo-orig.jpg'))
W, H = d.size  # 765x1020
# subject sits centre-left; crop a 3:4 window biased left
cw = int(W * 0.86)
cx = int(W * 0.30 - cw / 2)
cx = max(0, min(cx, W - cw))
ch = min(H, int(cw * 4 / 3))
crop = d.crop((cx, 0, cx + cw, ch))
save(crop, 'hero-doctor.jpg', 82, 900)

# --- thumbnails for gallery ---
for f, name in [('clinic-exterior.jpg', 'thumb-exterior.jpg'),
                ('clinic-reception.jpg', 'thumb-reception.jpg'),
                ('clinic-exam-room.jpg', 'thumb-exam-room.jpg')]:
    im = Image.open(os.path.join(A, f))
    save(im, name, 76, 700)

# --- favicon from logo ---
logo = Image.open(os.path.join(A, 'logo-mark.png')).convert('RGBA')
# trim white background to transparent-ish: keep as is, just square it
side = max(logo.size)
sq = Image.new('RGBA', (side, side), (255, 255, 255, 0))
sq.paste(logo, ((side - logo.width) // 2, (side - logo.height) // 2))
sq.resize((256, 256), Image.LANCZOS).save(os.path.join(A, 'logo-mark-256.png'))
sq.resize((180, 180), Image.LANCZOS).save(os.path.join(A, 'apple-touch-icon.png'))
ico = [sq.resize((s, s), Image.LANCZOS) for s in (16, 32, 48)]
ico[1].save(os.path.join(A, 'favicon.ico'), sizes=[(16, 16), (32, 32), (48, 48)])
print('favicon done')
