# -*- coding: utf-8 -*-
"""Static site builder for Dr. Adarsh Patil's Orthopaedic Clinic."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from partials import *  # noqa

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


def write(name, html):
    p = os.path.join(ROOT, name)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(html)
    print('wrote', name, len(html) // 1024, 'KB')


# ------------------------------------------------------------------ data
SERVICES = [
    ("joint-arthritis", "joint", "green", "Joint Pain &amp; Arthritis Care",
     "Assessment and treatment of joint pain, osteoarthritis, inflammatory arthritis, gout and osteoporosis, including medication, injections and rehabilitation guidance."),
    ("spine-pain", "spine", "pink", "Spine, Back &amp; Neck Pain",
     "Evaluation of back and neck pain, disc-related problems and nerve compression, with conservative care, physiotherapy referral and spine surgery when indicated."),
    ("trauma", "bone", "blue", "Fractures &amp; Trauma Surgery",
     "Care for fractures and injuries, including plaster and bracing, fracture fixation, and Ilizarov external fixation for complex or non-healing bone injuries."),
    ("arthroscopy", "scope", "orange", "Arthroscopy &amp; Joint Replacement",
     "Minimally invasive keyhole joint surgery (arthroscopy) for shoulder and knee problems, and joint replacement surgery (arthroplasty) for advanced joint damage."),
    ("hand-surgery", "hand", "blue", "Hand Surgery",
     "Surgical and non-surgical treatment of hand and wrist conditions, following a completed fellowship in hand surgery."),
    ("sports", "run", "green", "Sports &amp; Ligament Injuries",
     "Diagnosis and management of ligament injuries, sports-related injuries, shoulder problems and bone deformities, with a return-to-activity plan."),
]

CONDITIONS = [
    ("Joint pain", "Pain, stiffness or swelling in the knee, hip, shoulder or other joints."),
    ("Arthritis", "Osteoarthritis and inflammatory arthritis affecting one or more joints."),
    ("Osteoporosis", "Reduced bone density and the fracture risk that comes with it."),
    ("Gout", "Sudden joint pain and swelling caused by uric acid crystal deposits."),
    ("Back &amp; neck pain", "Spinal pain, disc-related problems and nerve compression symptoms."),
    ("Shoulder problems", "Stiffness, instability, rotator cuff and other shoulder conditions."),
    ("Fractures &amp; trauma", "Broken bones and injuries from falls, road traffic and workplace accidents."),
    ("Ligament injuries", "Ligament tears and instability, commonly of the knee and ankle."),
    ("Sports injuries", "Injuries arising from training, recreational and competitive sport."),
    ("Bone deformities", "Congenital and acquired deformities affecting limb alignment or length."),
]

PROCEDURES = [
    ("Arthroscopy", "Minimally invasive joint surgery performed through small keyhole incisions using a camera."),
    ("Joint replacement surgery", "Arthroplasty, in which a damaged joint surface is replaced with an implant."),
    ("Spine surgery", "Surgical treatment of spinal conditions where non-surgical care has not resolved symptoms."),
    ("Fracture fixation &amp; trauma surgery", "Realignment and stabilisation of broken bones with plates, screws, nails or wires."),
    ("Ilizarov external fixation", "A ring-frame external fixator used for complex fractures, non-union and deformity correction."),
    ("Hand surgery", "Procedures for conditions affecting the hand and wrist."),
]

HOSPITALS = [
    ("MPCT Hospital", "Sanpada"),
    ("MGM Hospital &amp; Medical College", "Vashi"),
    ("Suraj Hospital", "Sanpada"),
]

FAQS = [
    ("How do I book an appointment?",
     "Consultations are by appointment, Monday to Sunday. Call or send a WhatsApp message to +91 70205 25460, or email adarshpatilortho@gmail.com with a preferred day and time, and the clinic will confirm a slot."),
    ("What should I bring to my first visit?",
     "Please bring any previous X-rays, MRI or CT films and reports, blood test results, a list of the medicines you currently take, discharge or operation summaries from earlier treatment, and a photo identity document."),
    ("Do I need a referral from another doctor?",
     "A referral is not required. You can contact the clinic directly to book a consultation. If another doctor has given you a referral letter or reports, please bring them along."),
    ("Which conditions are seen at the clinic?",
     "The clinic sees joint pain, arthritis, osteoporosis, gout, back and neck pain, shoulder problems, fractures and trauma, ligament injuries, sports injuries and bone deformities."),
    ("Are surgical procedures carried out at the clinic?",
     "The Sanpada clinic is used for consultation, clinical examination, dressing and follow-up. Surgical procedures are performed at the affiliated hospitals: MPCT Hospital, Sanpada; MGM Hospital & Medical College, Vashi; and Suraj Hospital, Sanpada."),
    ("Which languages are spoken at the clinic?",
     "Consultations can be held in English, Hindi or Marathi."),
    ("Where is the clinic located?",
     "Shop No. 4, Datta Ganesh CHS, Plot No. 101, Sector 1, Sanpada, Navi Mumbai, Maharashtra 400705, India. The clinic is at street level with a signboard above the entrance."),
    ("How long will my consultation take?",
     "The length of a consultation depends on the condition being assessed and whether imaging or tests need to be reviewed. Please arrive a few minutes before your appointment time."),
]


def service_cards(link_base="services.html"):
    out = ['<div class="grid grid--3">']
    for slug, icon, tone, title, desc in SERVICES:
        out.append(f"""<article class="card reveal">
  <span class="card__icon" data-tone="{tone}">{IC[icon]}</span>
  <h3>{title}</h3>
  <p>{desc}</p>
  <a class="card__more" href="{link_base}#{slug}">Read More {IC['arrow']}</a>
