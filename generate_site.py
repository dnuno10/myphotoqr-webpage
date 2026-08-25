from datetime import date
from html import escape
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE_URL = "https://www.myphotoqr.com"
TODAY = date.today().isoformat()
PRICE = "9.99"
DISPLAY_PRICE = f"${PRICE}"


EVENTS = [
    {
        "slug": "weddings",
        "label": "Weddings",
        "event_name": "wedding",
        "hero_title": "Free photo gallery for wedding guests",
        "description": "Collect wedding photos and videos in one private QR album. Guests scan a QR code, upload from their browser, and you get a live gallery, moderation controls, and a final ZIP export.",
        "hero_copy": "Capture ceremony, cocktail hour, and dance-floor moments without chasing guests later. One QR code gives everyone an easy way to share from any phone.",
        "image": "img/wedding-slideshow.webp",
        "eyebrow": "Ceremony, reception and candid moments in one place",
        "placements": "Welcome sign, reception tables, photo booth backdrop, DJ screen and post-event thank-you message.",
    },
    {
        "slug": "birthdays",
        "label": "Birthdays",
        "event_name": "birthday party",
        "hero_title": "Free photo gallery for birthday guests",
        "description": "Collect birthday party photos and videos in one private QR album. Guests scan a QR code, upload from their browser, and you keep everything organized in one gallery.",
        "hero_copy": "From candles to cake, every guest can add photos instantly. MyPhotoQR replaces scattered chats with one clean album and a simple QR flow.",
        "image": "img/feature-slideshow.webp",
        "eyebrow": "Candids, cake, family photos and party videos",
        "placements": "Gift table, welcome sign, photo wall, kids table and follow-up text after the party.",
    },
    {
        "slug": "graduations",
        "label": "Graduations",
        "event_name": "graduation party",
        "hero_title": "Free photo gallery for graduation guests",
        "description": "Collect graduation party photos and videos with a QR code guests can scan from any phone. Build one live album, protect it with optional moderation, and export the full archive later.",
        "hero_copy": "Collect cap toss photos, family snapshots and celebration videos in one place without asking guests to install an app.",
        "image": "img/grad-slideshow.webp",
        "eyebrow": "Cap toss, family portraits and celebration uploads",
        "placements": "Entrance board, party tables, graduation announcements, family group chat and slideshow screen.",
    },
    {
        "slug": "anniversaries",
        "label": "Anniversaries",
        "event_name": "anniversary celebration",
        "hero_title": "Free photo gallery for anniversary guests",
        "description": "Collect anniversary celebration photos and videos in one QR album guests can use without an app. Keep memories private, feature the best uploads, and download everything afterward.",
        "hero_copy": "Make it easy for family and friends to share toasts, throwback photos and new memories with one QR code and one private event gallery.",
        "image": "img/anniversary-slideshow.webp",
        "eyebrow": "One private album for family memories and tributes",
        "placements": "Memory table, dinner menus, anniversary slideshow and family WhatsApp message.",
    },
    {
        "slug": "corporate-events",
        "label": "Corporate Events",
        "event_name": "corporate event",
        "hero_title": "Free photo gallery for event attendees",
        "description": "Collect conference, retreat and activation photos in one branded QR album. Attendees upload from their browser while your team reviews, features and exports the best content.",
        "hero_copy": "Use one clean upload flow for staff, guests and attendees. Gather event media, social-ready moments and behind-the-scenes content in real time.",
        "image": "img/corporate-slideshow.webp",
        "eyebrow": "Activations, conferences, retreats and team events",
        "placements": "Registration desk, agenda slides, booth signage, recap email and team Slack post.",
    },
    {
        "slug": "baby-showers",
        "label": "Baby Showers",
        "event_name": "baby shower",
        "hero_title": "Free photo gallery for baby shower guests",
        "description": "Collect baby shower photos, videos and sweet messages in one private QR album. Guests upload from any browser and you keep everything organized for later.",
        "hero_copy": "Share one QR code and collect gift-table photos, family moments and messages without losing anything in text threads.",
        "image": "img/babyshower-slideshow.webp",
        "eyebrow": "A keepsake album for photos, videos and notes",
        "placements": "Gift table, dessert station, welcome sign, favor tags and thank-you follow-up.",
    },
    {
        "slug": "quinceaneras",
        "label": "Quinceañeras",
        "event_name": "quinceañera",
        "hero_title": "Free photo gallery for quinceañera guests",
        "description": "Collect quinceañera photos and videos in one private QR album. Guests scan a QR code, upload instantly, and you can show a live slideshow and export the full gallery after the event.",
        "hero_copy": "Capture dance-floor moments, family portraits and guest videos with one shareable QR code that works on any device.",
        "image": "img/15-slideshow.webp",
        "eyebrow": "Dance floor, portraits and celebration highlights",
        "placements": "Entrance display, centerpieces, DJ screen, printed programs and family social posts.",
    },
    {
        "slug": "religious-events",
        "label": "Religious Events",
        "event_name": "religious event",
        "hero_title": "Free photo gallery for family celebrations",
        "description": "Collect church and family celebration photos in one private QR album guests can access without an app. Keep the gallery simple, respectful and easy to share later.",
        "hero_copy": "For baptisms, confirmations, first communions and community celebrations, MyPhotoQR keeps every guest upload in one secure place.",
        "image": "img/religious-slideshow.webp",
        "eyebrow": "Baptisms, confirmations, communions and community events",
        "placements": "Reception hall sign, printed programs, family table, church bulletin insert and post-event message.",
    },
    {
        "slug": "farewell-parties",
        "label": "Farewell Parties",
        "event_name": "farewell party",
        "hero_title": "Free photo gallery for farewell parties",
        "description": "Collect farewell party photos, videos and messages in one QR album guests can use from any phone browser. Keep every memory together and export the full archive later.",
        "hero_copy": "Make it easy for everyone to share group photos, speeches and candid goodbye moments in one place before the night ends.",
        "image": "img/farewell-slideshow.webp",
        "eyebrow": "Photos, speeches and goodbye messages in one album",
        "placements": "Entrance sign, memory wall, group dinner tables, projector screen and post-party message.",
    },
    {
        "slug": "group-trips",
        "label": "Group Trips",
        "event_name": "group trip",
        "hero_title": "Free photo gallery for group trips",
        "description": "Collect group trip photos and videos in one QR album everyone can use without an app. Build a live shared gallery and download the full archive after the trip.",
        "hero_copy": "From airports to excursions, MyPhotoQR keeps everyone’s travel photos in one place instead of spread across dozens of chats.",
        "image": "img/trip-slideshow.webp",
        "eyebrow": "Travel photos and videos collected in one shared album",
        "placements": "Trip itinerary, welcome packet, tour bus screen, accommodation message and recap email.",
    },
]

EVENT_LOOKUP = {event["slug"]: event for event in EVENTS}

IMAGE_DIMENSIONS = {
    "img/15-slideshow.webp": (1200, 750),
    "img/anniversary-slideshow.webp": (1200, 750),
    "img/babyshower-slideshow.webp": (1200, 750),
    "img/corporate-slideshow.webp": (1200, 750),
    "img/event-collage.webp": (1100, 963),
    "img/farewell-slideshow.webp": (1200, 750),
    "img/feature-branding.webp": (1200, 750),
    "img/feature-export.webp": (1200, 750),
    "img/feature-slideshow.webp": (1200, 750),
    "img/feature-upload.webp": (1200, 750),
    "img/grad-slideshow.webp": (1200, 750),
    "img/home-phone-mockup.webp": (1200, 750),
    "img/icon-download.webp": (512, 512),
    "img/icon-event.webp": (512, 512),
    "img/icon-gallery.webp": (512, 512),
    "img/icon-moderation.webp": (512, 512),
    "img/icon-qr.webp": (512, 512),
    "img/icon-slideshow.webp": (512, 512),
    "img/icon-theme.webp": (512, 512),
    "img/icon-upload.webp": (512, 512),
    "img/logo-myphotoqr.webp": (784, 784),
    "img/og-myphotoqr.webp": (1200, 630),
    "img/religious-slideshow.webp": (1200, 750),
    "img/scanning.webp": (1200, 1200),
    "img/trip-slideshow.webp": (1200, 750),
    "img/wedding-slideshow.webp": (1200, 750),
}

