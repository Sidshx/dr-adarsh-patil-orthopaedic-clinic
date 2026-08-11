# -*- coding: utf-8 -*-
"""Shared markup partials for Dr. Adarsh Patil's Orthopaedic Clinic site."""

CLINIC = "Dr. Adarsh Patil's Orthopaedic Clinic"
TAGLINE = "Bone &amp; Joint Specialists"
DOCTOR = "Dr. Adarsh D. Patil"
DEGREES = "MBBS, MS (Orthopaedics)"
ROLE = "Consultant Orthopaedic / Trauma Surgeon"
REG = "MMC2020053493, Maharashtra Medical Council"
PHONE_DISP = "+91 70205 25460"
PHONE_TEL = "+917020525460"
WA = "https://wa.me/917020525460"
EMAIL = "adarshpatilortho@gmail.com"
ADDRESS_1 = "Shop No. 4, Datta Ganesh CHS, Plot No. 101"
ADDRESS_2 = "Sector 1, Sanpada, Navi Mumbai"
ADDRESS_3 = "Maharashtra 400705, India"
ADDRESS_FULL = "Shop No. 4, Datta Ganesh CHS, Plot No. 101, Sector 1, Sanpada, Navi Mumbai, Maharashtra 400705, India"
HOURS = "Monday to Sunday, by appointment"
MAP_Q = "Datta+Ganesh+CHS,+Plot+No.+101,+Sector+1,+Sanpada,+Navi+Mumbai,+Maharashtra+400705"
MAP_LINK = "https://www.google.com/maps/search/?api=1&amp;query=" + MAP_Q
MAP_EMBED = "https://www.google.com/maps?q=" + MAP_Q + "&amp;output=embed"
GOOGLE_PROFILE = "https://share.google/PiXCMrwgPo3YnYGQm"
BASE_URL = "https://sidshx.github.io/dr-adarsh-patil-orthopaedic-clinic"
GEO_LAT = 19.06082
GEO_LNG = 73.026138

