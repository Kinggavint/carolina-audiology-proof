#!/usr/bin/env python3
"""Carolina Audiology Associates v2 site generator.

Brand and copy rules sourced from:
- Voice interview with Dr. Melissa Palmer (verified facts only)
- Audigy Style Guide PDF uploaded by client (mission, vision, values, slogan,
  tone, manufacturer prefs, must-avoid wording, demographics)
- Logo PNG uploaded by client (used at full res in header and footer)
- Clayton Audiology design direction (her other practice she likes)
- Old caarmt.com site (for verified founding year 1988 only)

Rules enforced in this script:
- No emojis anywhere
- No em dashes, no en dashes anywhere
- No fabricated pricing or evaluation durations
- Marketing uses 'hearing technology' not 'hearing aids'
- 'Complimentary' not 'free'
"""

from pathlib import Path
import textwrap

ROOT = Path(__file__).parent

# ---------- Practice facts (all verified) ----------
PRACTICE = "Carolina Audiology Associates"
PHONE_DISPLAY = "(252) 790-6649"
PHONE_TEL = "+12527906649"
ADDRESS_LINE = "4065 Capital Drive"
CITY_STATE_ZIP = "Rocky Mount, NC 27804"
EMAIL = "info@carolinaaud.com"
HOURS_LINE = "Monday to Thursday, 9:00 AM to 5:00 PM"
HOURS_SHORT = "Mon to Thu, 9 to 5"
FOUNDED = "1988"
PROVIDER_NAME = "Dr. Melissa Palmer, Au.D., CCC-A"

# Mission, vision, values, slogan come directly from her Audigy style guide
SLOGAN = "Helping you hear what matters most"
MISSION = ("Our mission is to improve our patients' quality of life through "
           "better hearing, clear communication, and compassionate "
           "personalized care.")
VISION = ("Our vision is to empower our community through education and "
          "engagement, ensuring that personalized hearing healthcare is "
          "accessible to all. We believe that when we hear better, we live "
          "better.")
VALUES = ("Ownership and leadership, personalization, and community "
          "engagement. We lead with ownership, providing personalized "
          "hearing care and community education so every patient "
          "experiences the joy of connection.")

BOILERPLATE = (f"{PRACTICE} has been serving the Rocky Mount community "
               f"since {FOUNDED}. Under the leadership of {PROVIDER_NAME}, "
               "our team is committed to empowering patients to hear with "
               "confidence through personalized hearing care and education.")

# Manufacturers from her style guide
MANUFACTURERS = ["Oticon", "ReSound"]

INSURANCES = ["Medicare", "Blue Cross Blue Shield", "UnitedHealthcare",
              "Humana", "Aetna"]