EVENT_SEO = {
    "weddings": {
        "title": "Free Photo Gallery for Wedding Guests | QR Photo Sharing",
        "description": "Create a wedding photo sharing QR code so guests can upload photos and videos with no app. Collect candid guest moments, run a live gallery and download the archive.",
        "anchor": "QR photo album for weddings",
        "intent": "A wedding QR photo album works best when it is visible before the reception starts and easy to scan throughout the night.",
        "use_cases": ["Welcome signs and seating charts", "Cocktail hour and reception tables", "Photo booth backdrops and DJ screens", "Thank-you cards after the wedding"],
    },
    "birthdays": {
        "title": "Free Photo Gallery for Birthdays | QR Guest Uploads",
        "description": "Use a birthday party photo sharing QR code to collect guest photos and videos in one private album. No app required, with live gallery, moderation and ZIP export.",
        "anchor": "birthday party photo sharing QR code",
        "intent": "Birthday parties move quickly, so the QR code should be placed where guests naturally pause, gather and take photos.",
        "use_cases": ["Kids' birthday parties", "Milestone birthdays", "Surprise parties", "Backyard parties and family dinners"],
    },
    "graduations": {
        "title": "Free Photo Gallery for Graduations | QR Guest Uploads",
        "description": "Collect graduation photos and videos with one QR code guests can scan from any phone. Build a live album for ceremony moments, family photos and after-party uploads.",
        "anchor": "graduation photo sharing QR code",
        "intent": "Graduation albums need to capture formal moments, family snapshots and the casual celebration that happens afterward.",
        "use_cases": ["Graduation ceremonies", "School and campus events", "Family celebrations", "After-parties and brunches"],
    },
    "anniversaries": {
        "title": "Free Photo Gallery for Anniversaries | Collect Memories",
        "description": "Create an anniversary photo sharing QR code for family and friends. Collect photos, videos and tribute moments in one private album with no app required.",
        "anchor": "anniversary photo sharing QR code",
        "intent": "Anniversary events often mix old memories with new photos, so the album should invite guests to share both.",
        "use_cases": ["Memory tables", "Dinner menus", "Family slideshow screens", "Post-event family messages"],
    },
    "corporate-events": {
        "title": "Free Photo Gallery for Corporate Events | Attendee Uploads",
        "description": "Collect corporate event, conference and retreat photos with a branded QR upload album. Attendees upload from a browser while your team reviews and exports content.",
        "anchor": "corporate event photo sharing QR code",
        "intent": "Business events need a branded, low-friction upload flow that works for attendees, staff, partners and sponsors.",
        "use_cases": ["Conferences and expos", "Company retreats", "Brand activations", "Team-building events"],
    },
    "baby-showers": {
        "title": "Free Photo Gallery for Baby Showers | Guest Photo Uploads",
        "description": "Create a baby shower photo sharing QR code so guests can upload photos, videos and sweet messages with no app. Keep everything in one private QR album.",
        "anchor": "baby shower photo sharing QR code",
        "intent": "Baby shower albums should make it easy to collect gift moments, family photos and short messages from guests.",
        "use_cases": ["Gift tables and dessert stations", "Welcome signs", "Favor tags", "Thank-you follow-ups"],
    },
    "quinceaneras": {
        "title": "Free Photo Gallery for Quinceañeras | QR Guest Uploads",
        "description": "Collect quinceañera guest photos and videos with one QR code. Guests upload without an app, and you can show a live slideshow and download the final album.",
        "anchor": "quinceañera photo sharing QR code",
        "intent": "A quinceañera QR album should support invitations, entrance displays, table cards and live celebration moments.",
        "use_cases": ["Invitations and entrance signs", "Centerpieces and table cards", "DJ screens and live slideshows", "Family social posts after the party"],
    },
    "religious-events": {
        "title": "Free Photo Gallery for Religious Events | Private Album",
        "description": "Collect baptism, confirmation, first communion and church celebration photos in a private QR album guests can use without an app.",
        "anchor": "religious event photo sharing QR code",
        "intent": "Religious events need a respectful upload flow that keeps family memories private and easy to organize afterward.",
        "use_cases": ["Baptisms and confirmations", "First communions", "Church community events", "Family receptions"],
    },
    "farewell-parties": {
        "title": "Free Photo Gallery for Farewell Parties | Photos & Messages",
        "description": "Use a farewell party QR album to collect guest photos, videos and goodbye messages from any phone browser. Keep every memory together and export the archive.",
        "anchor": "farewell party photo sharing QR code",
        "intent": "Farewell parties benefit from prompts that invite group photos, short videos, speeches and goodbye messages.",
        "use_cases": ["Memory walls", "Group dinner tables", "Projector screens", "Post-party recap links"],
    },
    "group-trips": {
        "title": "Free Photo Gallery for Group Trips | Shared Travel Album",
        "description": "Collect group trip photos and videos with one QR code everyone can use without an app. Build a shared travel album and download the full archive.",
        "anchor": "group trip photo sharing QR code",
        "intent": "Group trips create photos across many phones, so the QR album should travel with the itinerary and recap messages.",
        "use_cases": ["Trip itineraries", "Welcome packets", "Tour bus screens", "Hotel or group chat messages"],
    },
}

FAQ_HOME = [
    (
        "What is a QR photo album?",
        "A QR photo album is a private event page where guests scan a QR code and upload photos or videos directly from their browser. It removes the need for apps, accounts or long upload instructions.",
    ),
    (
        "Do guests need to download an app?",
        "No. MyPhotoQR works in the browser on iPhone, Android, tablets and desktop. Guests scan, tap upload and share instantly.",
    ),
    (
        "Can I moderate uploads before they appear?",
        "Yes. You can enable moderation, keep content pending, auto-approve uploads, hide items or feature the best moments for your gallery and slideshow.",
    ),
    (
        "Can I download all photos after the event?",
        "Yes. You can export the album as a ZIP file to save every photo and video after the event.",
    ),
]

FAQ_HOW = [
    (
        "How long does setup take?",
        "Most hosts can create the album, personalize it and share the QR code in just a few minutes.",
    ),
    (
        "Where should I place the QR code?",
        "Use tables, welcome signs, invitations, slides, DJ screens, booths and follow-up messages so guests always have a visible way to upload.",
    ),
    (
        "Can I use the same album on phones and desktop?",
        "Yes. Album links open in mobile and desktop browsers, which makes testing and admin review simple before and during the event.",
    ),
    (
        "Can guests upload both photos and videos?",
        "Yes. Depending on your album settings, you can allow photos, videos, notes and audio memories.",
    ),
]

FAQ_FEATURES = [
    (
        "What makes MyPhotoQR better than sharing photos in group chats?",
        "Everything stays in one gallery with one link, instead of being buried across messages, apps and duplicate uploads.",
    ),
    (
        "Can I brand the album to match my event?",
        "Yes. You can customize the album name, description, event type, cover image, banner and theme colors.",
    ),
    (
        "Does MyPhotoQR support live slideshows?",
        "Yes. You can show approved uploads on a TV or projector during the event using the live gallery and slideshow view.",
    ),
]

FAQ_PRICING = [
    (
        "Is MyPhotoQR a subscription?",
        "No. The main plan is a one-time payment for one event album.",
    ),
    (
        "How long does the album stay active?",
        "The album and storage remain active for one year from the date the album is created.",
    ),
    (
        "What is included in the one-time payment?",
        "The plan includes one event album, QR sharing, guest uploads, live gallery, moderation options, slideshow support and ZIP export.",
    ),
    (
        "Can I buy the album before my event date?",
        "Yes. Many customers create and test the album in advance so the QR code is ready before guests arrive.",
    ),
]

FAQ_SUPPORT = [
    (
        "How can I contact support?",
        "You can email support@myphotoqr.com for help with album setup, QR sharing, slideshow testing and export questions.",
    ),
    (
        "What should I test before the event?",
        "Test the QR code on a phone, verify upload settings, review moderation options and confirm the slideshow works on the screen you plan to use.",
    ),
    (
        "What if guests have slow internet?",
        "Guests can retry when the connection improves. For the best experience, place the QR where mobile data or Wi-Fi signal is strong.",
    ),
]


def img(src: str, alt: str, css_class: str = "", eager: bool = False) -> str:
    attrs = [
        f'src="{escape(src)}"',
        f'alt="{escape(alt)}"',
        'decoding="async"',
    ]
    if src in IMAGE_DIMENSIONS:
        width, height = IMAGE_DIMENSIONS[src]
        attrs.append(f'width="{width}"')
        attrs.append(f'height="{height}"')
    if eager:
        attrs.append('loading="eager"')
        attrs.append('fetchpriority="high"')
    else:
        attrs.append('loading="lazy"')
    if css_class:
        attrs.append(f'class="{escape(css_class)}"')
    return f"<img {' '.join(attrs)}>"


def event_seo(event):
    return EVENT_SEO[event["slug"]]


def absolute(path: str) -> str:
    return f"{SITE_URL}/{path}" if path else f"{SITE_URL}/"


def breadcrumb_schema(trail):
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": index,
                "name": label,
                "item": url,
            }
            for index, (label, url) in enumerate(trail, start=1)
        ],
    }


def faq_schema(items):
    return {
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": question,
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": answer,
                },
            }
            for question, answer in items
        ],
    }


def site_schema():
    return [
        {
            "@type": "WebSite",
            "@id": f"{SITE_URL}/#website",
            "name": "MyPhotoQR",
            "url": f"{SITE_URL}/",
        },
        {
            "@type": "Organization",
            "@id": f"{SITE_URL}/#organization",
            "name": "MyPhotoQR",
            "url": f"{SITE_URL}/",
            "logo": {
                "@type": "ImageObject",
                "url": absolute("img/logo-myphotoqr.webp"),
            },
            "contactPoint": {
                "@type": "ContactPoint",
                "contactType": "customer support",
                "email": "support@myphotoqr.com",
                "availableLanguage": ["English"],
            },
        },
        {
            "@type": "SoftwareApplication",
            "@id": f"{SITE_URL}/#app",
            "name": "MyPhotoQR",
            "applicationCategory": "MultimediaApplication",
            "operatingSystem": "Web",
            "offers": {
                "@type": "Offer",
                "price": PRICE,
                "priceCurrency": "USD",
                "availability": "https://schema.org/InStock",
                "url": "https://app.myphotoqr.com/create",
            },
            "description": "A no-app QR album for event photo and video sharing.",
            "url": f"{SITE_URL}/",
        },
    ]


def webpage_schema(title: str, description: str, canonical: str, image_path: str, about: list[str]):
    return {
        "@type": "WebPage",
        "@id": f"{absolute(canonical)}#webpage",
        "url": absolute(canonical),
        "name": title,
        "description": description,
        "isPartOf": {"@id": f"{SITE_URL}/#website"},
        "about": [{"@type": "Thing", "name": item} for item in about],
        "primaryImageOfPage": {
            "@type": "ImageObject",
            "url": absolute(image_path),
        },
    }


def render_faq(items, title):
    blocks = []
    for question, answer in items:
        blocks.append(
            f"<details><summary>{escape(question)}</summary><p>{escape(answer)}</p></details>"
        )
    return f"""
<section class="faq section-pad" id="faq">
  <h2>{escape(title)}</h2>
  {''.join(blocks)}
</section>
"""