# ---------------------------------------------------------------- icons
IC = {
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 2 .7 2.9a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.2-1.2a2 2 0 0 1 2.1-.5c.9.3 1.9.6 2.9.7a2 2 0 0 1 1.7 2z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 7 10 6 10-6"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
    "wa": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 14.4c-.3-.2-1.7-.9-2-1-.3-.1-.5-.1-.7.1s-.7.9-.9 1.1c-.2.2-.3.2-.6.1a8.2 8.2 0 0 1-2.4-1.5 9 9 0 0 1-1.7-2.1c-.2-.3 0-.5.1-.6l.5-.6.3-.5v-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.2.2 2.1 3.3 5.2 4.6.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.7-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.2-.3-.2-.6-.3zM12 2a10 10 0 0 0-8.6 15L2 22l5.2-1.4A10 10 0 1 0 12 2zm0 18.2c-1.6 0-3.1-.4-4.4-1.2l-.3-.2-3.1.8.8-3-.2-.3a8.2 8.2 0 1 1 7.2 3.9z"/></svg>',
    "map": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 4-6 2v14l6-2 6 2 6-2V4l-6 2-6-2z"/><path d="M9 4v14M15 6v14"/></svg>',
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m4 12.5 5.5 5.5L20 6"/></svg>',
    "play": '<svg viewBox="0 0 12 12" aria-hidden="true"><path d="M3 2l7 4-7 4z"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    "medal": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="15" r="6"/><path d="M8.2 9.5 5 2h5l2 4M15.8 9.5 19 2h-5"/></svg>',
    "cap": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 8.5 12 4l10 4.5-10 4.5z"/><path d="M6 10.7V16c0 1.7 2.7 3 6 3s6-1.3 6-3v-5.3"/></svg>',
    "id": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="5" width="20" height="14" rx="2"/><circle cx="8.5" cy="11.5" r="2"/><path d="M5 16c.7-1.4 2-2 3.5-2s2.8.6 3.5 2M15 10h4M15 14h3"/></svg>',
    "lang": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a15 15 0 0 1 0 18M12 3a15 15 0 0 0 0 18"/></svg>',
    "google": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#4285F4" d="M23.5 12.3c0-.8-.1-1.6-.2-2.3H12v4.5h6.4a5.5 5.5 0 0 1-2.4 3.6v3h3.9c2.3-2.1 3.6-5.2 3.6-8.8z"/><path fill="#34A853" d="M12 24c3.2 0 6-1.1 8-2.9l-3.9-3a7.2 7.2 0 0 1-10.7-3.8h-4v3.1A12 12 0 0 0 12 24z"/><path fill="#FBBC05" d="M5.3 14.3a7.1 7.1 0 0 1 0-4.6v-3.1h-4a12 12 0 0 0 0 10.8l4-3.1z"/><path fill="#EA4335" d="M12 4.8c1.8 0 3.4.6 4.6 1.8l3.5-3.5A12 12 0 0 0 1.3 6.6l4 3.1A7.2 7.2 0 0 1 12 4.8z"/></svg>',
    "star": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="m12 2.5 2.9 5.9 6.6.9-4.8 4.6 1.2 6.5-5.9-3.1-5.9 3.1 1.2-6.5L2.5 9.3l6.6-.9z"/></svg>',
    "quote": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M9.5 5C6.5 6.6 4.8 9.3 4.8 12.6V19h6.4v-6.4H8.1c0-2.2.9-3.8 2.8-4.9L9.5 5zm9.4 0c-3 1.6-4.7 4.3-4.7 7.6V19h6.4v-6.4h-3.1c0-2.2.9-3.8 2.8-4.9L18.9 5z"/></svg>',
    "hospital": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 21V8l8-5 8 5v13"/><path d="M9 21v-5h6v5M12 8v4M10 10h4"/></svg>',
    # service icons
    "joint": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 3v4.2a3 3 0 0 1-1 2.2 3.5 3.5 0 0 0 0 5.2 3 3 0 0 1 1 2.2V21"/><path d="M16 3v4.2a3 3 0 0 0 1 2.2 3.5 3.5 0 0 1 0 5.2 3 3 0 0 0-1 2.2V21"/><path d="M8 12h8"/></svg>',
    "spine": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2c-2 2-2 3 0 5s2 3 0 5-2 3 0 5 2 3 0 5"/><path d="M9 4.5h6M8 9.5h8M8 14.5h8M9 19.5h6"/></svg>',
    "bone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6.5 3a2.5 2.5 0 0 0-2 4A2.5 2.5 0 1 0 7 10.5L13.5 17a2.5 2.5 0 1 0 3.5 3.5 2.5 2.5 0 0 0 3.5-3.5 2.5 2.5 0 0 0-3.5-3.5L10.5 7A2.5 2.5 0 0 0 6.5 3z"/></svg>',
    "scope": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="10" cy="10" r="6"/><path d="m14.5 14.5 6 6M8 10h4M10 8v4"/></svg>',
    "hand": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 11V4.5a1.5 1.5 0 1 1 3 0V10"/><path d="M12 10V3.5a1.5 1.5 0 1 1 3 0V10"/><path d="M15 10V5.5a1.5 1.5 0 1 1 3 0V14a7 7 0 0 1-7 7h-.5A6.5 6.5 0 0 1 4 14.5V12a1.5 1.5 0 1 1 3 0v2"/></svg>',
    "run": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="15" cy="4.5" r="2"/><path d="m8 21 2.5-5 3-2-1-5-3.5 2L7 14"/><path d="m13.5 14 2.5 2 1.5 5M13 9l4 1 2-2"/></svg>',
}