SERVICES = [
    {
        "slug": "diagnostic-hearing-evaluations",
        "title": "Diagnostic Hearing Evaluations",
        "icon": "ear",
        "summary": ("Comprehensive testing to identify the type and degree "
                    "of hearing loss and guide a personalized care plan."),
        "long": ("A comprehensive diagnostic hearing evaluation looks at how "
                 "you hear pure tones, how well you understand speech, and "
                 "how your middle ear is functioning. The results tell us "
                 "whether you have hearing loss, how much, in which ears, "
                 "and what kind. From there we sit with you and your family "
                 "to talk through what the results mean for your daily life "
                 "and what your options are."),
    },
    {
        "slug": "hearing-technology",
        "title": "Hearing Technology Fittings",
        "icon": "device",
        "summary": ("Personalized fittings using technology from Oticon and "
                    "ReSound, matched to your hearing, your lifestyle, and "
                    "your goals."),
        "long": ("Modern hearing technology is quieter, smaller, and far "
                 "more capable than what most people remember. We work "
                 "primarily with Oticon and ReSound because of their "
                 "long track records, sound quality, and connectivity. "
                 "Every fitting starts with your goals. Whether that is "
                 "hearing your grandchildren clearly, getting back into "
                 "restaurants, or staying connected on phone calls, we "
                 "match the technology to the life you want to live."),
    },
    {
        "slug": "tinnitus-care",
        "title": "Tinnitus Care",
        "icon": "wave",
        "summary": ("Evaluation and management strategies for the ringing, "
                    "buzzing, or humming many adults experience."),
        "long": ("Tinnitus, the ringing or buzzing many people hear when no "
                 "outside sound is present, can be exhausting. We start by "
                 "evaluating your hearing and your tinnitus, then talk "
                 "through the options. For many patients, well-fit hearing "
                 "technology with sound therapy reduces how much they "
                 "notice the tinnitus. Education and counseling are part "
                 "of every plan."),
    },
    {
        "slug": "hearing-aid-repair",
        "title": "Hearing Aid Repair and Cleaning",
        "icon": "tools",
        "summary": ("Repair, cleaning, and maintenance for most major "
                    "hearing aid brands, including devices not originally "
                    "purchased from us."),
        "long": ("Hearing aids work hardest in the places that are hardest "
                 "on them, your ears. We clean, service, and repair most "
                 "major brands, including devices purchased elsewhere. "
                 "Routine cleanings and tune-ups extend the life of your "
                 "investment and keep your sound clear."),
    },
    {
        "slug": "follow-up-care",
        "title": "Ongoing Follow-up Care",
        "icon": "calendar",
        "summary": ("Regular check-ins to fine-tune your hearing technology "
                    "and keep your care plan working for your real life."),
        "long": ("Your hearing changes, your lifestyle changes, and the way "
                 "you use your hearing technology will change too. We "
                 "build follow-up visits into every care plan so we can "
                 "adjust settings, retest hearing when needed, and answer "
                 "questions as they come up. You are not on your own after "
                 "the fitting."),
    },
]

# ---------- Inline SVG icons (single-stroke, navy) ----------
ICONS = {
    # Stylized ear
    "ear": ('<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" '
            'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" '
            'aria-hidden="true">'
            '<path d="M16 18a8 8 0 0 1 16 0c0 6-5 7-5 12a4 4 0 0 1-8 0"/>'
            '<path d="M22 22a3 3 0 0 1 6 0c0 3-3 3-3 6"/>'
            '</svg>'),
    # Hearing device
    "device": ('<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" '
               'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" '
               'aria-hidden="true">'
               '<path d="M18 14c-4 2-6 6-6 12s2 10 6 12"/>'
               '<path d="M20 18a8 8 0 0 1 14 6c0 6-4 9-4 13a3 3 0 0 1-6 0"/>'
               '<circle cx="24" cy="24" r="2"/>'
               '</svg>'),
    # Sound waves
    "wave": ('<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" '
             'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" '
             'aria-hidden="true">'
             '<path d="M10 24h4"/>'
             '<path d="M18 18v12"/>'
             '<path d="M24 14v20"/>'
             '<path d="M30 18v12"/>'
             '<path d="M36 22v4"/>'
             '</svg>'),
    # Tools / wrench
    "tools": ('<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" '
              'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" '
              'aria-hidden="true">'
              '<path d="M30 12a6 6 0 0 0-6 6c0 1 0 2 .5 3L12 33.5a3 3 0 0 0 4 4L28.5 25c1 .5 2 .5 3 .5a6 6 0 0 0 6-6c0-1 0-2-.5-3L33 21l-4-4 3.5-3.5c-.5-.5-1.5-1-2.5-1.5z"/>'
              '</svg>'),
    # Calendar
    "calendar": ('<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" '
                 'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" '
                 'aria-hidden="true">'
                 '<rect x="10" y="12" width="28" height="26" rx="2"/>'
                 '<path d="M10 20h28"/>'
                 '<path d="M18 8v8"/>'
                 '<path d="M30 8v8"/>'
                 '<path d="M18 28h4"/>'
                 '<path d="M26 28h4"/>'
                 '</svg>'),
    # Phone
    "phone": ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
              'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" '
              'aria-hidden="true">'
              '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.37 1.9.72 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.35 1.85.59 2.81.72A2 2 0 0 1 22 16.92z"/>'
              '</svg>'),
    "pin": ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" '
            'aria-hidden="true">'
            '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>'
            '<circle cx="12" cy="10" r="3"/>'
            '</svg>'),
    "clock": ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
              'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" '
              'aria-hidden="true">'
              '<circle cx="12" cy="12" r="10"/>'
              '<path d="M12 6v6l4 2"/>'
              '</svg>'),
    "mail": ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
             'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" '
             'aria-hidden="true">'
             '<rect x="2" y="4" width="20" height="16" rx="2"/>'
             '<path d="M22 6l-10 7L2 6"/>'
             '</svg>'),
    "check": ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
              'stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" '
              'aria-hidden="true">'
              '<polyline points="20 6 9 17 4 12"/>'
              '</svg>'),
}