def render_breadcrumbs(items):
    links = []
    for index, (label, href) in enumerate(items):
        if index == len(items) - 1:
            links.append(f'<span aria-current="page">{escape(label)}</span>')
        else:
            links.append(f'<a href="{escape(href)}">{escape(label)}</a>')
    return f"""
<nav class="breadcrumbs section-pad" aria-label="Breadcrumb">
  {'<span class="breadcrumbs-sep">/</span>'.join(links)}
</nav>
"""


def head(title: str, description: str, canonical: str, image_path: str, schema_nodes: list[dict], robots: str = "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1") -> str:
    graph = {"@context": "https://schema.org", "@graph": site_schema() + schema_nodes}
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(description)}">
  <meta name="robots" content="{escape(robots)}">
  <meta name="author" content="MyPhotoQR">
  <meta name="theme-color" content="#ffffff">
  <link rel="canonical" href="{escape(absolute(canonical))}">
  <meta property="og:locale" content="en_US">
  <meta property="og:site_name" content="MyPhotoQR">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{escape(title)}">
  <meta property="og:description" content="{escape(description)}">
  <meta property="og:url" content="{escape(absolute(canonical))}">
  <meta property="og:image" content="{escape(absolute(image_path))}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{escape(title)}">
  <meta name="twitter:description" content="{escape(description)}">
  <meta name="twitter:image" content="{escape(absolute(image_path))}">
  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" type="image/png" href="/favicon-48x48.png" sizes="48x48">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png" sizes="180x180">
  <link rel="manifest" href="/manifest.webmanifest">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/styles.css">
  <script type="application/ld+json">{json.dumps(graph, ensure_ascii=False)}</script>
</head>"""


def nav():
    event_links = "".join(
        f'<a role="menuitem" href="{event["slug"]}.html">{event["label"]}</a>' for event in EVENTS
    )
    return f"""
<header class="site-header">
  <a class="brand" href="/" aria-label="MyPhotoQR home">
    {img("img/logo-myphotoqr.webp", "MyPhotoQR logo", "brand-logo", eager=True)}
    <span>MyPhotoQR</span>
  </a>
  <button class="menu-toggle" aria-label="Open menu" data-menu-toggle>☰</button>
  <nav class="nav" data-nav>
    <a href="/">Home</a>
    <a href="how-it-works.html">How it works</a>
    <a href="features.html">Features</a>
    <a href="events.html">Events</a>
    <div class="nav-dropdown" data-dropdown>
      <button class="nav-dropdown-toggle" type="button" aria-haspopup="true" aria-expanded="false" aria-controls="events-menu">
        Event Types <span aria-hidden="true">▾</span>
      </button>
      <div class="nav-dropdown-menu" id="events-menu" role="menu">
        {event_links}
      </div>
    </div>
    <a href="pricing.html">Pricing</a>
    <a href="support.html">Support</a>
  </nav>
  <a class="nav-cta" href="https://app.myphotoqr.com/create">Create album</a>
</header>
"""


def footer():
    event_links = "".join(f'<a href="{event["slug"]}.html">{event["label"]}</a>' for event in EVENTS)
    return f"""
<footer class="footer">
  <div>
    <a class="brand footer-brand" href="/" aria-label="MyPhotoQR home">
      {img("img/logo-myphotoqr.webp", "MyPhotoQR logo", "brand-logo")}
      <span>MyPhotoQR</span>
    </a>
    <p>MyPhotoQR is a no-app QR album for weddings, birthdays, graduations, corporate events and every celebration worth keeping.</p>
  </div>
  <div class="footer-links">
    <a href="events.html">All event pages</a>
    <a href="features.html">Features</a>
    <a href="pricing.html">Pricing</a>
    <a href="how-it-works.html">How it works</a>
    <a href="support.html">Support</a>
    <a href="privacy.html">Privacy</a>
    <a href="terms.html">Terms</a>
    <a href="refunds.html">Refunds</a>
  </div>
  <div class="footer-links footer-events">
    {event_links}
  </div>
  <p class="copyright">© 2026 MyPhotoQR. All rights reserved. Support: support@myphotoqr.com</p>
</footer>
"""


def page(title, description, canonical, image_path, body, schema_nodes, body_class="", robots="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"):
    return (
        head(title, description, canonical, image_path, schema_nodes, robots)
        + f"""
<body{f' class="{body_class}"' if body_class else ''}>
{nav()}
<main>{body}</main>
{footer()}
<script src="js/main.js"></script>
</body>
</html>
"""
    )


def event_cards():
    cards = []
    for event in EVENTS:
        seo = event_seo(event)
        cards.append(
            f"""
<article>
  <h3><a href="{event["slug"]}.html">{escape(seo["anchor"])}</a></h3>
  <p>{escape(seo["description"])}</p>
  <a class="text-link" href="{event["slug"]}.html">Collect {escape(event["event_name"])} photos</a>
</article>
"""
        )
    return "".join(cards)


home_body = f"""
<section class="hero section-pad">
  {img("img/feature-slideshow.webp", "Live event gallery preview", "hero-float-media hero-float-left")}
  {img("img/scanning.webp", "Guest scanning a QR code to upload event photos", "hero-float-media hero-float-right")}
  <div class="hero-copy">
    <p class="eyebrow">No app needed · Built for real events</p>
    <h1>Free Photo Gallery for Every Event Guest</h1>
    <p>Guests scan your QR code and instantly upload photos and videos to one shared album. You keep everything organized in one gallery with privacy controls, moderation and ZIP export.</p>
    <div class="hero-actions">
      <a class="btn primary" href="https://app.myphotoqr.com/create">Create your album</a>
      <a class="btn secondary" href="how-it-works.html">See how it works</a>
    </div>
    <p class="microcopy">Works on iPhone, Android, tablets and desktop. Setup takes minutes.</p>
  </div>
  <div class="hero-visual">
    {img("img/home-phone-mockup.webp", "MyPhotoQR upload flow and live gallery preview on a phone", eager=True)}
  </div>
</section>

<section class="section-pad compact center">
  <h2>Why event hosts use a QR photo album</h2>
  <p class="section-lead">MyPhotoQR replaces scattered chats, air drops and missing media with one simple upload page guests can open from any browser.</p>
  <div class="benefit-grid">
    <article><h3>One upload link for everyone</h3><p>Guests scan one QR code and upload without downloading an app or creating an account.</p></article>
    <article><h3>Private event gallery</h3><p>Keep event memories in one branded album instead of spread across messages and social apps.</p></article>
    <article><h3>Live slideshow and moderation</h3><p>Feature the best uploads live on a TV or projector while staying in control of what appears.</p></article>
    <article><h3>Final ZIP export</h3><p>Download the full archive after the event so every photo and video stays with you.</p></article>
  </div>
</section>

<section class="split section-pad alt">
  <div>
    <p class="eyebrow">What it solves</p>
    <h2>Stop losing event photos in group chats</h2>
    <p>Traditional event sharing breaks because guests use different apps, formats and chats. MyPhotoQR gives every attendee one clean place to upload from their phone while the event is happening.</p>
    <ul class="check-list compact-list">
      <li>No app install friction</li>
      <li>No searching across multiple chats</li>
      <li>No missing guest photos after the event</li>
      <li>No messy manual collection process</li>
    </ul>
  </div>
  <div class="image-board">
    {img("img/event-collage.webp", "Collage of MyPhotoQR event album use cases")}
    {img("img/feature-upload.webp", "Guest photo upload screen in the browser")}
  </div>
</section>

<section class="section-pad center" id="events">
  <p class="eyebrow">Event pages</p>
  <h2>SEO landing pages for every type of event</h2>
  <p class="section-lead">Use a dedicated page for your event type to understand the best QR album setup, the most effective placement ideas and the features that matter most.</p>
  <div class="benefit-grid link-grid">
    {event_cards()}
  </div>
</section>

<section class="flowbar section-pad">
  <div class="flowbar-track" aria-hidden="true"></div>
  <div class="flowbar-grid">
    <article><div class="flowbar-icon">{img("img/icon-gallery.webp", "Create album icon")}</div><h3>Create your album</h3><p>Name the event, add the cover, tune privacy settings and make the page match your celebration.</p></article>
    <article><div class="flowbar-icon">{img("img/icon-qr.webp", "Share QR code icon")}</div><h3>Share the QR code</h3><p>Print it on signs, tables, invitations, slides or send the link directly before and during the event.</p></article>
    <article><div class="flowbar-icon">{img("img/icon-upload.webp", "Collect uploads icon")}</div><h3>Collect memories live</h3><p>Guests upload from any browser and you can review, feature and export everything after the event.</p></article>
  </div>
</section>

<section class="section-pad center">
  <h2>What one MyPhotoQR album includes</h2>
  <div class="pill-row">
    <span>1 event album</span>
    <span>QR + link sharing</span>
    <span>Photo and video uploads</span>
    <span>Optional moderation</span>
    <span>Live gallery</span>
    <span>Slideshow support</span>
    <span>ZIP export</span>
    <span>1 year storage</span>
  </div>
</section>

{render_faq(FAQ_HOME, "MyPhotoQR QR album FAQ")}

<section class="cta-panel section-pad">
  <h2>Make photo sharing effortless from the first scan</h2>
  <p>Create one QR album and give every guest a simple path to upload photos, videos and memories while the event is still happening.</p>
  <a class="btn primary" href="https://app.myphotoqr.com/create">Buy album for {DISPLAY_PRICE}</a>
</section>
"""


def informational_page(title, description, canonical, image_path, hero_eyebrow, hero_heading, hero_copy, sections, faq_items, about, extra_schema=None):
    body = render_breadcrumbs([("Home", "/"), (hero_heading, absolute(canonical))])
    body += f"""
<section class="page-hero section-pad center">
  <p class="eyebrow">{escape(hero_eyebrow)}</p>
  <h1>{escape(hero_heading)}</h1>
  <p>{escape(hero_copy)}</p>