</article>""")
    out.append('</div>')
    return "\n".join(out)


def hospital_cards():
    out = ['<div class="grid grid--3">']
    for name, place in HOSPITALS:
        out.append(f"""<article class="card hospital-card reveal">
  <span class="card__icon" data-tone="blue">{IC['hospital']}</span>
  <span class="k">Affiliated hospital</span>
  <h3>{name}</h3>
  <p>{place}, Navi Mumbai</p>
</article>""")
    out.append('</div>')
    return "\n".join(out)


def faq_block(items):
    out = ['<div class="faq">']
    for i, (q, a) in enumerate(items):
        open_ = 'true' if i == 0 else 'false'
        exp = 'true' if i == 0 else 'false'
        out.append(f"""<div class="faq__item" data-open="{open_}">
  <h3 style="margin:0"><button class="faq__q" type="button" aria-expanded="{exp}">{q}</button></h3>
  <div class="faq__a"><div><p>{a}</p></div></div>
</div>""")
    out.append('</div>')
    return "\n".join(out)


def map_block():
    return f"""<div class="map-frame">
  <iframe src="{MAP_EMBED}" title="Google Map showing the location of {CLINIC} in Sector 1, Sanpada, Navi Mumbai" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
</div>"""


def contact_info_list():
    return f"""<ul class="info-list">
  <li><span class="ico">{IC['pin']}</span><span><span class="k">Clinic address</span><span class="v">{ADDRESS_1},<br>{ADDRESS_2},<br>{ADDRESS_3}</span></span></li>
  <li><span class="ico">{IC['phone']}</span><span><span class="k">Phone &amp; WhatsApp</span><a class="v" href="tel:{PHONE_TEL}">{PHONE_DISP}</a></span></li>
  <li><span class="ico">{IC['mail']}</span><span><span class="k">Email</span><a class="v" href="mailto:{EMAIL}">{EMAIL}</a></span></li>
  <li><span class="ico">{IC['clock']}</span><span><span class="k">Consultation hours</span><span class="v">{HOURS}</span></span></li>
  <li><span class="ico">{IC['lang']}</span><span><span class="k">Languages</span><span class="v">English, Hindi, Marathi</span></span></li>
  <li><span class="ico">{IC['id']}</span><span><span class="k">Registration</span><span class="v">{REG}</span></span></li>
</ul>"""


# ------------------------------------------------------------------ index
def build_index():
    jsonld = jsonld_clinic("index.html") + "\n" + jsonld_faq([(q, a) for q, a in FAQS])
    h = head(
        f"{CLINIC} — Bone &amp; Joint Specialists, Sanpada, Navi Mumbai",
        "Orthopaedic clinic in Sanpada, Navi Mumbai. Dr. Adarsh D. Patil, MBBS, MS (Orthopaedics), Consultant Orthopaedic / Trauma Surgeon. Consultations Monday to Sunday, by appointment.",
        "index.html", jsonld=jsonld)

    hero = f"""<section class="hero" aria-label="Introduction">
  <div class="hero__media">
    <img src="assets/hero-doctor.jpg" alt="{DOCTOR} seated at the consulting desk in his clinic" width="575" height="980" fetchpriority="high">
  </div>
  <div class="hero__panel" aria-hidden="true"></div>
  <div class="hero__edge" aria-hidden="true"></div>
  <div class="container hero__inner">
    <div class="hero__content">
      <div class="hero-slide is-active">
        <h1 class="hero__headline">
          <span>{DOCTOR}</span>
          <span>Orthopaedic &amp; Trauma Surgeon</span>
          <span class="accent">Bone, Joint &amp; Spine Care</span>
        </h1>
        <p class="hero__text">Consultation, diagnosis and treatment for bone, joint, spine and trauma conditions at our clinic in Sector 1, Sanpada, Navi Mumbai. {DEGREES}. Registration {REG}.</p>
        <ul class="hero__points">
          <li><span class="tick">{IC['play']}</span> Joint pain, arthritis, back and neck pain</li>
          <li><span class="tick">{IC['play']}</span> Fractures, trauma and ligament injuries</li>
        </ul>
        <a class="btn btn--primary" href="contact.html">Book Appointment</a>
      </div>
      <div class="hero-slide">
        <h1 class="hero__headline">
          <span>Surgical &amp; Non-Surgical</span>
          <span>Orthopaedic Treatment</span>
          <span class="accent">In Sanpada, Navi Mumbai</span>
        </h1>
        <p class="hero__text">Arthroscopy, joint replacement, spine surgery, fracture fixation, Ilizarov external fixation and hand surgery, carried out at affiliated hospitals in Navi Mumbai.</p>
        <ul class="hero__points">
          <li><span class="tick">{IC['play']}</span> Consultations {HOURS}</li>
          <li><span class="tick">{IC['play']}</span> English, Hindi and Marathi spoken</li>
        </ul>
        <a class="btn btn--primary" href="services.html">View Services</a>
      </div>
      <div class="hero__dots" role="tablist" aria-label="Introduction slides">
        <button type="button" role="tab" aria-selected="true" aria-label="Slide 1"></button>
        <button type="button" role="tab" aria-selected="false" aria-label="Slide 2"></button>
      </div>
    </div>
  </div>