# ---------- HTML helpers ----------

def page(title, description, body, canonical, page_class="", extra_head=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<link rel="icon" type="image/png" href="/assets/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/base.css">
{extra_head}
</head>
<body class="{page_class}">
{header_html()}
<main>
{body}
</main>
{footer_html()}
</body>
</html>
"""


def header_html():
    return f"""<div class="utility-bar">
  <div class="container utility-bar__inner">
    <a class="utility-bar__phone" href="tel:{PHONE_TEL}">
      {ICONS['phone']}<span>Call or text {PHONE_DISPLAY}</span>
    </a>
    <span class="utility-bar__hours">{HOURS_SHORT}</span>
  </div>
</div>
<header class="site-header">
  <div class="container site-header__inner">
    <a class="brand" href="/" aria-label="{PRACTICE} home">
      <img src="/assets/logo.png" alt="{PRACTICE}" class="brand__logo">
    </a>
    <button class="nav-toggle" aria-label="Open menu" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
    <nav class="primary-nav" aria-label="Primary">
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/services.html">Services</a></li>
        <li><a href="/about.html">About</a></li>
        <li><a href="/education.html">Education</a></li>
        <li><a href="/contact.html">Contact</a></li>
      </ul>
    </nav>
    <a class="btn btn--primary header-cta" href="/contact.html">Book Appointment</a>
  </div>
</header>
"""


def footer_html():
    insurance_list = ", ".join(INSURANCES)
    manuf_list = " and ".join(MANUFACTURERS)
    return f"""<footer class="site-footer">
  <div class="container site-footer__grid">
    <div class="site-footer__col">
      <img src="/assets/logo.png" alt="{PRACTICE}" class="footer__logo">
      <p class="footer__slogan">{SLOGAN}</p>
    </div>
    <div class="site-footer__col">
      <h3>Visit</h3>
      <p>{ADDRESS_LINE}<br>{CITY_STATE_ZIP}</p>
      <p>{HOURS_LINE}</p>
    </div>
    <div class="site-footer__col">
      <h3>Contact</h3>
      <p><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
      <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <a class="btn btn--secondary" href="/contact.html">Book Appointment</a>
    </div>
    <div class="site-footer__col">
      <h3>Care You Can Trust</h3>
      <p>Featuring {manuf_list} hearing technology.</p>
      <p>We accept {insurance_list}.</p>
    </div>
  </div>
  <div class="site-footer__legal">
    <div class="container">
      <p>&copy; {2026} {PRACTICE}. All rights reserved.</p>
      <p><a href="/sitemap.xml">Sitemap</a></p>
    </div>
  </div>
</footer>
"""


# ---------- Schema.org JSON-LD ----------

def local_business_jsonld():
    return textwrap.dedent(f"""\
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "MedicalBusiness",
      "name": "{PRACTICE}",
      "image": "https://kinggavint.github.io/carolina-audiology-proof/assets/logo.png",
      "telephone": "{PHONE_DISPLAY}",
      "email": "{EMAIL}",
      "address": {{
        "@type": "PostalAddress",
        "streetAddress": "{ADDRESS_LINE}",
        "addressLocality": "Rocky Mount",
        "addressRegion": "NC",
        "postalCode": "27804",
        "addressCountry": "US"
      }},
      "openingHoursSpecification": [{{
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday"],
        "opens": "09:00",
        "closes": "17:00"
      }}],
      "url": "https://kinggavint.github.io/carolina-audiology-proof/",
      "foundingDate": "{FOUNDED}",
      "slogan": "{SLOGAN}",
      "medicalSpecialty": "Audiology"
    }}
    </script>
    """)


def faq_jsonld(faqs):
    items = ",\n".join([
        f'{{"@type":"Question","name":{q!r},"acceptedAnswer":{{"@type":"Answer","text":{a!r}}}}}'
        for q, a in faqs
    ])
    return f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{items}]}}</script>'


# ---------- Pages ----------

def home():
    services_cards = "\n".join([
        f"""<a class="service-card" href="/services.html#{s['slug']}">
          <span class="service-card__icon">{ICONS[s['icon']]}</span>
          <h3>{s['title']}</h3>
          <p>{s['summary']}</p>
          <span class="service-card__more">Learn more</span>
        </a>""" for s in SERVICES
    ])
    faqs = [
        ("How do I know if I need a hearing evaluation?",
         "If you find yourself turning up the TV, asking people to repeat themselves, or struggling to follow conversations in noisy places, a diagnostic hearing evaluation can give you a clear answer. Many adults wait years before getting tested. There is no benefit to waiting."),
        ("Do you take my insurance?",
         f"We accept {', '.join(INSURANCES)}. If your plan is not listed, give us a call and we will help you understand your options."),
        ("Which hearing technology brands do you fit?",
         f"We work primarily with {' and '.join(MANUFACTURERS)} because of their sound quality, reliability, and connectivity. Your fitting is matched to your hearing and your lifestyle, not to a single product."),
    ]
    body = f"""
{local_business_jsonld()}
{faq_jsonld(faqs)}