</section>
"""
    body += "".join(sections)
    body += render_faq(faq_items, f"{hero_heading} FAQ")
    body += """
<section class="cta-panel section-pad">
  <h2>Ready to create your album?</h2>
  <p>Build your event album before guests arrive so the QR code, upload page and slideshow are all ready to go.</p>
  <a class="btn primary" href="https://app.myphotoqr.com/create">Create album</a>
</section>
"""
    schema = [
        webpage_schema(title, description, canonical, image_path, about),
        breadcrumb_schema([("Home", f"{SITE_URL}/"), (hero_heading, absolute(canonical))]),
        faq_schema(faq_items),
    ]
    if extra_schema:
        schema.extend(extra_schema)
    return page(title, description, canonical, image_path, body, schema)


how_sections = [
    """
<section class="flowbar section-pad">
  <div class="flowbar-track" aria-hidden="true"></div>
  <div class="flowbar-grid">
    <article><div class="flowbar-icon">"""
    + img("img/icon-gallery.webp", "Create album icon")
    + """</div><h3>Create</h3><p>Start your album, choose the event type and prepare the page guests will open.</p></article>
    <article><div class="flowbar-icon">"""
    + img("img/icon-qr.webp", "Share QR icon")
    + """</div><h3>Share</h3><p>Print the QR or send the link before the event so guests can access the album instantly.</p></article>
    <article><div class="flowbar-icon">"""
    + img("img/icon-upload.webp", "Upload icon")
    + """</div><h3>Collect</h3><p>Watch guest uploads arrive live and export everything once the event is over.</p></article>
  </div>
</section>
""",
    """
<section class="timeline section-pad">
  <article><h2>Create the album</h2><p>Add the event name, date, location, message, cover image and theme colors.</p></article>
  <article><h2>Set privacy rules</h2><p>Enable moderation, access protection and upload preferences before the event starts.</p></article>
  <article><h2>Place the QR well</h2><p>Use visible signage, printed materials and digital reminders so guests always know where to upload.</p></article>
  <article><h2>Collect guest media</h2><p>Guests upload photos, videos, audio memories and notes from any compatible browser.</p></article>
  <article><h2>Feature the best moments</h2><p>Run a live gallery or slideshow using approved uploads for screens, TVs and projectors.</p></article>
  <article><h2>Export after the event</h2><p>Download a ZIP archive and keep every memory in one organized backup.</p></article>
</section>
""",
    """
<section class="split section-pad alt">
  <div>
    <p class="eyebrow">Best practices</p>
    <h2>How to get more guest uploads</h2>
    <p>Hosts get the best results when the QR code is visible more than once, the upload page is tested before the event and guests are reminded to use it while the energy is high.</p>
  </div>
  <div class="support-grid single-grid">
    <article><h3>Place the QR early</h3><p>Start at the entrance or welcome area so guests see it before they settle in.</p></article>
    <article><h3>Repeat the placement</h3><p>Use tables, screens and printed signs to keep the upload path visible throughout the event.</p></article>
    <article><h3>Prompt during key moments</h3><p>Ask the DJ, MC or host to remind guests to upload during speeches, dances or group photos.</p></article>
  </div>
</section>
""",
    """
<section class="section-pad center">
  <p class="eyebrow">Event timeline</p>
  <h2>What to do before, during and after the event</h2>
  <p class="section-lead">A QR photo album works best when the upload flow is prepared early, visible during the event and exported soon after guests finish sharing.</p>
  <div class="benefit-grid">
    <article><h3>Before the event</h3><p>Create the album, test the QR code on a phone, choose moderation settings and place the QR on signs, invitations or table cards.</p></article>
    <article><h3>During the event</h3><p>Keep the QR visible, remind guests during high-energy moments and use the live gallery or slideshow for approved uploads.</p></article>
    <article><h3>After the event</h3><p>Review the final gallery, hide anything you do not want to keep public and download the complete ZIP archive.</p></article>
    <article><h3>For guests</h3><p>Guests scan, tap upload and add photos or videos directly from their browser without installing an app or creating an account.</p></article>
  </div>
</section>
""",
]

features_sections = [
    """
<section class="feature-list section-pad">
  <article>"""
    + img("img/feature-branding.webp", "Album branding customization")
    + """<div><h2>Branded event album</h2><p>Customize the album name, event type, description, date, location, cover image, banner and color theme so the page feels specific to the event.</p></div></article>
  <article>"""
    + img("img/feature-upload.webp", "Browser-based guest upload page")
    + """<div><h2>Guest uploads without an app</h2><p>Guests upload from a browser on iPhone, Android, tablets or desktop. That removes app-store friction and improves participation.</p></div></article>
  <article>"""
    + img("img/feature-slideshow.webp", "Live slideshow with guest media")
    + """<div><h2>Live gallery and slideshow</h2><p>Turn guest media into a live visual wall on a TV or projector. Use approved or featured uploads to keep the presentation polished.</p></div></article>
  <article>"""
    + img("img/feature-export.webp", "ZIP export of event photos")
    + """<div><h2>ZIP export and long-term backup</h2><p>Download the full event archive after the celebration so you keep every photo and video outside the platform too.</p></div></article>
</section>
""",
    f"""
<section class="section-pad center alt">
  <p class="eyebrow">Event coverage</p>
  <h2>Built for many types of events</h2>
  <p class="section-lead">MyPhotoQR works across personal celebrations, group travel and business events, with landing pages tuned for each intent.</p>
  <div class="use-grid">
    {''.join(f'<span>{event["label"]}</span>' for event in EVENTS)}
  </div>
</section>
""",
]

pricing_sections = [
    f"""
<section class="pricing-wrap section-pad">
  <article class="price-card">
    <p class="eyebrow">One-time payment</p>
    <h2>{DISPLAY_PRICE}</h2>
    <p class="price-note">One QR album for one event, with admin controls and one year of storage.</p>
    <a class="btn primary full" href="https://app.myphotoqr.com/create">Buy album</a>
    <ul class="check-list">
      <li>1 event album</li>
      <li>QR code and guest share link</li>
      <li>Photo and video uploads from any browser</li>
      <li>Optional notes and audio memories</li>
      <li>Live gallery and slideshow</li>
      <li>Privacy and moderation controls</li>
      <li>ZIP export</li>
      <li>1 year active album and storage</li>
    </ul>
  </article>
  <aside class="include-panel">
    <h2>What happens after payment?</h2>
    <p>After checkout, you create the album, personalize the event page, test the QR code and start sharing with guests before the event begins.</p>
    <div class="mini-steps">
      <span>1. Buy the album</span>
      <span>2. Personalize the page</span>
      <span>3. Share the QR code</span>
      <span>4. Collect guest uploads</span>
      <span>5. Export the archive</span>
    </div>
  </aside>
</section>
""",
    """
<section class="split section-pad alt">
  <div>
    <p class="eyebrow">Purchase intent</p>
    <h2>Simple pricing built for one event</h2>
    <p>MyPhotoQR is designed for hosts who need one reliable photo-sharing workflow without a subscription, complicated setup or hidden steps before the event.</p>
  </div>
  <div class="support-grid single-grid">
    <article><h3>Buy once</h3><p>One payment covers one event album instead of recurring monthly billing.</p></article>
    <article><h3>Prepare in advance</h3><p>Create and test everything before the event so guests only see a simple QR flow.</p></article>
    <article><h3>Keep the archive</h3><p>Download the full ZIP later so your media lives beyond the event itself.</p></article>
  </div>
</section>
""",
]

support_sections = [
    """
<section class="support-grid section-pad">
  <article><h2>Contact support</h2><p>Email <a href="mailto:support@myphotoqr.com">support@myphotoqr.com</a> for help with setup, QR placement ideas, uploads, slideshow preparation and exports.</p></article>
  <article><h2>Before your event</h2><p>Test the QR code on a phone, review upload permissions and confirm the gallery or slideshow works on the screen you plan to use.</p></article>
  <article><h2>During your event</h2><p>Use visible QR signage, repeat the link in messages and keep one person ready to monitor uploads if you want moderation turned on.</p></article>
</section>
""",
    """
<section class="split section-pad alt">
  <div>
    <p class="eyebrow">Support topics</p>
    <h2>Common setup issues to avoid</h2>
    <p>Most event-day issues come from weak QR placement, untested links or last-minute slideshow setup. A quick pre-event check removes most of that risk.</p>
  </div>
  <div class="support-grid single-grid">
    <article><h3>QR too small</h3><p>Use signage large enough for guests to scan from a comfortable distance.</p></article>
    <article><h3>No reminder to guests</h3><p>Prompt uploads during key moments so participation stays high.</p></article>
    <article><h3>No export plan</h3><p>Download the ZIP after the event so your final archive is backed up outside the app.</p></article>
  </div>
</section>
""",
]

events_hub_sections = [
    """
<section class="section-pad center">
  <p class="eyebrow">Topic cluster</p>
  <h2>Choose the right QR album page for your event</h2>
  <p class="section-lead">Each event page targets a different intent, use case and guest flow so search engines and visitors both understand how MyPhotoQR fits the event.</p>
  <div class="benefit-grid link-grid">
"""
    + event_cards()
    + """
  </div>
</section>
""",
    """
<section class="split section-pad alt">
  <div>
    <p class="eyebrow">Why this helps SEO</p>
    <h2>More specific pages rank better than one generic event page</h2>
    <p>Dedicated pages for weddings, birthdays, graduations and corporate events create stronger topical relevance, clearer internal linking and better matching for search intent.</p>
  </div>
  <div class="support-grid single-grid">
    <article><h3>Specific keyword match</h3><p>Each page can target event-specific searches like wedding QR photo sharing or graduation upload link.</p></article>
    <article><h3>Better internal architecture</h3><p>The hub strengthens crawl paths between the homepage, feature pages and deeper event-specific content.</p></article>
    <article><h3>Stronger structured data</h3><p>Breadcrumbs, FAQ schema and event-focused page copy help clarify topical intent for each landing page.</p></article>
  </div>