</section>"""

    about = f"""<section class="section" id="about">
  <div class="container split">
    <div class="split__media split__media--frame reveal">
      <img src="assets/doctor-photo.jpg" alt="{DOCTOR} at his consulting desk at the clinic in Sanpada" width="765" height="1020" loading="lazy">
    </div>
    <div class="reveal">
      <span class="eyebrow">About the doctor</span>
      <h2 class="doctor-name">{DOCTOR}</h2>
      <p class="doctor-degrees">{DEGREES}</p>
      <p class="doctor-role">{ROLE} &middot; Orthopaedic Surgeon, Spine &amp; Pain Specialist, Spine Surgeon (Ortho)</p>
      <hr class="rule">
      <p>Dr. Adarsh D. Patil consults at {CLINIC} in Sector 1, Sanpada, Navi Mumbai. His practice covers bone, joint and spine conditions, sports and ligament injuries, and fracture and trauma care, in both non-surgical and surgical forms.</p>
      <p>Consultations include clinical examination, review of imaging and reports, an explanation of the diagnosis, and a treatment plan discussed with the patient. Surgical treatment, when it is indicated, is carried out at affiliated hospitals in Navi Mumbai.</p>
      <ul class="facts">
        <li><span class="ico">{IC['cap']}</span><span><span class="k">Qualifications</span><span class="v">MBBS &middot; MS (Orthopaedics)</span></span></li>
        <li><span class="ico">{IC['id']}</span><span><span class="k">Registration</span><span class="v">{REG}</span></span></li>
        <li><span class="ico">{IC['lang']}</span><span><span class="k">Languages</span><span class="v">English, Hindi, Marathi</span></span></li>
        <li><span class="ico">{IC['clock']}</span><span><span class="k">Consultation hours</span><span class="v">{HOURS}</span></span></li>
      </ul>
      <a class="btn btn--navy" href="about.html">More about Dr. Patil {IC['arrow']}</a>
    </div>
  </div>
</section>"""

    stats = f"""<section class="stats" aria-label="Qualifications at a glance">
  <div class="container">
    <div class="stats__grid">
      <div class="stat"><span class="stat__key">MBBS, MS</span><span class="stat__label">Orthopaedics</span></div>
      <div class="stat"><span class="stat__key">Gold Medal</span><span class="stat__label">Orthopaedics</span></div>
      <div class="stat"><span class="stat__key">Fellowship</span><span class="stat__label">Hand Surgery</span></div>
      <div class="stat"><span class="stat__key">Mon&ndash;Sun</span><span class="stat__label">By Appointment</span></div>
    </div>
  </div>
</section>"""

    services = f"""<section class="section section--tint" id="services">
  <div class="container">
    <div class="section-head section-head--center">
      <span class="eyebrow">What we treat</span>
      <h2>Orthopaedic Services</h2>
      <p class="lead">Consultation and treatment across bone, joint, spine and trauma care. Each service is described in more detail on the services page.</p>
    </div>
    {service_cards()}
    <p style="text-align:center;margin-top:2.25rem"><a class="btn btn--navy" href="services.html">See all services, conditions and procedures {IC['arrow']}</a></p>
  </div>
</section>"""

    band_walk = f"""<section class="band band--tall band--logo-top" aria-label="Mobility and movement">
  <img src="assets/banner-active-walking.jpg" alt="A woman walking along a waterfront promenade" width="1376" height="768" loading="lazy">
  <div class="band__caption">
    <div class="container">
      <h2>Getting back to everyday movement</h2>
      <p>Treatment plans are built around the activity you need to return to &mdash; walking, working, climbing stairs or sport &mdash; and are reviewed at follow-up.</p>
    </div>
  </div>
</section>"""

    hospitals = f"""<section class="section" id="hospitals">
  <div class="container">
    <div class="section-head section-head--center">
      <span class="eyebrow">Hospital affiliations</span>
      <h2>Affiliated Hospitals</h2>
      <p class="lead">Surgical procedures and inpatient care are carried out at the following hospitals in Navi Mumbai.</p>
    </div>
    {hospital_cards()}
  </div>
</section>"""

    approach = f"""<section class="section section--navy" id="visit">
  <div class="container split split--reverse">
    <div class="split__media reveal">
      <img src="assets/clinic-exterior.jpg" alt="Street-level view of the clinic entrance with the illuminated signboard and potted plants" width="896" height="1195" loading="lazy" style="max-height:520px">
    </div>
    <div class="reveal">
      <span class="eyebrow">Your visit</span>
      <h2>What to expect at the clinic</h2>
      <p class="lead">A consultation follows the same clear sequence, so you know what happens at each step.</p>
      <ul class="checklist" style="margin-top:1.75rem">
        <li><span class="tick">{IC['check']}</span><span><strong>History and examination</strong><span>Your symptoms, previous treatment and daily activity are discussed, followed by a clinical examination.</span></span></li>
        <li><span class="tick">{IC['check']}</span><span><strong>Review of imaging and reports</strong><span>X-rays, MRI or CT films and blood reports you bring with you are reviewed during the consultation.</span></span></li>
        <li><span class="tick">{IC['check']}</span><span><strong>Explanation of the diagnosis</strong><span>The findings are explained in English, Hindi or Marathi, whichever you prefer.</span></span></li>
        <li><span class="tick">{IC['check']}</span><span><strong>Treatment plan and follow-up</strong><span>Non-surgical and surgical options are set out, along with the follow-up schedule.</span></span></li>
      </ul>
      <p style="margin-top:1.75rem"><a class="btn btn--primary" href="contact.html">Book an appointment</a></p>
    </div>
  </div>