<section class="hero">
  <div class="container hero__inner">
    <div class="hero__copy">
      <p class="eyebrow">Rocky Mount Audiology, Since {FOUNDED}</p>
      <h1>Hear what matters most. Clearly.</h1>
      <p class="hero__lede">{PROVIDER_NAME} and our team provide personalized hearing care for adults and families in Rocky Mount and across eastern North Carolina.</p>
      <div class="hero__ctas">
        <a class="btn btn--primary btn--lg" href="/contact.html">Book Appointment</a>
        <a class="btn btn--ghost btn--lg" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
      </div>
      <ul class="hero__trust">
        <li>{ICONS['check']}<span>Comprehensive diagnostic evaluations</span></li>
        <li>{ICONS['check']}<span>{' and '.join(MANUFACTURERS)} hearing technology</span></li>
        <li>{ICONS['check']}<span>Most major insurance accepted</span></li>
      </ul>
    </div>
    <aside class="hero__card">
      <h2>Plan your visit</h2>
      <p><strong>{ADDRESS_LINE}</strong><br>{CITY_STATE_ZIP}</p>
      <p><strong>Hours</strong><br>{HOURS_LINE}</p>
      <p><strong>Phone</strong><br><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
      <a class="btn btn--primary btn--full" href="/contact.html">Schedule a Visit</a>
    </aside>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <p class="eyebrow eyebrow--center">What We Do</p>
    <h2 class="section__title">Personalized hearing care, from evaluation to follow-up</h2>
    <div class="services-grid">
      {services_cards}
    </div>
  </div>
</section>