</section>
""",
]


def event_page(event):
    seo = event_seo(event)
    title = seo["title"]
    description = seo["description"]
    canonical = f'{event["slug"]}.html'
    trail = [
        ("Home", f"{SITE_URL}/"),
        ("Events", f"{SITE_URL}/events.html"),
        (event["label"], absolute(canonical)),
    ]
    faq_items = [
        (
            f'Do guests need an app to upload {event["event_name"]} photos?',
            "No. Guests scan your QR code and upload from their browser on iPhone, Android, tablet or desktop.",
        ),
        (
            "Can I review uploads before they appear in the gallery?",
            "Yes. You can turn moderation on, keep uploads pending, hide content or feature the best moments.",
        ),
        (
            "Can I download everything after the event?",
            "Yes. You can export a ZIP file with your event photos and videos after the celebration.",
        ),
    ]
    related = [other for other in EVENTS if other["slug"] != event["slug"]][:4]
    related_cards = "".join(
        f'<article><h3><a href="{other["slug"]}.html">{escape(event_seo(other)["anchor"])}</a></h3><p>{escape(event_seo(other)["description"])}</p></article>'
        for other in related
    )
    use_case_items = "".join(f"<li>{escape(item)}</li>" for item in seo["use_cases"])
    body = render_breadcrumbs([("Home", "/"), ("Events", "events.html"), (event["label"], absolute(canonical))])
    body += f"""
<section class="page-hero section-pad center">
  <p class="eyebrow">Events · {escape(event["label"])}</p>
  <h1>{escape(event["hero_title"])}</h1>
  <p>{escape(event["hero_copy"])}</p>
  <div class="hero-actions">
    <a class="btn primary" href="https://app.myphotoqr.com/create">Buy album for {DISPLAY_PRICE}</a>
    <a class="btn secondary" href="how-it-works.html">See how it works</a>
  </div>
  <p class="microcopy">{escape(event["eyebrow"])}</p>
  <div class="hero-visual event-hero-visual">
    {img(event["image"], f'{event["label"]} QR album preview', eager=True)}
  </div>
</section>

<section class="section-pad compact center">
  <h2>Why MyPhotoQR works well for {escape(event["label"].lower())}</h2>
  <p class="section-lead">{escape(seo["intent"])}</p>
  <div class="benefit-grid">
    <article><h3>Simple guest experience</h3><p>Scan the QR, open the browser, upload. No app store or account creation slows guests down.</p></article>
    <article><h3>Better media collection</h3><p>Capture candid angles, guest perspectives and spontaneous moments you would never receive later.</p></article>
    <article><h3>Optional moderation</h3><p>Review content before it reaches the live gallery or slideshow when you want tighter control.</p></article>
    <article><h3>Complete archive</h3><p>Keep one private album during the event and one ZIP archive after the event.</p></article>
  </div>
</section>

<section class="split section-pad">
  <div>
    <p class="eyebrow">Use cases</p>
    <h2>Best ways to use a {escape(seo["anchor"])}</h2>
    <p>Make the upload path match the actual flow of the event. The more naturally guests see the QR code, the more complete your final album becomes.</p>
  </div>
  <div class="include-panel">
    <h3>Recommended placements and moments</h3>
    <ul class="check-list compact-list">
      {use_case_items}
    </ul>
  </div>
</section>

<section class="split section-pad alt">
  <div>
    <p class="eyebrow">Best placement ideas</p>
    <h2>Where to put the QR code for higher participation</h2>
    <p>{escape(event["placements"])}</p>
    <a class="text-link" href="features.html">Explore QR album features</a>
  </div>
  <div class="usecase-steps">
    <div class="usecase-step">
      {img("img/scanning.webp", "Guest scanning the QR code")}
      <p><strong>Step 1:</strong> Guests scan the QR code from a sign, table card or screen.</p>
    </div>
    <div class="usecase-step">
      {img("img/feature-upload.webp", "Guest uploading event media from the browser")}
      <p><strong>Step 2:</strong> They upload photos or videos directly from their phone browser.</p>
    </div>
    <div class="usecase-step">
      {img("img/feature-slideshow.webp", "Event slideshow fed by guest uploads")}
      <p><strong>Step 3:</strong> You review, feature or display the best moments in the live gallery and slideshow.</p>
    </div>
  </div>
</section>

<section class="split section-pad">
  <div>
    <h2>What hosts usually want from a {escape(event["event_name"])} album</h2>
    <p>They want a fast setup, high guest participation, privacy controls during the event and a reliable way to keep the full archive after the event ends.</p>
    <ul class="check-list compact-list">
      <li>One QR code guests can use instantly</li>
      <li>One upload page that works on any phone</li>
      <li>One private gallery with moderation controls</li>
      <li>One ZIP export for long-term storage</li>
    </ul>
  </div>
  <div class="include-panel">
    <h3>Included with every album</h3>
    <div class="mini-steps">
      <span>QR sharing</span>
      <span>Live gallery</span>
      <span>Slideshow support</span>
      <span>Moderation controls</span>
      <span>ZIP export</span>
    </div>
  </div>
</section>

{render_faq(faq_items, f'{event["label"]} QR album FAQ')}

<section class="section-pad center">
  <p class="eyebrow">Related pages</p>
  <h2>Explore other event photo sharing pages</h2>
  <div class="benefit-grid link-grid">
    {related_cards}
  </div>
</section>

<section class="cta-panel section-pad">
  <h2>Ready to collect {escape(event["event_name"])} memories?</h2>
  <p>Create the QR album before the event so guests have a simple, visible way to upload from the first minute.</p>
  <a class="btn primary" href="https://app.myphotoqr.com/create">Create album</a>