</section>"""

    gallery = f"""<section class="section section--tint" id="gallery">
  <div class="container">
    <div class="section-head section-head--center">
      <span class="eyebrow">Inside the clinic</span>
      <h2>Clinic Gallery</h2>
      <p class="lead">The consulting rooms, reception and examination area at Sector 1, Sanpada. Select a photo to view it larger.</p>
    </div>
    {gallery_grid()}
    <p style="text-align:center;margin-top:2rem"><a class="btn btn--outline" href="gallery.html">Open the full gallery {IC['arrow']}</a></p>
  </div>
</section>"""

    inaug_home = f"""<section class="section" id="inauguration">
  <div class="container">
    <div class="section-head section-head--center">
      <span class="eyebrow">Opening ceremony</span>
      <h2>Clinic Inauguration</h2>
      <p class="lead">The clinic was inaugurated on {INAUGURATION_DATE} at Sector 1, Sanpada, by the chief guest Hon. Shri Ganesh Naik, Minister, Government of Maharashtra.</p>
    </div>
    {gallery_grid(inauguration_items()[:3])}
    <p style="text-align:center;margin-top:2rem"><a class="btn btn--outline" href="gallery.html#inauguration">See all inauguration photos {IC['arrow']}</a></p>
  </div>
</section>"""

    band_wait = f"""<section class="band band--logo-left" aria-label="Clinic waiting area">
  <img src="assets/banner-waiting-area.jpg" alt="An older couple seated in the clinic waiting area" width="1600" height="406" loading="lazy">
  <div class="band__caption">
    <div class="container">
      <h2>Care for every age</h2>
      <p>From sports and workplace injuries to age-related joint and bone conditions, appointments can be arranged Monday to Sunday.</p>
    </div>
  </div>
</section>"""

    faq = f"""<section class="section" id="faq">
  <div class="container container-narrow">
    <div class="section-head section-head--center">
      <span class="eyebrow">Questions</span>
      <h2>Frequently Asked Questions</h2>
      <p class="lead">Practical information about booking, what to bring, and how the clinic works.</p>
    </div>
    {faq_block(FAQS[:6])}
    <p style="text-align:center;margin-top:1.75rem"><a class="btn btn--outline" href="contact.html#faq">See all questions {IC['arrow']}</a></p>
  </div>
</section>"""

    contact = f"""<section class="section section--tint" id="contact">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Find us</span>
      <h2>Clinic Location &amp; Contact</h2>
    </div>
    <div class="contact-grid">
      <div>{contact_info_list()}
        <p style="margin-top:1.5rem;display:flex;gap:0.75rem;flex-wrap:wrap">
          <a class="btn btn--primary" href="tel:{PHONE_TEL}">Call the clinic</a>
          <a class="btn btn--outline" href="{WA}" target="_blank" rel="noopener">WhatsApp</a>
        </p>
      </div>
      {map_block()}
    </div>
  </div>
</section>"""

    reviews = f"""<section class="section section--tint reviews" id="reviews">
  <div class="container">
    <div class="section-head section-head--center">
      <span class="eyebrow">Patient feedback</span>
      <h2>Reviews From Our Patients</h2>
      <p class="lead">Reviews published by patients on the clinic&rsquo;s Google Business Profile. They are shown here as written by their authors.</p>
    </div>
  </div>
  <div class="reviews__summary" data-reviews-summary hidden>
    <div class="container">
      <div class="reviews__badge">
        <span class="reviews__g" aria-hidden="true">{IC['google']}</span>
        <span class="reviews__score" data-reviews-rating></span>
        <span class="reviews__stars" data-reviews-stars aria-hidden="true"></span>
        <span class="reviews__count" data-reviews-count></span>
      </div>
    </div>
  </div>
  <div class="reviews__viewport" data-reviews-track-wrap>
    <div class="reviews__track" data-reviews-track>
      <p class="reviews__loading">Loading reviews from Google&hellip;</p>
    </div>
  </div>
  <div class="container">
    <p class="reviews__foot">
      <a class="btn btn--outline" href="{GOOGLE_PROFILE}" target="_blank" rel="noopener">Read all reviews on Google {IC['arrow']}</a>
    </p>
    <p class="reviews__attrib">Reviews are the opinions of their individual authors and are sourced from Google. They describe personal experience and are not a promise or guarantee of any medical outcome. Last synced <span data-reviews-updated>&mdash;</span>.</p>
  </div>