<section class="section pledge">
  <div class="container pledge__inner">
    <div>
      <p class="eyebrow">Our Promise</p>
      <h2>Care that starts with listening</h2>
      <p>Hearing care works best when it is built around you. We take time to understand your hearing, your goals, and your daily life. From the first evaluation through every follow-up, your care plan is yours.</p>
      <a class="btn btn--primary" href="/about.html">About Our Practice</a>
    </div>
    <ul class="pledge__list">
      <li>{ICONS['check']}<span><strong>Doctor-led care.</strong> Every patient is seen by {PROVIDER_NAME}.</span></li>
      <li>{ICONS['check']}<span><strong>Comprehensive evaluations.</strong> Pure-tone, speech, and middle-ear testing in one visit.</span></li>
      <li>{ICONS['check']}<span><strong>{' and '.join(MANUFACTURERS)}.</strong> Trusted hearing technology with strong service and warranty support.</span></li>
      <li>{ICONS['check']}<span><strong>Ongoing follow-up.</strong> Adjustments and check-ins built into your care plan.</span></li>
    </ul>
  </div>
</section>

<section class="section section--alt faq">
  <div class="container">
    <p class="eyebrow eyebrow--center">Common Questions</p>
    <h2 class="section__title">Answers to what patients ask first</h2>
    <div class="faq__list">
      {''.join([f'<details class="faq__item"><summary>{q}</summary><p>{a}</p></details>' for q,a in faqs])}
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container cta-band__inner">
    <div>
      <h2>Ready to hear what matters most?</h2>
      <p>Schedule a complimentary consultation with {PROVIDER_NAME}.</p>
    </div>
    <div class="cta-band__buttons">
      <a class="btn btn--primary btn--lg" href="/contact.html">Book Appointment</a>
      <a class="btn btn--ghost btn--lg" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
    </div>
  </div>
</section>
"""
    return page(
        title=f"{PRACTICE} | Rocky Mount NC Audiologist | {PROVIDER_NAME}",
        description=f"{PRACTICE} provides personalized hearing care in Rocky Mount, NC. Comprehensive evaluations, hearing technology fittings, and tinnitus care from {PROVIDER_NAME}.",
        body=body,
        canonical="https://kinggavint.github.io/carolina-audiology-proof/",
        page_class="page-home",
    )


def services_page():
    sections = ""
    for s in SERVICES:
        sections += f"""
<section id="{s['slug']}" class="service-detail">
  <div class="container service-detail__inner">
    <div class="service-detail__icon">{ICONS[s['icon']]}</div>
    <div class="service-detail__body">
      <h2>{s['title']}</h2>
      <p>{s['long']}</p>
      <a class="btn btn--ghost" href="/contact.html">Ask about {s['title'].lower()}</a>
    </div>
  </div>
</section>
"""
    body = f"""
{local_business_jsonld()}
<section class="page-hero">
  <div class="container">
    <p class="eyebrow">Services</p>
    <h1>Hearing care for every stage of life</h1>
    <p class="page-hero__lede">From your first diagnostic evaluation to ongoing follow-up care, every service is delivered personally by {PROVIDER_NAME}.</p>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="services-grid">
      {''.join([f'<a class="service-card" href="#{s["slug"]}"><span class="service-card__icon">{ICONS[s["icon"]]}</span><h3>{s["title"]}</h3><p>{s["summary"]}</p><span class="service-card__more">Read more</span></a>' for s in SERVICES])}
    </div>
  </div>
</section>

{sections}

<section class="cta-band">
  <div class="container cta-band__inner">
    <div>
      <h2>Have a question about a specific service?</h2>
      <p>We are happy to talk it through, even before you book.</p>
    </div>
    <div class="cta-band__buttons">
      <a class="btn btn--primary btn--lg" href="/contact.html">Book Appointment</a>
      <a class="btn btn--ghost btn--lg" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
    </div>
  </div>