</section>
"""
    schema = [
        webpage_schema(title, description, canonical, event["image"], [event["label"], f'{event["label"]} photo sharing', "QR photo sharing code", "QR album"]),
        breadcrumb_schema(trail),
        faq_schema(faq_items),
    ]
    return page(title, description, canonical, event["image"], body, schema, body_class="events-page")


home = page(
    "Free Photo Gallery for Events | MyPhotoQR QR Album",
    "Create a QR album for your event. Guests scan a QR code, upload photos and videos from their browser, enjoy a live gallery, and download everything after the event.",
    "",
    "img/og-myphotoqr.webp",
    home_body,
    [
        webpage_schema(
            "Free Photo Gallery for Events | MyPhotoQR QR Album",
            "Create a QR album for your event. Guests scan a QR code, upload photos and videos from their browser, enjoy a live gallery, and download everything after the event.",
            "",
            "img/og-myphotoqr.webp",
            ["QR album", "Event photo sharing", "Guest photo upload"],
        ),
        {
            "@type": "ItemList",
            "name": "Event QR album landing pages",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": index,
                    "url": absolute(f'{event["slug"]}.html'),
                    "name": event["label"],
                }
                for index, event in enumerate(EVENTS, start=1)
            ],
        },
        faq_schema(FAQ_HOME),
    ],
)

how = informational_page(
    "Free Photo Gallery Setup | Create, Share and Collect Photos",
    "Learn how to create a QR album, personalize it, share QR links with guests, collect photos and videos in real time, and export your event memories.",
    "how-it-works.html",
    "img/feature-upload.webp",
    "Simple from the first scan",
    "Free photo gallery setup",
    "Create the album, share the QR code, collect guest uploads in real time and export the full archive after the event.",
    how_sections,
    FAQ_HOW,
    ["How QR photo sharing works", "Guest uploads", "Event gallery workflow"],
)

features = informational_page(
    "Free Photo Gallery Features | QR Uploads, Slideshow and Export",
    "Explore MyPhotoQR features: custom QR album, guest photo and video uploads, live slideshow, privacy code, moderation, branding and ZIP export.",
    "features.html",
    "img/feature-slideshow.webp",
    "Made for event memories",
    "Free photo gallery features for events",
    "Everything you need to collect, organize, moderate, display and keep the best content from your event.",
    features_sections,
    FAQ_FEATURES,
    ["QR event album features", "Live gallery", "Event slideshow", "ZIP export"],
)

pricing = informational_page(
    f"Free Guest Photo Gallery | {DISPLAY_PRICE} Host QR Album",
    f"Create a QR photo album for one event for {DISPLAY_PRICE}. Guests upload photos and videos with no app, and you can download everything after the event.",
    "pricing.html",
    "img/feature-export.webp",
    "One event. One payment.",
    "Simple $9.99 pricing for your QR gallery",
    "No monthly subscription. Buy one event album, share your QR code and collect guest media without ongoing fees.",
    pricing_sections,
    FAQ_PRICING,
    ["MyPhotoQR pricing", "One-time event album", "QR photo sharing cost"],
    extra_schema=[
        {
            "@type": "Product",
            "@id": f"{SITE_URL}/pricing.html#product",
            "name": "MyPhotoQR QR Photo Album",
            "description": "A one-time QR photo album for event guest photo and video uploads.",
            "brand": {
                "@type": "Brand",
                "name": "MyPhotoQR",
            },
            "image": absolute("img/feature-export.webp"),
            "offers": {
                "@type": "Offer",
                "price": PRICE,
                "priceCurrency": "USD",
                "availability": "https://schema.org/InStock",
                "url": f"{SITE_URL}/pricing.html",
            },
        }
    ],
)

support = informational_page(
    "Free Photo Gallery Support | QR Albums and Guest Uploads",
    "Get help with QR albums, guest uploads, live gallery, moderation, slideshow, download export, privacy settings and event setup.",
    "support.html",
    "img/scanning.webp",
    "Help when you need it",
    "Free photo gallery support",
    "Questions about QR sharing, guest uploads, moderation, slideshow setup or final exports? This page covers the most common support topics.",
    support_sections,
    FAQ_SUPPORT,
    ["QR album support", "Event gallery help", "Guest upload troubleshooting"],
)

events_hub = informational_page(
    "Free Photo Gallery Ideas | Weddings, Parties and Trips",
    "Explore QR album pages for weddings, birthdays, graduations, corporate events, quinceañeras, baby showers, group trips and more.",
    "events.html",
    "img/event-collage.webp",
    "Use cases and landing pages",
    "Free photo gallery ideas for every event",
    "Each event page explains how MyPhotoQR fits a specific celebration or gathering, with setup ideas, placement tips and answers to common questions.",
    events_hub_sections,
    [
        (
            "Why does MyPhotoQR have separate pages for different event types?",
            "Because guests, hosts and searchers often have different needs depending on the event. Separate pages let us explain those differences clearly.",
        ),
        (
            "Can the same MyPhotoQR product work for all these event types?",
            "Yes. The same core product works across many event types, but the best setup and messaging can vary based on the occasion.",
        ),
    ],
    ["Event QR album use cases", "Wedding photo sharing", "Corporate event photo sharing"],
)


INTENT_PAGES = [
    {
        "slug": "wedding-photo-sharing-qr-code",
        "title": "Free Wedding Photo Gallery | No-App Guest Uploads",
        "description": "Create a wedding photo sharing QR code so guests can upload photos and videos from any phone browser. Collect candid guest photos in one private album.",
        "heading": "Free wedding photo gallery for guest uploads",
        "eyebrow": "Wedding QR photo sharing",
        "copy": "Use one QR code at the ceremony, reception and after-party so guests can upload wedding photos without downloading an app.",
        "image": "img/wedding-slideshow.webp",
        "problem": "Wedding photos often stay trapped in guest phones, group chats and social apps. A dedicated QR upload page gives everyone one clear place to share.",
        "best_for": ["Welcome signs near the ceremony entrance", "Reception table cards and bar signs", "Photo booth backdrops", "Post-wedding thank-you messages"],
        "links": [("QR photo album for weddings", "weddings.html"), ("QR photo album pricing", "pricing.html"), ("How QR photo sharing works", "how-it-works.html")],
    },
    {
        "slug": "qr-code-for-wedding-photos",
        "title": "Free Photo Gallery QR Code | Collect Wedding Photos",
        "description": "Make a QR code for wedding photos and let guests upload from their phone browser. Build one live wedding album with moderation and ZIP export.",
        "heading": "Free photo gallery QR code for wedding photos",
        "eyebrow": "Collect wedding guest photos",
        "copy": "Give guests a simple scan-to-upload path for ceremony moments, reception candids, dance-floor videos and family photos.",
        "image": "img/wedding-slideshow.webp",
        "problem": "The best wedding photos are often taken by guests, but asking for them later is slow and incomplete. The QR code keeps collection active while the event is happening.",
        "best_for": ["Ceremony programs", "Seating charts", "Cocktail napkin signs", "DJ screen reminders"],
        "links": [("Wedding photo sharing QR code", "wedding-photo-sharing-qr-code.html"), ("Wedding QR album page", "weddings.html"), ("Event photo sharing features", "features.html")],
    },
    {
        "slug": "collect-wedding-guest-photos",
        "title": "Free Photo Gallery for Wedding Guests | No-App QR Album",
        "description": "Collect wedding guest photos with one QR upload album. Guests scan, upload from the browser and help you build a complete wedding gallery.",
        "heading": "Free photo gallery for wedding guest photos",
        "eyebrow": "No app for guests",
        "copy": "Make it easy for guests to contribute candid photos and short videos before memories get lost in private messages.",
        "image": "img/event-collage.webp",
        "problem": "After the wedding, hosts usually have to chase guests across texts, AirDrop, email and social apps. MyPhotoQR turns that into one album link.",
        "best_for": ["Candid table photos", "Guest selfies", "Dance-floor videos", "Family group shots"],
        "links": [("QR code for wedding photos", "qr-code-for-wedding-photos.html"), ("Wedding QR album", "weddings.html"), ("Buy one QR album", "pricing.html")],
    },
    {
        "slug": "event-photo-sharing-qr-code",
        "title": "Free Event Photo Gallery QR Code | Collect Photos & Videos",
        "description": "Create an event photo sharing QR code for weddings, parties, graduations, corporate events and trips. Guests upload with no app and you export the archive.",
        "heading": "Free event photo gallery QR code for any gathering",
        "eyebrow": "One upload link for guests",
        "copy": "Use one QR code to collect event photos and videos from guests, attendees, family, friends or coworkers.",
        "image": "img/event-collage.webp",
        "problem": "Most events generate photos across dozens of phones. A QR photo album creates one shared upload destination and one clean archive.",
        "best_for": ["Weddings and birthdays", "Graduations and baby showers", "Corporate events and activations", "Group trips and family gatherings"],
        "links": [("All QR album event pages", "events.html"), ("No-app event photo sharing", "no-app-photo-sharing-for-events.html"), ("QR upload for events", "qr-photo-upload-for-events.html")],
    },
    {
        "slug": "no-app-photo-sharing-for-events",
        "title": "Free Photo Gallery for Events | Browser QR Uploads",
        "description": "Let guests share event photos without downloading an app. MyPhotoQR uses one QR code and a browser upload page for photos, videos and memories.",
        "heading": "Free no-app photo gallery for events",
        "eyebrow": "Browser-based uploads",
        "copy": "Guests scan a QR code, open the upload page and add photos or videos from the browser on iPhone, Android, tablet or desktop.",
        "image": "img/feature-upload.webp",
        "problem": "App downloads reduce participation because guests do not want accounts, permissions or setup steps during an event.",
        "best_for": ["Mixed-age guest lists", "Venues with limited time for instructions", "Events where people use different devices", "Hosts who want fewer support questions"],
        "links": [("How MyPhotoQR works", "how-it-works.html"), ("Event photo sharing QR code", "event-photo-sharing-qr-code.html"), ("QR album features", "features.html")],
    },
    {
        "slug": "qr-photo-upload-for-events",
        "title": "Free Photo Gallery Uploads | Guests Add Photos by QR",
        "description": "Set up QR photo upload for events so guests can scan, upload and contribute photos or videos to one private event gallery.",
        "heading": "Free QR photo uploads for events",
        "eyebrow": "Scan, upload, collect",
        "copy": "Turn signs, table cards, slides and messages into upload prompts that feed one private event gallery.",
        "image": "img/scanning.webp",
        "problem": "Guests will share more when the upload path is visible, fast and repeated at the right moments.",
        "best_for": ["Entrance signs", "Table cards", "Projection screens", "Follow-up texts and emails"],
        "links": [("Event photo sharing QR code", "event-photo-sharing-qr-code.html"), ("No-app photo sharing", "no-app-photo-sharing-for-events.html"), ("Simple pricing", "pricing.html")],
    },
    {
        "slug": "live-event-photo-slideshow",
        "title": "Free Photo Gallery Slideshow | Show Guest QR Uploads",
        "description": "Create a live event photo slideshow from guest uploads. Use MyPhotoQR to collect photos by QR code, moderate uploads and display approved moments.",
        "heading": "Free photo gallery slideshow from guest uploads",
        "eyebrow": "Gallery and slideshow",
        "copy": "Collect photos by QR code and turn approved guest uploads into a live gallery or slideshow for a TV, projector or venue screen.",
        "image": "img/feature-slideshow.webp",
        "problem": "A live slideshow is strongest when uploads are easy for guests and the host can control what appears on screen.",
        "best_for": ["Wedding receptions", "Graduation parties", "Corporate event screens", "Birthday and anniversary celebrations"],
        "links": [("QR album features", "features.html"), ("Event photo sharing QR code", "event-photo-sharing-qr-code.html"), ("How the upload flow works", "how-it-works.html")],
    },
]


def intent_landing_cards():
    return "".join(
        f"""
<article>
  <h3><a href="{page_data["slug"]}.html">{escape(page_data["heading"])}</a></h3>
  <p>{escape(page_data["description"])}</p>
  <a class="text-link" href="{page_data["slug"]}.html">Read the guide</a>
</article>
"""
        for page_data in INTENT_PAGES
    )


def intent_page(page_data):
    best_for = "".join(f"<li>{escape(item)}</li>" for item in page_data["best_for"])
    related = "".join(
        f'<a href="{escape(href)}">{escape(label)}</a>' for label, href in page_data["links"]
    )
    faq_items = [
        (
            f'Can guests use this {page_data["heading"].lower()} without an app?',
            "Yes. Guests scan the QR code and upload from a browser on iPhone, Android, tablet or desktop.",
        ),
        (
            "Can the host review uploads?",
            "Yes. MyPhotoQR supports moderation so hosts can review, hide or feature uploads before using the gallery or slideshow.",
        ),
        (
            "Can I download the photos after the event?",
            "Yes. The album can be exported as a ZIP archive after the event.",
        ),
    ]
    body = render_breadcrumbs([("Home", "/"), ("Guides", "events.html"), (page_data["heading"], f'{page_data["slug"]}.html')])
    body += f"""
<section class="page-hero section-pad center">
  <p class="eyebrow">{escape(page_data["eyebrow"])}</p>
  <h1>{escape(page_data["heading"])}</h1>
  <p>{escape(page_data["copy"])}</p>
  <div class="hero-actions">
    <a class="btn primary" href="https://app.myphotoqr.com/create">Create album</a>
    <a class="btn secondary" href="pricing.html">See pricing</a>
  </div>
  <div class="hero-visual event-hero-visual">
    {img(page_data["image"], page_data["heading"], eager=True)}
  </div>
</section>