</section>"""

    html = (h + topbar() + header() + navbar("index.html")
            + '<main id="main">\n' + hero + about + stats + services + band_walk
            + hospitals + approach + gallery + inaug_home + band_wait + reviews + faq + contact + '\n</main>\n'
            + footer() + fabs() + lightbox() + tail(reviews=True))
    write('index.html', html)


# ------------------------------------------------------------------ about
def build_about():
    jsonld = jsonld_clinic("about.html") + "\n" + jsonld_breadcrumb("About", "about.html")
    h = head(
        f"About {DOCTOR} — {CLINIC}",
        "Dr. Adarsh D. Patil, MBBS, MS (Orthopaedics), Consultant Orthopaedic / Trauma Surgeon in Sanpada, Navi Mumbai. Qualifications, registration, certifications and hospital affiliations.",
        "about.html", og_image="assets/doctor-photo.jpg", jsonld=jsonld)

    page_hero = f"""<section class="page-hero">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> &nbsp;/&nbsp; About</p>
    <h1>About {DOCTOR}</h1>
    <p>{DEGREES} &middot; {ROLE} &middot; Registration {REG}</p>
  </div>
</section>"""

    intro = f"""<section class="section">
  <div class="container split">
    <div class="split__media split__media--frame reveal">
      <img src="assets/doctor-photo.jpg" alt="{DOCTOR} seated at his consulting desk" width="765" height="1020">
    </div>
    <div class="reveal">
      <span class="eyebrow">Profile</span>
      <h2 class="doctor-name">{DOCTOR}</h2>
      <p class="doctor-degrees">{DEGREES}</p>
      <p class="doctor-role">{ROLE}</p>
      <hr class="rule">
      <p>Dr. Adarsh D. Patil is an orthopaedic and trauma surgeon practising at {CLINIC} in Sector 1, Sanpada, Navi Mumbai. He is registered with the Maharashtra Medical Council under registration number MMC2020053493.</p>
      <p>His clinical work covers joint and bone conditions, spine and pain problems, fractures and trauma, ligament and sports injuries, and hand conditions. Care ranges from medication, injections, plaster and bracing through to arthroscopy, joint replacement, spine surgery, fracture fixation, Ilizarov external fixation and hand surgery.</p>
      <p>Consultations are held in English, Hindi or Marathi, {HOURS}.</p>
      <ul class="pill-list" style="margin-top:1.5rem">
        <li><span class="pill">Orthopaedic Surgeon</span></li>
        <li><span class="pill">Spine &amp; Pain Specialist</span></li>
        <li><span class="pill">Spine Surgeon (Ortho)</span></li>
      </ul>
    </div>
  </div>
</section>"""

    edu = f"""<section class="section section--tint" id="education">
  <div class="container">
    <div class="grid grid--2" style="align-items:start">
      <div class="reveal">
        <span class="eyebrow">Education</span>
        <h2>Qualifications</h2>
        <ul class="timeline" style="margin-top:1.75rem">
          <li>
            <h4>MBBS</h4>
            <p>MGM Medical College Hospital &amp; Research Centre, Aurangabad</p>
          </li>
          <li>
            <h4>MS Orthopaedics</h4>
            <p>Maharashtra University of Health Sciences (MUHS)</p>
          </li>
        </ul>
        <div class="award-badge" style="margin-top:2rem">
          <span class="ico">{IC['medal']}</span>
          <span>
            <strong>Gold Medal &mdash; Orthopaedics</strong>
            <span>Awarded across his MBBS and MS (Orthopaedics) training</span>
          </span>
        </div>
      </div>
      <div class="reveal">
        <span class="eyebrow">Training</span>
        <h2>Certifications</h2>
        <ul class="checklist" style="margin-top:1.75rem">
          <li><span class="tick">{IC['check']}</span><span><strong>AHA BLS &amp; ACLS Certification (2024)</strong><span>American Heart Association Basic and Advanced Cardiovascular Life Support.</span></span></li>
          <li><span class="tick">{IC['check']}</span><span><strong>Basic Course in Biomedical Research (2024)</strong><span>Foundational training in research methods and ethics.</span></span></li>
          <li><span class="tick">{IC['check']}</span><span><strong>Poster Presentation, 41st MOACON Orthopaedic Conference (2025)</strong><span>Presented at the Maharashtra Orthopaedic Association conference.</span></span></li>
          <li><span class="tick">{IC['check']}</span><span><strong>Completed Fellowship in Hand Surgery</strong><span>Dedicated training in the surgical care of hand and wrist conditions.</span></span></li>
        </ul>
        <ul class="facts" style="margin-top:2rem">
          <li><span class="ico">{IC['id']}</span><span><span class="k">Medical registration</span><span class="v">{REG}</span></span></li>
          <li><span class="ico">{IC['lang']}</span><span><span class="k">Languages</span><span class="v">English, Hindi, Marathi</span></span></li>
        </ul>
      </div>
    </div>
  </div>
</section>"""

    hospitals = f"""<section class="section" id="hospitals">
  <div class="container">
    <div class="section-head section-head--center">
      <span class="eyebrow">Hospital affiliations</span>
      <h2>Affiliated Hospitals</h2>
      <p class="lead">Surgical procedures and inpatient care are carried out at the following hospitals in Navi Mumbai.</p>
    </div>
    {hospital_cards()}
  </div>
</section>"""

    band = f"""<section class="band band--logo-left" aria-label="Clinic waiting area">
  <img src="assets/banner-waiting-area.jpg" alt="An older couple seated in the clinic waiting area" width="1600" height="406" loading="lazy">
  <div class="band__caption">
    <div class="container">
      <h2>Consultations Monday to Sunday</h2>
      <p>All consultations are by appointment. Call or WhatsApp {PHONE_DISP} to arrange a time.</p>
    </div>
  </div>