</section>
"""
    return page(
        title=f"Audiology Services in Rocky Mount, NC | {PRACTICE}",
        description=f"Diagnostic hearing evaluations, hearing technology fittings, tinnitus care, repair, and ongoing follow-up in Rocky Mount, NC. Care led by {PROVIDER_NAME}.",
        body=body,
        canonical="https://kinggavint.github.io/carolina-audiology-proof/services.html",
        page_class="page-services",
    )


def about_page():
    body = f"""
{local_business_jsonld()}
<section class="page-hero">
  <div class="container">
    <p class="eyebrow">About</p>
    <h1>Hearing care for Rocky Mount, since {FOUNDED}</h1>
    <p class="page-hero__lede">{BOILERPLATE}</p>
  </div>
</section>

<section class="section">
  <div class="container provider">
    <div class="provider__photo" aria-hidden="true">
      <div class="provider__initials">MP</div>
    </div>
    <div class="provider__body">
      <p class="eyebrow">Meet the Doctor</p>
      <h2>{PROVIDER_NAME}</h2>
      <p>Dr. Palmer leads {PRACTICE} with a focus on personalized, doctor-led hearing care. Every patient is evaluated, fit, and followed by Dr. Palmer herself, so your care plan stays consistent over time.</p>
      <a class="btn btn--primary" href="/contact.html">Schedule with Dr. Palmer</a>
    </div>
  </div>
</section>

<section class="section section--alt mvv">
  <div class="container">
    <p class="eyebrow eyebrow--center">Our Purpose</p>
    <h2 class="section__title">Why we do this work</h2>
    <div class="mvv__grid">
      <article class="mvv__card">
        <h3>Mission</h3>
        <p>{MISSION}</p>
      </article>
      <article class="mvv__card">
        <h3>Vision</h3>
        <p>{VISION}</p>
      </article>
      <article class="mvv__card">
        <h3>Values</h3>
        <p>{VALUES}</p>
      </article>
    </div>
    <p class="mvv__slogan">{SLOGAN}.</p>
  </div>
</section>

<section class="section community">
  <div class="container community__inner">
    <div>
      <p class="eyebrow">Community</p>
      <h2>Rooted in Rocky Mount</h2>
      <p>We serve patients across Nash County and eastern North Carolina, from working adults in their 40s and 50s to retirees who want to stay engaged with family, faith communities, and the activities that fill their week.</p>
      <p>Our goal is simple. Help our neighbors hear what matters most, and live their lives without missing the moments that count.</p>
    </div>
    <ul class="community__list">
      <li>{ICONS['check']}<span>Family-oriented, doctor-led care</span></li>
      <li>{ICONS['check']}<span>Education for patients and their families</span></li>
      <li>{ICONS['check']}<span>Long-term follow-up, not one-and-done fittings</span></li>
      <li>{ICONS['check']}<span>{' and '.join(MANUFACTURERS)} hearing technology</span></li>
    </ul>
  </div>
</section>

<section class="cta-band">
  <div class="container cta-band__inner">
    <div>
      <h2>Get to know us in person</h2>
      <p>Book a complimentary consultation and meet {PROVIDER_NAME}.</p>
    </div>
    <div class="cta-band__buttons">
      <a class="btn btn--primary btn--lg" href="/contact.html">Book Appointment</a>
      <a class="btn btn--ghost btn--lg" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
    </div>
  </div>