<section class="split section-pad">
  <div>
    <p class="eyebrow">Search intent</p>
    <h2>Why this QR album page exists</h2>
    <p>{escape(page_data["problem"])}</p>
  </div>
  <div class="include-panel">
    <h3>Best places to use it</h3>
    <ul class="check-list compact-list">
      {best_for}
    </ul>
  </div>
</section>

<section class="section-pad center alt">
  <p class="eyebrow">Workflow</p>
  <h2>From QR scan to final archive</h2>
  <div class="benefit-grid">
    <article><h3>Create</h3><p>Set up one event album and personalize the upload page before guests arrive.</p></article>
    <article><h3>Share</h3><p>Place the QR code on signs, tables, screens, invitations or messages.</p></article>
    <article><h3>Collect</h3><p>Guests upload photos and videos from their browser while the event is happening.</p></article>
    <article><h3>Export</h3><p>Review the gallery, use the slideshow and download the full ZIP archive afterward.</p></article>
  </div>
</section>

<section class="section-pad center">
  <p class="eyebrow">Internal links</p>
  <h2>Related MyPhotoQR pages</h2>
  <div class="footer-links intent-links">
    {related}
  </div>
</section>

{render_faq(faq_items, f'{page_data["heading"]} FAQ')}

<section class="cta-panel section-pad">
  <h2>Create one QR album before the event starts</h2>
  <p>Give every guest one simple upload path and keep the final gallery organized from the first scan.</p>
  <a class="btn primary" href="https://app.myphotoqr.com/create">Buy album for {DISPLAY_PRICE}</a>
</section>
"""
    schema = [
        webpage_schema(page_data["title"], page_data["description"], f'{page_data["slug"]}.html', page_data["image"], [page_data["heading"], "Event photo sharing", "QR photo upload"]),
        breadcrumb_schema([("Home", f"{SITE_URL}/"), ("Guides", f"{SITE_URL}/events.html"), (page_data["heading"], absolute(f'{page_data["slug"]}.html'))]),
        faq_schema(faq_items),
    ]
    return page(page_data["title"], page_data["description"], f'{page_data["slug"]}.html', page_data["image"], body, schema)


events_hub_sections.append(
    f"""
<section class="section-pad center">
  <p class="eyebrow">Search guides</p>
  <h2>Pages built around high-intent searches</h2>
  <p class="section-lead">These focused guides answer the exact questions people search before choosing a QR photo album for an event.</p>
  <div class="benefit-grid link-grid">
    {intent_landing_cards()}
  </div>
</section>
"""
)

events_hub = informational_page(
    "Free Photo Gallery Ideas | Weddings, Parties and Trips",
    "Explore QR album pages for weddings, birthdays, graduations, corporate events, quinceañeras, baby showers, group trips and more.",
    "events.html",
    "img/event-collage.webp",
    "Use cases and landing pages",
    "Free photo gallery ideas for every event",
    "Each event page explains how MyPhotoQR fits a specific celebration or gathering, with setup ideas, placement tips and answers to common questions.",
    events_hub_sections,
    [
        (
            "Why does MyPhotoQR have separate pages for different event types?",
            "Because guests, hosts and searchers often have different needs depending on the event. Separate pages let us explain those differences clearly.",
        ),
        (
            "Can the same MyPhotoQR product work for all these event types?",
            "Yes. The same core product works across many event types, but the best setup and messaging can vary based on the occasion.",
        ),
    ],
    ["Event QR album use cases", "Wedding photo sharing", "Corporate event photo sharing"],
)


def legal_page(title, description, canonical, body_copy):
    breadcrumb = render_breadcrumbs([("Home", "/"), (title.split("|")[0].strip(), absolute(canonical))])
    body = (
        breadcrumb
        + f"""
<section class="legal section-pad">
  <h1>{escape(title.split('|')[0].strip())}</h1>
  {body_copy}
</section>
"""
    )
    schema = [
        webpage_schema(title, description, canonical, "img/og-myphotoqr.webp", [title.split("|")[0].strip(), "MyPhotoQR policies"]),
        breadcrumb_schema([("Home", f"{SITE_URL}/"), (title.split("|")[0].strip(), absolute(canonical))]),
    ]
    return page(title, description, canonical, "img/og-myphotoqr.webp", body, schema, robots="noindex, follow")


privacy = legal_page(
    "Privacy Policy | MyPhotoQR",
    "Privacy information for MyPhotoQR event album users and guests.",
    "privacy.html",
    """
<p>MyPhotoQR is designed to collect event memories through QR links and browser uploads. Album owners control visibility, sharing and moderation settings.</p>
<p>We collect the account, album and upload information required to operate the service. Uploaded content can include photos, videos, notes and audio memories shared by guests.</p>
<p>For privacy questions, contact <a href="mailto:support@myphotoqr.com">support@myphotoqr.com</a>.</p>
""",
)

terms = legal_page(
    "Terms of Service | MyPhotoQR",
    "Terms for using MyPhotoQR QR albums, guest uploads, live gallery and event sharing tools.",
    "terms.html",
    """
<p>By using MyPhotoQR, you agree to use the service lawfully and only upload content you have permission to share. Album owners are responsible for managing guest access and content moderation.</p>
<p>The one-time event album plan includes the features shown on the pricing page, subject to reasonable technical limits and acceptable use.</p>
<p>For questions about these terms, contact <a href="mailto:support@myphotoqr.com">support@myphotoqr.com</a>.</p>
""",
)

refunds = legal_page(
    "Refund Policy | MyPhotoQR",
    "Refund information for MyPhotoQR one-time QR album purchases.",
    "refunds.html",
    """