</section>"""

    cta = f"""<section class="section section--navy">
  <div class="container container-narrow" style="text-align:center">
    <span class="eyebrow" style="justify-content:center">Appointments</span>
    <h2>Arrange a consultation</h2>
    <p class="lead">Call or send a WhatsApp message to {PHONE_DISP}, or email {EMAIL}.</p>
    <p style="margin-top:1.75rem;display:flex;gap:0.75rem;justify-content:center;flex-wrap:wrap">
      <a class="btn btn--primary" href="tel:{PHONE_TEL}">Call {PHONE_DISP}</a>
      <a class="btn btn--ghost" href="contact.html">Contact page</a>
    </p>
  </div>
</section>"""

    html = (h + topbar() + header() + navbar("about.html")
            + '<main id="main">\n' + page_hero + intro + edu + hospitals + band + cta + '\n</main>\n'
            + footer() + fabs() + tail())
    write('about.html', html)


# ------------------------------------------------------------------ services
def build_services():
    jsonld = jsonld_clinic("services.html") + "\n" + jsonld_breadcrumb("Services", "services.html")
    h = head(
        f"Orthopaedic Services, Conditions &amp; Procedures — {CLINIC}",
        "Conditions treated and procedures offered at Dr. Adarsh Patil's Orthopaedic Clinic, Sanpada, Navi Mumbai: joint pain, arthritis, spine care, fractures and trauma, arthroscopy, joint replacement and hand surgery.",
        "services.html", jsonld=jsonld)

    page_hero = f"""<section class="page-hero">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> &nbsp;/&nbsp; Services</p>
    <h1>Services</h1>
    <p>Consultation, diagnosis and treatment for bone, joint, spine and trauma conditions at Sector 1, Sanpada, Navi Mumbai.</p>
  </div>
</section>"""

    overview = f"""<section class="section">
  <div class="container">
    <div class="section-head section-head--center">
      <span class="eyebrow">Areas of practice</span>
      <h2>Orthopaedic Services</h2>
    </div>
    {service_cards(link_base="")}
  </div>
</section>"""

    # detailed sections per service
    details = ['<section class="section section--tint"><div class="container">']
    details.append("""<div class="section-head"><span class="eyebrow">In detail</span><h2>Service Details</h2></div>""")
    detail_copy = {
        "joint-arthritis": [
            "Joint pain can come from wear of the joint surface, inflammation, crystal deposits such as gout, or from reduced bone density. Assessment starts with a clinical examination and a review of any X-rays or blood reports you bring with you.",
            "Treatment may include medication, activity modification, physiotherapy referral, bracing, or intra-articular injections. Where joint damage is advanced and symptoms are not controlled, joint replacement surgery is discussed as an option.",
        ],
        "spine-pain": [
            "Back and neck pain is assessed for its origin — muscular, disc-related, degenerative, or associated with nerve compression. Symptoms such as radiating pain, numbness or weakness are examined specifically.",
            "Most spinal problems are managed without surgery, using medication, posture and activity guidance and physiotherapy. Spine surgery is considered where symptoms persist or where there are progressive neurological signs.",
        ],
        "trauma": [
            "Fracture and trauma care covers injuries from falls, road traffic accidents, workplace incidents and sport. Initial care includes assessment, pain relief, and immobilisation with plaster or bracing where appropriate.",
            "Operative treatment includes fracture fixation with plates, screws, nails or wires, and Ilizarov external fixation for complex fractures, non-union and deformity correction. Surgery is carried out at the affiliated hospitals listed on the about page.",
        ],
        "arthroscopy": [
            "Arthroscopy is minimally invasive joint surgery carried out through small incisions using a camera and fine instruments. It is used for diagnosis and treatment of certain knee and shoulder problems, including ligament and cartilage injuries.",
            "Joint replacement surgery (arthroplasty) replaces a damaged joint surface with an implant. The decision to proceed is based on symptoms, examination findings, imaging and how much daily activity is affected.",
        ],
        "hand-surgery": [
            "Hand and wrist conditions are assessed for the effect on grip, dexterity and daily function. Non-surgical care includes splinting, injections and hand therapy guidance.",
            "Surgical treatment of hand and wrist conditions is offered following a completed fellowship in hand surgery.",
        ],
        "sports": [
            "Ligament and sports injuries are examined for joint stability, range of motion and associated cartilage or tendon damage. Shoulder problems and bone deformities are assessed in the same consultation setting.",
            "Management is staged: initial protection and pain control, progressive rehabilitation, and reconstruction where instability persists. A return-to-activity plan is set out and reviewed at follow-up.",
        ],
    }
    for slug, icon, tone, title, desc in SERVICES:
        paras = "".join(f"<p>{p}</p>" for p in detail_copy[slug])
        details.append(f"""<article class="card reveal" id="{slug}" style="margin-bottom:1.25rem">
  <div style="display:flex;gap:1rem;align-items:center;margin-bottom:0.75rem">
    <span class="card__icon" data-tone="{tone}" style="margin-bottom:0">{IC[icon]}</span>
    <h3 style="margin:0">{title}</h3>
  </div>
  {paras}