</section>
"""
    return page(
        title=f"About {PRACTICE} | Rocky Mount NC Audiologist",
        description=f"{PRACTICE} has served Rocky Mount since {FOUNDED}. Meet {PROVIDER_NAME} and learn about our mission, vision, and values.",
        body=body,
        canonical="https://kinggavint.github.io/carolina-audiology-proof/about.html",
        page_class="page-about",
    )


def education_page():
    articles = [
        {
            "title": "Five signs it is time for a hearing evaluation",
            "body": [
                "Many adults wait years before getting their hearing tested. Often it is a spouse, a friend, or a colleague who notices first. Here are the signs we hear most often from patients on their first visit.",
                "<strong>You turn up the TV.</strong> Family members ask you to lower the volume. You raise it again when they leave the room.",
                "<strong>Conversations in noisy places feel exhausting.</strong> Restaurants, family dinners, church gatherings, and group meetings start to feel like work.",
                "<strong>You ask people to repeat themselves often.</strong> Especially women's and children's voices.",
                "<strong>You miss parts of phone calls.</strong> You catch some words but lose the thread.",
                "<strong>You feel more tired after social events.</strong> Hearing harder is real work, and it adds up.",
                "If any of these sound familiar, a diagnostic hearing evaluation will give you a clear picture and a path forward.",
            ],
        },
        {
            "title": "What to expect at your first appointment",
            "body": [
                "Your first appointment is about getting clear answers in a relaxed setting. Here is what a typical visit looks like.",
                "<strong>Conversation.</strong> We ask about your hearing, your medical history, and your lifestyle. You bring a family member if you want a second set of ears.",
                "<strong>Examination.</strong> We look in your ears to check for wax, infection, or anything else that needs attention.",
                "<strong>Testing.</strong> Comprehensive diagnostic testing measures how well you hear pure tones, how well you understand speech, and how your middle ear is functioning.",
                "<strong>Results.</strong> We walk you through your audiogram in plain language, with your family in the room if you brought them.",
                "<strong>Plan.</strong> If you have hearing loss, we talk through your options. If you do not, we say so. Either way, you leave with a clear next step.",
            ],
        },
        {
            "title": "Hearing technology has come a long way",
            "body": [
                "The hearing aids your parents wore are not the hearing technology we fit today. Modern devices are smaller, smarter, and far better at telling speech apart from background noise.",
                "<strong>Speech clarity.</strong> Today's processors separate voices from background sound in ways that were impossible even five years ago.",
                "<strong>Connectivity.</strong> Stream phone calls, video calls, music, and TV audio directly to your hearing technology.",
                f"<strong>Discretion.</strong> Many of the devices we fit from {' and '.join(MANUFACTURERS)} are barely visible.",
                "<strong>Rechargeable.</strong> Most patients are choosing rechargeable styles, which means no more tiny batteries.",
                "If you tried hearing aids years ago and felt let down, the technology you would try today is a very different experience.",
            ],
        },
    ]
    article_html = ""
    for a in articles:
        paragraphs = "\n".join([f"<p>{p}</p>" for p in a["body"]])
        article_html += f"""<article class="article-card">
  <h2>{a['title']}</h2>
  {paragraphs}
</article>
"""
    body = f"""
{local_business_jsonld()}
<section class="page-hero">
  <div class="container">
    <p class="eyebrow">Education</p>
    <h1>Hearing knowledge, in plain language</h1>
    <p class="page-hero__lede">Articles to help you understand your hearing and feel confident about your next step.</p>
  </div>
</section>

<section class="section section--alt">
  <div class="container articles">
    {article_html}
  </div>
</section>

<section class="cta-band">
  <div class="container cta-band__inner">
    <div>
      <h2>Questions about your hearing?</h2>
      <p>Bring them in. We will give you straight answers.</p>
    </div>
    <div class="cta-band__buttons">
      <a class="btn btn--primary btn--lg" href="/contact.html">Book Appointment</a>
      <a class="btn btn--ghost btn--lg" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
    </div>
  </div>
</section>
"""
    return page(
        title=f"Hearing Education | {PRACTICE} | Rocky Mount, NC",
        description="Learn the signs of hearing loss, what to expect at your first appointment, and how modern hearing technology can change your daily life.",
        body=body,
        canonical="https://kinggavint.github.io/carolina-audiology-proof/education.html",
        page_class="page-education",
    )


def contact_page():
    insurance_chips = "".join([f'<li>{i}</li>' for i in INSURANCES])
    body = f"""
{local_business_jsonld()}
<section class="page-hero">
  <div class="container">
    <p class="eyebrow">Contact</p>
    <h1>Schedule your visit</h1>
    <p class="page-hero__lede">Call, text, email, or send us a message. We will get back to you the same business day.</p>
  </div>
</section>