<p>Because MyPhotoQR provides digital event album access, refund eligibility can depend on whether the album has been created, shared or used to receive uploads.</p>
<p>Contact <a href="mailto:support@myphotoqr.com">support@myphotoqr.com</a> with your purchase email and event details. Refund requests are reviewed case by case.</p>
""",
)


FILES = {
    "index.html": home,
    "how-it-works.html": how,
    "features.html": features,
    "pricing.html": pricing,
    "support.html": support,
    "events.html": events_hub,
    "privacy.html": privacy,
    "terms.html": terms,
    "refunds.html": refunds,
}

for event in EVENTS:
    FILES[f'{event["slug"]}.html'] = event_page(event)

for page_data in INTENT_PAGES:
    FILES[f'{page_data["slug"]}.html'] = intent_page(page_data)


CSS = r"""
:root{--text:#0b0d12;--muted:#666b76;--line:#eceef3;--soft:#f8f7f5;--cream:#fff8ed;--blue:#eff8ff;--accent:#ff4f7b;--radius:34px;--max:1180px}*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font-family:Inter,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;color:var(--text);background:#fff}img{max-width:100%;display:block}a{color:inherit;text-decoration:none}h1,h2,h3,p{margin-top:0}h1{font-size:clamp(44px,7vw,82px);line-height:.96;letter-spacing:-.07em;margin-bottom:22px}h2{font-size:clamp(34px,5vw,58px);line-height:1;letter-spacing:-.06em;margin-bottom:18px}h3{font-size:22px;letter-spacing:-.04em;margin-bottom:10px}p{color:var(--muted);line-height:1.68;font-size:17px}.site-header{height:82px;display:flex;align-items:center;gap:24px;max-width:1280px;margin:0 auto;padding:0 28px;position:sticky;top:0;background:rgba(255,255,255,.9);backdrop-filter:blur(18px);border:1px solid var(--line);border-radius:var(--radius);box-shadow:0 10px 30px rgba(11,13,18,.06);z-index:20}.brand{display:flex;align-items:center;gap:10px;font-weight:800;letter-spacing:-.03em}.brand-logo{width:42px;height:42px;object-fit:cover}.nav{display:flex;gap:30px;margin:0 auto;color:#30323a;font-size:15px;align-items:center}.nav a:hover,.nav-dropdown-toggle:hover{color:#000}.nav-cta,.btn{border-radius:999px;padding:14px 22px;font-weight:800;display:inline-flex;align-items:center;justify-content:center}.nav-cta,.btn.primary{background:#000;color:#fff}.btn.secondary{border:1px solid var(--line);background:#fff;color:#111}.btn.full{width:100%}.menu-toggle{display:none;background:#fff;border:1px solid var(--line);border-radius:16px;padding:10px 12px}.nav-dropdown{position:relative;display:flex;align-items:center}.nav-dropdown-toggle{background:none;border:0;padding:0;font:inherit;color:inherit;cursor:pointer;font-size:15px}.nav-dropdown-menu{display:none;position:absolute;top:100%;left:-16px;min-width:280px;background:#fff;border:1px solid var(--line);border-radius:24px;padding:22px 10px 10px;box-shadow:0 18px 40px rgba(11,13,18,.08);z-index:30}.nav-dropdown-menu a{display:block;padding:10px 14px;border-radius:14px;font-weight:800}.nav-dropdown-menu a:hover{background:var(--soft)}.nav-dropdown.open .nav-dropdown-menu,.nav-dropdown:focus-within .nav-dropdown-menu,.nav-dropdown:hover .nav-dropdown-menu{display:block}.section-pad{padding:80px 28px;max-width:var(--max);margin:0 auto}.breadcrumbs{padding-top:26px;padding-bottom:0;display:flex;flex-wrap:wrap;gap:10px;font-size:14px;color:#5b6170}.breadcrumbs a{font-weight:700}.breadcrumbs-sep{color:#a6abb4}.hero{min-height:760px;display:grid;grid-template-columns:1fr;place-items:center;justify-items:center;text-align:center;position:relative;overflow:hidden;background:radial-gradient(circle at 5% 24%,#fff0b8 0,transparent 22%),radial-gradient(circle at 92% 60%,#ffe3ce 0,transparent 22%),linear-gradient(#fff,#fffdfa);max-width:none}.hero-copy{width:100%;max-width:760px;margin:20px auto 0;padding-inline:20px;display:grid;justify-items:center}.hero-copy>p:not(.eyebrow):not(.microcopy){max-width:30ch;font-size:19px}.hero-actions{display:flex;gap:12px;justify-content:center;margin:28px 0 12px;flex-wrap:wrap}.microcopy{font-size:14px!important}.hero-visual{width:min(700px,96vw);margin-inline:auto}.hero-visual img,.event-hero-visual img{border-radius:42px}.hero-float-media{position:absolute;width:170px;height:170px;object-fit:cover;border-radius:999px;border:1px solid var(--line);box-shadow:0 18px 40px rgba(11,13,18,.1);background:#fff}.hero-float-left{left:7%;top:38%;transform:rotate(-8deg)}.hero-float-right{right:9%;top:47%;transform:rotate(7deg)}.eyebrow{font-size:13px;text-transform:uppercase;letter-spacing:.16em;color:var(--accent);font-weight:900;margin:0 0 16px}.center{text-align:center}.compact{padding-top:60px}.section-lead{max-width:720px;margin:0 auto 44px}.benefit-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:22px;text-align:left}.benefit-grid article,.support-grid article,.price-card,.include-panel,.timeline article,.legal,.faq details{border:1px solid var(--line);border-radius:var(--radius);padding:30px;background:#fff}.link-grid article{display:flex;flex-direction:column;justify-content:space-between}.alt{background:linear-gradient(110deg,var(--cream),#fff 50%,var(--blue));max-width:none}.split{display:grid;grid-template-columns:minmax(0,560px) minmax(0,560px);justify-content:center;gap:70px;align-items:center}.image-board,.usecase-steps{display:grid;gap:18px}.image-board img{border-radius:34px}.usecase-step{display:grid;grid-template-columns:120px 1fr;gap:18px;align-items:center;border:1px solid var(--line);border-radius:28px;padding:16px 18px;background:#fff}.usecase-step img{width:120px;height:120px;border-radius:24px;object-fit:cover}.usecase-step p{margin:0}.text-link{font-weight:900;border-bottom:2px solid #000;width:max-content}.pill-row,.use-grid{display:flex;flex-wrap:wrap;gap:12px;justify-content:center;max-width:940px;margin:32px auto 0}.pill-row span,.use-grid span{border:1px solid var(--line);border-radius:999px;padding:14px 18px;font-weight:800;background:#fff}.cta-panel{text-align:center;background:linear-gradient(120deg,#fff7e8,#fff,#f4f8ff);border-radius:46px;margin-bottom:80px}.cta-panel p{max-width:650px;margin:0 auto 28px}.page-hero{padding-top:40px;padding-bottom:42px}.page-hero p:not(.eyebrow){max-width:760px;margin:0 auto}.event-hero-visual{max-width:860px;margin:26px auto 0}.timeline{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}.feature-list{display:grid;gap:26px}.feature-list article{display:grid;grid-template-columns:260px 1fr;gap:38px;align-items:center;border-bottom:1px solid var(--line);padding-bottom:26px}.feature-list img{height:180px;width:260px;object-fit:cover;border-radius:28px}.pricing-wrap{display:grid;grid-template-columns:minmax(320px,520px) 1fr;gap:38px;align-items:start}.price-card h2{font-size:72px}.price-note{margin-top:-10px}.check-list{list-style:none;margin:28px 0 0;padding:0;display:grid;gap:14px}.compact-list{margin-top:20px}.check-list li{padding-left:30px;position:relative;color:#30323a}.check-list li:before{content:"✓";position:absolute;left:0;top:0;font-weight:900;color:#03a57a}.mini-steps{display:grid;gap:12px;margin-top:26px}.mini-steps span{padding:16px 18px;background:#fff;border:1px solid var(--line);border-radius:18px;font-weight:800}.support-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}.single-grid{grid-template-columns:1fr}.faq{max-width:920px}.faq h2{text-align:center}.faq details{padding:24px 30px}.faq summary{font-weight:900;font-size:20px;cursor:pointer;letter-spacing:-.03em}.faq p{margin:12px 0 0}.legal{max-width:860px}.footer{border-top:1px solid var(--line);padding:46px 28px;max-width:1280px;margin:0 auto;display:grid;gap:24px}.footer p{max-width:620px;font-size:15px}.footer-links{display:flex;flex-wrap:wrap;gap:18px;font-weight:800}.footer-events a{font-weight:700}.intent-links{justify-content:center}.copyright{font-size:13px!important;color:#8a8f98}.flowbar{max-width:980px;margin:0 auto;position:relative;--flowpad:80px}.flowbar-track{position:absolute;top:calc(var(--flowpad) + 62px);left:6%;right:6%;height:10px;border-radius:999px;background:linear-gradient(90deg,#ffe08f,#ff66b7,#a98bff,#8fd0ff);opacity:.95;z-index:1}.flowbar-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:48px;position:relative;text-align:center;z-index:2}.flowbar-icon{width:124px;height:124px;border:4px solid #050505;border-radius:50%;display:grid;place-items:center;margin:0 auto 18px;background:#fff;box-shadow:0 18px 34px rgba(11,13,18,.1);position:relative;z-index:2}.flowbar-icon img{width:44px;height:44px;object-fit:contain}.events-page .hero-copy{max-width:820px}@media(max-width:900px){.site-header{height:auto;min-height:72px;flex-wrap:wrap}.menu-toggle{display:block;margin-left:auto}.nav,.nav-cta{display:none}.nav.open{display:flex;order:5;width:100%;flex-direction:column;gap:12px;padding:18px 0}.nav-dropdown{width:100%;flex-direction:column;align-items:flex-start}.nav-dropdown-toggle{width:100%;text-align:left;padding:14px 0;font-weight:800}.nav-dropdown-menu{position:static;box-shadow:none;border:0;padding:0;margin:0 0 8px;display:none;min-width:auto;width:100%}.nav-dropdown.open .nav-dropdown-menu,.nav-dropdown:focus-within .nav-dropdown-menu{display:block}.nav-dropdown-menu a{padding:10px 0;border-radius:0;font-weight:700}.nav-dropdown-menu a:hover{background:transparent}.section-pad{padding:58px 20px}.hero{min-height:auto;padding-top:42px}.hero-actions{flex-direction:column}.hero-float-media{display:none}.hero-visual{width:min(320px,84vw)}.benefit-grid,.timeline,.support-grid,.pricing-wrap,.split,.feature-list article{grid-template-columns:1fr}.feature-list img{width:100%;height:auto}.usecase-step{grid-template-columns:1fr}.usecase-step img{width:100%;height:auto}h1{font-size:46px}.page-hero{padding-top:24px}.cta-panel{border-radius:32px;margin-left:20px;margin-right:20px}.flowbar{--flowpad:58px}.flowbar-track{display:none}.flowbar-grid{grid-template-columns:1fr;gap:26px}.faq details{padding:22px}}"""


# Preserve image proportions when responsive containers constrain their width.
CSS += "\nimg{height:auto}\n"


JS = """const menuButton=document.querySelector('[data-menu-toggle]');const nav=document.querySelector('[data-nav]');if(menuButton&&nav){menuButton.addEventListener('click',()=>nav.classList.toggle('open'));}document.querySelectorAll('[data-dropdown]').forEach(dropdown=>{const button=dropdown.querySelector('.nav-dropdown-toggle');if(!button)return;button.addEventListener('click',()=>{const expanded=button.getAttribute('aria-expanded')==='true';button.setAttribute('aria-expanded',String(!expanded));dropdown.classList.toggle('open',!expanded);});});"""


MANIFEST = {
    "name": "MyPhotoQR",
    "short_name": "MyPhotoQR",
    "start_url": "/",
    "display": "standalone",
    "background_color": "#ffffff",
    "theme_color": "#ffffff",
    "description": "QR albums for event photo and video sharing without an app.",
    "icons": [
        {
            "src": "/apple-touch-icon.png",
            "sizes": "180x180",
            "type": "image/png",
        },
        {
            "src": "/favicon-48x48.png",
            "sizes": "48x48",
            "type": "image/png",
        },
    ],
}


for filename, content in FILES.items():
    (ROOT / filename).write_text(content, encoding="utf-8")

(ROOT / "css" / "styles.css").write_text(CSS, encoding="utf-8")
(ROOT / "js" / "main.js").write_text(JS, encoding="utf-8")
(ROOT / "manifest.webmanifest").write_text(json.dumps(MANIFEST, ensure_ascii=False, indent=2), encoding="utf-8")

sitemap_urls = [
    ("", "weekly", "1.0"),
    ("how-it-works.html", "monthly", "0.85"),
    ("features.html", "monthly", "0.85"),
    ("pricing.html", "monthly", "0.8"),
    ("support.html", "monthly", "0.7"),
    ("events.html", "monthly", "0.8"),
]
sitemap_urls.extend((f'{event["slug"]}.html', "monthly", "0.75") for event in EVENTS)
sitemap_urls.extend((f'{page_data["slug"]}.html', "monthly", "0.78") for page_data in INTENT_PAGES)

sitemap_parts = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for loc, changefreq, priority in sitemap_urls:
    sitemap_parts.append("  <url>")
    sitemap_parts.append(f"    <loc>{absolute(loc)}</loc>")
    sitemap_parts.append(f"    <lastmod>{TODAY}</lastmod>")
    sitemap_parts.append(f"    <changefreq>{changefreq}</changefreq>")
    sitemap_parts.append(f"    <priority>{priority}</priority>")
    sitemap_parts.append("  </url>")
sitemap_parts.append("</urlset>")
(ROOT / "sitemap.xml").write_text("\n".join(sitemap_parts) + "\n", encoding="utf-8")

(ROOT / "robots.txt").write_text(
    "User-agent: *\nAllow: /\n\nHost: https://www.myphotoqr.com\nSitemap: https://www.myphotoqr.com/sitemap.xml\n",
    encoding="utf-8",
)