</article>""")
    details.append('</div></section>')
    details = "\n".join(details)

    cond_rows = "".join(
        f"""<article class="card reveal"><h3 style="font-size:1.05rem">{n}</h3><p>{d}</p></article>"""
        for n, d in CONDITIONS)
    conditions = f"""<section class="section" id="conditions">
  <div class="container">
    <div class="section-head section-head--center">
      <span class="eyebrow">Conditions</span>
      <h2>Conditions Treated</h2>
      <p class="lead">Ten condition groups are seen at the clinic. Bring any earlier films and reports to your consultation.</p>
    </div>
    <div class="grid grid--3">{cond_rows}</div>
  </div>
</section>"""

    proc_rows = "".join(
        f"""<li><span class="tick">{IC['check']}</span><span><strong>{n}</strong><span>{d}</span></span></li>"""
        for n, d in PROCEDURES)
    procedures = f"""<section class="section section--navy" id="procedures">
  <div class="container split">
    <div class="split__media reveal">
      <img src="assets/clinic-exam-room.jpg" alt="Examination room with a padded examination table and instrument trolley" width="896" height="1195" loading="lazy" style="max-height:520px">
    </div>
    <div class="reveal">
      <span class="eyebrow">Procedures</span>
      <h2>Procedures Offered</h2>
      <p class="lead">Surgical procedures are performed at the affiliated hospitals in Navi Mumbai; the Sanpada clinic is used for consultation, examination and follow-up.</p>
      <ul class="checklist" style="margin-top:1.75rem">{proc_rows}</ul>
    </div>
  </div>
</section>"""

    band = f"""<section class="band band--logo-top" aria-label="Returning to activity">
  <img src="assets/banner-active-walking.jpg" alt="A woman walking along a waterfront promenade" width="1376" height="768" loading="lazy">
  <div class="band__caption">
    <div class="container">
      <h2>Follow-up and rehabilitation</h2>
      <p>Recovery is reviewed at scheduled follow-up visits, with rehabilitation adjusted to how the joint or bone is healing.</p>
    </div>
  </div>
</section>"""

    cta = f"""<section class="section">
  <div class="container container-narrow" style="text-align:center">
    <h2>Discuss your symptoms at a consultation</h2>
    <p class="lead">Consultations are {HOURS}. Call or WhatsApp {PHONE_DISP}.</p>
    <p style="margin-top:1.75rem;display:flex;gap:0.75rem;justify-content:center;flex-wrap:wrap">
      <a class="btn btn--primary" href="contact.html">Book Appointment</a>
      <a class="btn btn--outline" href="{WA}" target="_blank" rel="noopener">WhatsApp the clinic</a>
    </p>
  </div>
</section>"""

    html = (h + topbar() + header() + navbar("services.html")
            + '<main id="main">\n' + page_hero + overview + details + conditions + procedures + band + cta
            + '\n</main>\n' + footer() + fabs() + tail())
    write('services.html', html)


# ------------------------------------------------------------------ gallery
def build_gallery():
    jsonld = jsonld_clinic("gallery.html") + "\n" + jsonld_breadcrumb("Gallery", "gallery.html")
    h = head(
        f"Clinic Gallery — {CLINIC}, Sanpada",
        "Photographs of Dr. Adarsh Patil's Orthopaedic Clinic in Sector 1, Sanpada, Navi Mumbai: the street entrance, reception corridor, examination room and the clinic's opening ceremony.",
        "gallery.html", jsonld=jsonld)

    page_hero = """<section class="page-hero">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> &nbsp;/&nbsp; Gallery</p>
    <h1>Inside the Clinic</h1>
    <p>Photographs of the clinic at Shop No. 4, Datta Ganesh CHS, Sector 1, Sanpada, Navi Mumbai, and of its opening ceremony. Select any photo to view it larger.</p>
  </div>
</section>"""

    grid = f"""<section class="section">
  <div class="container">
    <div class="section-head section-head--center">
      <span class="eyebrow">The premises</span>
      <h2>Clinic photographs</h2>
    </div>
    {gallery_grid()}
  </div>
</section>"""

    inauguration = f"""<section class="section section--tint" id="inauguration">
  <div class="container">
    <div class="section-head section-head--center">
      <span class="eyebrow">Opening ceremony</span>
      <h2>Clinic inauguration</h2>
      <p>The clinic was inaugurated on {INAUGURATION_DATE} at Sector 1, Sanpada. The ribbon was cut by the chief guest, Hon. Shri Ganesh Naik, Minister, Government of Maharashtra. He was joined by Mrs. Sujata Patil, Mayor of Navi Mumbai, Mrs. Manda Mhatre, MLA, Belapur Constituency, and Mr. Dashrath Bhagat, Deputy Mayor of Navi Mumbai, along with family, friends and neighbours.</p>
    </div>
    {gallery_grid(inauguration_items())}
  </div>
</section>"""

    band = f"""<section class="band band--tall band--logo-left" aria-label="Clinic waiting area">
  <img src="assets/banner-waiting-area.jpg" alt="An older couple seated in the clinic waiting area" width="1600" height="406" loading="lazy">
  <div class="band__caption">
    <div class="container">
      <h2>Waiting area</h2>
      <p>Seating is provided next to reception. Appointments help keep waiting time short, so please call ahead.</p>
    </div>
  </div>