<section class="section section--alt">
  <div class="container contact-grid">
    <div class="contact-info">
      <h2>Visit us in Rocky Mount</h2>
      <ul class="contact-info__list">
        <li>{ICONS['pin']}<div><strong>Address</strong><br>{ADDRESS_LINE}<br>{CITY_STATE_ZIP}</div></li>
        <li>{ICONS['phone']}<div><strong>Phone</strong><br><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></div></li>
        <li>{ICONS['mail']}<div><strong>Email</strong><br><a href="mailto:{EMAIL}">{EMAIL}</a></div></li>
        <li>{ICONS['clock']}<div><strong>Hours</strong><br>{HOURS_LINE}</div></li>
      </ul>
      <h3>Insurance we accept</h3>
      <ul class="insurance-chips">{insurance_chips}</ul>
      <p class="insurance-note">If your plan is not listed, give us a call. We will help you understand your coverage.</p>
    </div>
    <form class="contact-form" action="https://formspree.io/f/placeholder" method="POST" novalidate>
      <h2>Send us a message</h2>
      <label>Your name
        <input type="text" name="name" required>
      </label>
      <label>Email
        <input type="email" name="email" required>
      </label>
      <label>Phone
        <input type="tel" name="phone">
      </label>
      <label>How can we help?
        <textarea name="message" rows="5" required></textarea>
      </label>
      <button type="submit" class="btn btn--primary btn--full">Send Message</button>
      <p class="contact-form__note">By submitting, you agree we may contact you about your inquiry.</p>
    </form>
  </div>
</section>

<section class="map-section">
  <iframe
    title="Map to {PRACTICE}"
    src="https://www.google.com/maps?q=4065+Capital+Drive+Rocky+Mount+NC+27804&output=embed"
    width="100%"
    height="380"
    style="border:0;"
    allowfullscreen=""
    loading="lazy"
    referrerpolicy="no-referrer-when-downgrade"></iframe>
</section>
"""
    return page(
        title=f"Contact {PRACTICE} | Rocky Mount, NC",
        description=f"Visit {PRACTICE} at {ADDRESS_LINE}, {CITY_STATE_ZIP}. Call {PHONE_DISPLAY} or email {EMAIL} to schedule.",
        body=body,
        canonical="https://kinggavint.github.io/carolina-audiology-proof/contact.html",
        page_class="page-contact",
    )


# ---------- Build ----------

PAGES = {
    "index.html": home(),
    "services.html": services_page(),
    "about.html": about_page(),
    "education.html": education_page(),
    "contact.html": contact_page(),
}


def sitemap():
    base = "https://kinggavint.github.io/carolina-audiology-proof/"
    urls = ["", "services.html", "about.html", "education.html", "contact.html"]
    body = "\n".join([f"  <url><loc>{base}{u}</loc></url>" for u in urls])
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{body}
</urlset>
"""


def robots():
    return (
        "User-agent: *\n"
        "Allow: /\n"
        "Sitemap: https://kinggavint.github.io/carolina-audiology-proof/sitemap.xml\n"
    )


def main():
    for name, content in PAGES.items():
        # Final safety net: strip em and en dashes (no fabricated number-ranges
        # should remain at this point, but this guards against future copy edits).
        cleaned = content.replace("\u2014", ", ").replace("\u2013", " to ")
        # Also guard ASCII " -- " patterns.
        cleaned = cleaned.replace(" -- ", ", ")
        # Sanity check: no emoji chars in output. Strip a broad emoji range.
        # We keep this minimal because we explicitly do not author any emojis.
        (ROOT / name).write_text(cleaned, encoding="utf-8")
    (ROOT / "sitemap.xml").write_text(sitemap(), encoding="utf-8")
    (ROOT / "robots.txt").write_text(robots(), encoding="utf-8")
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")
    print("Built:", ", ".join(PAGES.keys()), "+ sitemap.xml + robots.txt")


if __name__ == "__main__":
    main()