def head(title, description, canonical, og_image="assets/clinic-exterior.jpg", jsonld=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="theme-color" content="#162648">
<link rel="canonical" href="{BASE_URL}/{canonical}">

<meta property="og:type" content="website">
<meta property="og:site_name" content="{CLINIC}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="{og_image}">
<meta property="og:locale" content="en_IN">
<meta property="og:url" content="{BASE_URL}/{canonical}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{og_image}">

<link rel="icon" href="assets/favicon.ico" sizes="any">
<link rel="icon" type="image/png" href="assets/logo-mark-256.png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@75..125,400..900&family=DM+Sans:opsz,wght@9..40,400..700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
{jsonld}
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
"""


def topbar():
    msg = (f'<span>{CLINIC} — Bone &amp; Joint Specialists, Sanpada, Navi Mumbai</span>'
           f'<span>{DOCTOR}, {DEGREES} — {ROLE}</span>'
           f'<span>Consultations {HOURS} — call {PHONE_DISP}</span>')
    return f"""<div class="topbar">
  <div class="topbar__track" aria-hidden="true">
    <div class="topbar__group">{msg}</div>
    <div class="topbar__group">{msg}</div>
  </div>
  <p class="visually-hidden">{CLINIC} — Bone and Joint Specialists, Sanpada, Navi Mumbai. Consultations {HOURS}.</p>
</div>
"""


def header():
    return f"""<header class="site-header">
  <div class="container header-row">
    <a class="brand" href="index.html">
      <img class="brand__mark" src="assets/logo-mark.png" width="600" height="611" alt="{CLINIC} logo: four coloured squares showing a shoulder, hip, spine and knee">
      <span class="brand__text">
        <span class="brand__name">{DOCTOR}</span>
        <span class="brand__sub">{TAGLINE}</span>
        <span class="brand__cred">{DEGREES} &middot; {ROLE}</span>
      </span>
    </a>
    <div class="header-contacts">
      <a class="hc hc--phone" href="tel:{PHONE_TEL}">
        <span class="hc__icon">{IC['phone']}</span>
        <span><span class="hc__label">Phone No.</span><span class="hc__value">{PHONE_DISP}</span></span>
      </a>
      <a class="hc hc--mail" href="mailto:{EMAIL}">
        <span class="hc__icon">{IC['mail']}</span>
        <span><span class="hc__label">Email id.</span><span class="hc__value">{EMAIL}</span></span>
      </a>
    </div>
    <div class="header-cta">
      <a class="btn btn--primary" href="contact.html">Book Appointment</a>
    </div>
  </div>
</header>
"""


def navbar(active):
    pages = [("Home", "index.html"), ("About", "about.html"), ("Services", "services.html"),
             ("Gallery", "gallery.html"), ("Contact", "contact.html")]
    links = "".join(
        f'<li><a href="{href}"{" aria-current=\"page\"" if href == active else ""}>{label}</a></li>'
        for label, href in pages)
    return f"""<div class="navbar">
  <div class="container navbar__inner">
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="primary-nav">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
      Menu
    </button>
    <nav aria-label="Primary">
      <ul class="nav-links" id="primary-nav">{links}</ul>
    </nav>
    <div class="nav-social">
      <a href="tel:{PHONE_TEL}" aria-label="Call the clinic on {PHONE_DISP}">{IC['phone']}</a>
      <a href="{WA}" target="_blank" rel="noopener" aria-label="Message the clinic on WhatsApp">{IC['wa']}</a>
      <a href="mailto:{EMAIL}" aria-label="Email the clinic at {EMAIL}">{IC['mail']}</a>
      <a href="{MAP_LINK}" target="_blank" rel="noopener" aria-label="Open the clinic location in Google Maps">{IC['map']}</a>
    </div>
  </div>
</div>
"""


def footer():
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-nap">
        <div class="footer-brand">
          <img src="assets/logo-mark.png" width="600" height="611" alt="">
          <span>
            <strong>{CLINIC}</strong>
            <span>{TAGLINE}</span>
          </span>
        </div>
        <address>
          {DOCTOR}, {DEGREES}<br>
          {ROLE}<br>
          {ADDRESS_1},<br>
          {ADDRESS_2},<br>
          {ADDRESS_3}
        </address>
      </div>
      <div>
        <h4>Quick Links</h4>
        <ul class="footer-links">
          <li><a href="index.html">Home</a></li>
          <li><a href="about.html">About the Doctor</a></li>
          <li><a href="services.html">Services</a></li>
          <li><a href="gallery.html">Gallery</a></li>
          <li><a href="contact.html">Contact &amp; Location</a></li>
          <li><a href="services.html#conditions">Conditions Treated</a></li>
          <li><a href="services.html#expertise">Expertise</a></li>
          <li><a href="services.html#clinic-services">Clinic Services</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul class="footer-links">
          <li><a href="tel:{PHONE_TEL}">{PHONE_DISP}</a></li>
          <li><a href="{WA}" target="_blank" rel="noopener">WhatsApp {PHONE_DISP}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="{MAP_LINK}" target="_blank" rel="noopener">Get directions</a></li>
        </ul>
      </div>
      <div>
        <h4>Consultation Hours</h4>
        <table class="hours-table">
          <tbody>
            <tr><th scope="row" style="color:#fff">Monday &ndash; Sunday</th><td style="color:#b9c4d8">By appointment</td></tr>
          </tbody>
        </table>
        <p style="margin-top:0.9rem;font-size:0.88rem">Please call or WhatsApp to confirm a consultation slot before visiting.</p>
        <p style="font-size:0.88rem"><strong style="color:#fff">Registration:</strong><br>{REG}</p>
      </div>
    </div>
    <p class="disclaimer">Information on this website is provided for general awareness only and does not replace professional medical consultation.</p>
    <div class="footer-bottom">
      <span>&copy; <span data-year>2026</span> {CLINIC}. All rights reserved.</span>
      <span>Languages spoken: English, Hindi, Marathi</span>
    </div>
  </div>
</footer>
"""


def fabs():
    return f"""<div class="fab-stack">
  <a class="fab fab--call" href="tel:{PHONE_TEL}" aria-label="Call the clinic on {PHONE_DISP}">{IC['phone']}</a>
  <a class="fab fab--wa" href="{WA}" target="_blank" rel="noopener" aria-label="Chat with the clinic on WhatsApp">{IC['wa']}</a>
</div>
"""


def tail(reviews=False):
    extra = '<script src="js/reviews.js" defer></script>\n' if reviews else ''
    return """<script src="js/main.js" defer></script>
""" + extra + """</body>
</html>
"""


def lightbox():
    return """<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Clinic photo viewer">
  <button class="lightbox__close" type="button" aria-label="Close photo viewer">&times;</button>
  <button class="lightbox__nav lightbox__nav--prev" type="button" aria-label="Previous photo">&#8249;</button>
  <button class="lightbox__nav lightbox__nav--next" type="button" aria-label="Next photo">&#8250;</button>
  <div>
    <img src="" alt="">
    <p class="lightbox__cap"></p>
  </div>
</div>
"""


GALLERY_ITEMS = [
    ("assets/thumb-exterior.jpg", "assets/clinic-exterior.jpg",
     "Clinic entrance on the street in Sector 1, Sanpada, with the illuminated signboard above the glass door",
     "Clinic entrance, Sector 1, Sanpada"),
    ("assets/thumb-reception.jpg", "assets/clinic-reception.jpg",
     "Reception corridor seen through the branded glass partition, with a wood-slat wall and warm lighting",
     "Reception and waiting corridor"),
    ("assets/thumb-exam-room.jpg", "assets/clinic-exam-room.jpg",
     "Examination room with a padded examination table, instrument trolley and white-tiled walls",
     "Examination room"),
]


# Photographs from the clinic's opening ceremony, Saturday 18 July 2026.
# Captions stay descriptive; individuals other than the chief guest named on
# the event banner are not identified by name.
INAUGURATION_DATE = "Saturday, 18 July 2026"

INAUGURATION_ITEMS = [
    ("ribbon-cutting",
     "The ribbon being cut at the clinic entrance during the opening ceremony, with Dr. Adarsh Patil and invited guests standing on either side",
     "Cutting the ribbon at the opening"),
    ("chief-guest-address",
     "Hon. Shri Ganesh Naik, Minister, Government of Maharashtra, speaking into a microphone in front of the clinic's inauguration banner, with invited guests seated behind",
     "Hon. Shri Ganesh Naik addressing the gathering"),
    ("address-wide",
     "Wider view of the stage during the address, with invited guests seated on either side and attendees watching",
     "The ceremony under way"),
    ("guests-on-dais",
     "Invited guests seated on the stage in front of the inauguration banner, with balloons on either side",
     "Invited guests on the dais"),
    ("guests-seated",
     "Invited guests seated together in front of the event banner during the ceremony",
     "Guests at the ceremony"),
    ("felicitation",
     "Dr. Adarsh Patil presenting a bouquet of flowers to the chief guest, who has been given a ceremonial shawl",
     "Welcoming the chief guest"),
    ("group-photograph",
     "Group photograph of invited guests, family members and neighbours standing together in front of the inauguration banner",
     "Guests and family at the opening"),
    ("family-at-signage",
     "Dr. Adarsh Patil and three guests holding a small idol together beneath the clinic's wall signage on the wood-slat reception wall",
     "Inside the clinic on opening day"),
    ("consulting-room-guests",
     "Dr. Adarsh Patil standing with Mrs. Sujata Patil, Mayor of Navi Mumbai, and other guests in the consulting room, with framed certificates on the wall behind",
     "With Mrs. Sujata Patil, Mayor of Navi Mumbai"),
    ("consulting-room-visit",
     "Dr. Adarsh Patil standing with visitors beside the consultation desk in the consulting room",
     "Visitors on opening day"),
    ("consulting-room-gathering",
     "Family members and guests seated together in the consulting room, with bouquets and balloons around them",
     "Family and guests at the clinic"),
    ("bouquet-presentation",
     "Mrs. Manda Mhatre, MLA, Belapur Constituency, presenting a bouquet of flowers to Dr. Adarsh Patil inside the clinic",
     "With Mrs. Manda Mhatre, MLA, Belapur"),
]


def inauguration_items():
    return [(f"assets/inauguration/thumb-{slug}.jpg",
             f"assets/inauguration/{slug}.jpg", alt, cap)
            for slug, alt, cap in INAUGURATION_ITEMS]


def gallery_grid(items=None):
    if items is None:
        items = GALLERY_ITEMS
    out = ['<div class="gallery">']
    for thumb, full, alt, cap in items:
        out.append(
            f'<button class="gallery__item" type="button" data-full="{full}" data-caption="{cap}">'
            f'<img src="{thumb}" alt="{alt}" loading="lazy" width="700" height="525">'
            f'<span class="gallery__cap">{cap}</span></button>')
    out.append("</div>")
    return "\n".join(out)


# ---------------------------------------------------------------- JSON-LD
def jsonld_clinic(page_url, extra_physician=""):
    abs_url = f"{BASE_URL}/{page_url}"
    return """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MedicalClinic",
  "@id": "%(url)s#clinic",
  "name": "%(clinic_plain)s — Bone & Joint Specialists",
  "description": "Orthopaedic clinic in Sanpada, Navi Mumbai providing consultation and treatment for bone, joint, spine and trauma conditions.",
  "image": "%(base)s/assets/clinic-exterior.jpg",
  "logo": "%(base)s/assets/logo-mark.png",
  "url": "%(url)s",
  "telephone": "+91-7020525460",
  "email": "%(email)s",
  "sameAs": ["https://share.google/PiXCMrwgPo3YnYGQm"],
  "hasMap": "https://www.google.com/maps?q=Datta+Ganesh+CHS,+Plot+No.+101,+Sector+1,+Sanpada,+Navi+Mumbai,+Maharashtra+400705",
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 19.06082,
    "longitude": 73.026138
  },
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Shop No. 4, Datta Ganesh CHS, Plot No. 101, Sector 1",
    "addressLocality": "Sanpada, Navi Mumbai",
    "addressRegion": "Maharashtra",
    "postalCode": "400705",
    "addressCountry": "IN"
  },
  "openingHoursSpecification": [{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
    "description": "Monday to Sunday, by appointment"
  }],
  "openingHours": "Mo-Su",
  "availableLanguage": ["English","Hindi","Marathi"],
  "medicalSpecialty": "Orthopedic",
  "physician": {
    "@type": "Physician",
    "@id": "%(url)s#physician",
    "name": "Dr. Adarsh D. Patil",
    "honorificSuffix": "MBBS, MS (Orthopaedics)",
    "jobTitle": "Consultant Orthopaedic / Trauma Surgeon",
    "medicalSpecialty": ["Orthopedic Surgery","Spine Surgery"],
    "identifier": "MMC2020053493, Maharashtra Medical Council",
    "email": "%(email)s",
    "telephone": "+91-7020525460",
    "knowsLanguage": ["English","Hindi","Marathi"],
    "alumniOf": [
      {"@type": "CollegeOrUniversity", "name": "MGM Medical College Hospital & Research Centre, Aurangabad"},
      {"@type": "CollegeOrUniversity", "name": "Maharashtra University of Health Sciences (MUHS)"}
    ],
    "affiliation": [
      {"@type": "Hospital", "name": "MPCT Hospital, Sanpada"},
      {"@type": "Hospital", "name": "MGM Hospital & Medical College, Vashi"},
      {"@type": "Hospital", "name": "Suraj Hospital, Sanpada"}
    ],
    "award": "Gold Medal – Orthopaedics",
    "hasCredential": [
      "AHA BLS & ACLS Certification (2024)",
      "Basic Course in Biomedical Research (2024)",
      "Poster Presentation, 41st MOACON Orthopaedic Conference (2025)",
      "Completed Fellowship in Hand Surgery"
    ]
  },
  "areaServed": ["Sanpada","Vashi","Navi Mumbai","Maharashtra"]
}
</script>""" % {"url": abs_url, "base": BASE_URL, "clinic_plain": "Dr. Adarsh Patil's Orthopaedic Clinic", "email": EMAIL}


def jsonld_faq(pairs):
    import json
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pairs
        ],
    }
    return '<script type="application/ld+json">\n' + json.dumps(data, indent=2) + '\n</script>'


def jsonld_breadcrumb(name, url):
    import json
    data = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE_URL}/index.html"},
            {"@type": "ListItem", "position": 2, "name": name, "item": f"{BASE_URL}/{url}"},
        ],
    }
    return '<script type="application/ld+json">\n' + json.dumps(data, indent=2) + '\n</script>'