</section>"""

    notes = """<section class="section section--tint">
  <div class="container">
    <p style="text-align:center;margin:0"><a class="btn btn--primary" href="contact.html">Book an appointment</a></p>
  </div>
</section>"""

    html = (h + topbar() + header() + navbar("gallery.html")
            + '<main id="main">\n' + page_hero + grid + band + inauguration + notes + '\n</main>\n'
            + footer() + fabs() + lightbox() + tail())
    write('gallery.html', html)


# ------------------------------------------------------------------ contact
def build_contact():
    jsonld = (jsonld_clinic("contact.html") + "\n" + jsonld_faq(FAQS) + "\n"
              + jsonld_breadcrumb("Contact", "contact.html"))
    h = head(
        f"Contact &amp; Location — {CLINIC}, Sanpada, Navi Mumbai",
        "Contact Dr. Adarsh Patil's Orthopaedic Clinic, Shop No. 4, Datta Ganesh CHS, Sector 1, Sanpada, Navi Mumbai 400705. Phone and WhatsApp +91 70205 25460. Consultations Monday to Sunday, by appointment.",
        "contact.html", jsonld=jsonld)

    page_hero = f"""<section class="page-hero">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> &nbsp;/&nbsp; Contact</p>
    <h1>Contact &amp; Location</h1>
    <p>Consultations are {HOURS}. Call or send a WhatsApp message to confirm a slot before visiting.</p>
  </div>
</section>"""

    main = f"""<section class="section">
  <div class="container contact-grid">
    <div class="reveal">
      <span class="eyebrow">Clinic details</span>
      <h2>Get in touch</h2>
      {contact_info_list()}
      <p style="margin-top:1.75rem;display:flex;gap:0.75rem;flex-wrap:wrap">
        <a class="btn btn--primary" href="tel:{PHONE_TEL}">Call {PHONE_DISP}</a>
        <a class="btn btn--outline" href="{WA}" target="_blank" rel="noopener">WhatsApp</a>
        <a class="btn btn--outline" href="mailto:{EMAIL}">Email</a>
      </p>
    </div>
    <div class="reveal">
      <span class="eyebrow">Enquiry</span>
      <h2>Appointment enquiry</h2>
      <p class="form-note">This form is not connected to a booking system. Submitting it opens your own email application with the details filled in, addressed to {EMAIL}. For a faster reply, call or WhatsApp <a href="tel:{PHONE_TEL}">{PHONE_DISP}</a>. Please do not send urgent or emergency requests through this form.</p>
      <form id="enquiry-form" novalidate>
        <div class="field">
          <label for="f-name">Your name</label>
          <input id="f-name" name="name" type="text" autocomplete="name" required>
        </div>
        <div class="field">
          <label for="f-phone">Phone number</label>
          <input id="f-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel">
        </div>
        <div class="field">
          <label for="f-concern">Reason for the appointment</label>
          <select id="f-concern" name="concern">
            <option>Joint pain or arthritis</option>
            <option>Back or neck pain</option>
            <option>Fracture or injury</option>
            <option>Shoulder or ligament problem</option>
            <option>Hand or wrist problem</option>
            <option>Follow-up visit</option>
            <option>Other</option>
          </select>
        </div>
        <div class="field">
          <label for="f-message">Message</label>
          <textarea id="f-message" name="message" placeholder="Briefly describe your symptoms and a preferred day and time."></textarea>
        </div>
        <button class="btn btn--navy" type="submit">Open email with these details</button>
        <p id="form-status" role="status" style="margin-top:0.85rem;font-size:0.9rem;color:var(--ink-soft)"></p>
      </form>
    </div>
  </div>
</section>"""

    map_sec = f"""<section class="section section--tint" id="location">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Location</span>
      <h2>How to find the clinic</h2>
      <p class="lead">{ADDRESS_FULL}</p>
    </div>
    {map_block()}
    <div class="grid grid--3" style="margin-top:1.75rem">
      <article class="card"><span class="card__icon" data-tone="blue">{IC['map']}</span><h3>Getting here</h3><p>The clinic is in Sector 1, Sanpada, within Navi Mumbai. Use the map above for turn-by-turn directions.</p><a class="card__more" href="{MAP_LINK}" target="_blank" rel="noopener">Open in Google Maps {IC['arrow']}</a></article>
      <article class="card"><span class="card__icon" data-tone="orange">{IC['clock']}</span><h3>Consultation hours</h3><p>{HOURS}. Please confirm your slot by phone or WhatsApp before travelling.</p></article>
      <article class="card"><span class="card__icon" data-tone="green">{IC['check']}</span><h3>What to bring</h3><p>Previous X-ray, MRI or CT films and reports, blood test results, your current medicine list, earlier discharge summaries and a photo ID.</p></article>
    </div>
  </div>
</section>"""

    faq = f"""<section class="section" id="faq">
  <div class="container container-narrow">
    <div class="section-head section-head--center">
      <span class="eyebrow">Questions</span>
      <h2>Frequently Asked Questions</h2>
    </div>
    {faq_block(FAQS)}
  </div>
</section>"""

    html = (h + topbar() + header() + navbar("contact.html")
            + '<main id="main">\n' + page_hero + main + map_sec + faq + '\n</main>\n'
            + footer() + fabs() + tail())
    write('contact.html', html)


if __name__ == '__main__':
    build_index()
    build_about()
    build_services()
    build_gallery()
    build_contact()
    print('done')
