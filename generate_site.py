from pathlib import Path

root=Path('/mnt/data/myphotoqr_site')
(root/'css').mkdir(exist_ok=True)
(root/'js').mkdir(exist_ok=True)
(root/'img').mkdir(exist_ok=True)

base_phrases = [
"qr album", "photo qr album", "event photo sharing", "wedding qr album", "party photo album qr", "qr photo upload", "guest photo upload", "no app photo sharing", "instant photo sharing", "event gallery", "live event gallery", "live slideshow", "wedding photo sharing app", "qr code photo album", "event memories", "photo booth alternative", "collect guest photos", "upload wedding photos qr", "birthday qr album", "graduation qr album", "corporate event album", "quinceanera qr album", "baby shower photo sharing", "bridal shower qr photos", "anniversary photo album", "event photo collection", "shared photo album for event", "qr code for wedding photos", "qr upload link", "browser photo upload", "event video upload", "guest video upload", "download event photos", "zip photo export", "moderated event gallery", "private event album", "photo sharing without app", "digital event album", "scan qr upload photos", "qr gallery", "event qr code", "wedding memories online", "photo album for guests", "event album link", "photo upload page", "instant upload gallery", "qr photo sharing for events", "event media collection", "memories gallery", "event content hub", "wedding gallery live", "qr album for wedding", "guest upload website", "no login photo upload", "mobile photo sharing", "android iphone event album", "web based photo album", "event photo wall", "realtime photo wall", "event slideshow screen", "wedding slideshow live", "scan to upload photos", "scan to share photos", "share event photos qr", "photo drop for events", "qr memory album", "digital guestbook photos", "event notes audio photos", "event audio notes", "guest notes album", "event keepsake album", "online wedding album", "one time payment photo album", "affordable event photo sharing", "secure photo sharing event", "private qr album", "album protected by code", "photo moderation event", "approve guest photos", "hide guest uploads", "featured event photos", "event gallery admin", "album dashboard", "custom event album", "branded event gallery", "custom qr album", "event album themes", "event album cover", "album banner", "photo sharing link", "upload photos from phone", "event uploads from browser", "qr code wedding sign", "table qr photo upload", "event signs qr code", "wedding table qr code", "photo collection for wedding planner", "event planner photo sharing", "venue photo sharing tool", "corporate event memories", "conference photo album", "festival photo sharing", "concert photo sharing", "school event album", "sports event photo album", "family reunion qr album", "travel group photo album", "engagement party qr album", "bachelorette photo sharing", "bachelor party photo album", "holiday party photo sharing", "memorial event photo album", "fundraiser photo sharing", "church event photo album", "community event photo album", "reunion photo upload qr", "event photo archive", "digital memories event", "upload videos by qr", "photo video gallery", "share photos videos instantly", "event upload portal", "online gallery for guests", "guest media upload", "collect videos from guests", "all guest photos in one place", "replace whatsapp photo sharing", "avoid lost event photos", "wedding photo collection link", "qr code gallery app", "photo album qr code generator", "event album qr generator", "qr code upload system", "easy qr album", "create qr album", "make qr album", "fast event album setup", "instant qr album setup", "qr album one event", "photo sharing for one event", "download all photos after event", "photo album with qr code", "qr photo gallery for events", "online gallery no app", "real time photo upload event", "event media gallery", "collect memories with qr", "share memories with qr", "guest generated event content", "ugc event gallery", "event user generated content", "photo sharing software", "event SaaS photo sharing", "event memory platform", "qr memories platform", "live gallery software", "digital event guestbook", "wedding guest photo collection", "birthday guest photo upload", "graduation guest photo upload", "qr code photo wall", "photo wall for events", "slideshow with guest photos", "tv slideshow event photos", "projector slideshow wedding", "private event photo website", "secure wedding photo upload", "photo album with access code", "guest photo approval", "curated event album", "moderation dashboard photos", "event organizer photo control", "view and upload link", "upload only link", "admin link album", "qr album admin panel", "smart event photo album", "simple event photo album", "minimal event photo sharing", "clean event gallery", "modern qr album", "myphotoqr", "my photo qr", "MyPhotoQR event album"
]
modifiers = ["best", "easy", "fast", "simple", "secure", "private", "live", "online", "mobile", "instant", "modern", "affordable", "professional", "custom", "browser based", "no app", "real time", "shareable", "downloadable", "moderated"]
contexts = ["weddings", "events", "birthdays", "graduations", "corporate events", "parties", "quinceaneras", "baby showers", "bridal showers", "anniversaries", "conferences", "reunions", "festivals", "school events", "family events", "venues", "event planners", "guests", "hosts", "organizers"]
keywords=[]
for p in base_phrases:
    keywords.append(p)
for m in modifiers:
    for p in base_phrases[:120]:
        keywords.append(f"{m} {p}")
for p in base_phrases[:80]:
    for c in contexts:
        keywords.append(f"{p} for {c}")
# ensure >2000 phrases and many words
keywords = list(dict.fromkeys(keywords))
keywords_meta = ", ".join(keywords)

nav = '''
<header class="site-header">
  <a class="brand" href="index.html" aria-label="MyPhotoQR home">
    <img src="img/logo-myphotoqr.jpg" alt="MyPhotoQR logo" class="brand-logo">
    <span>MyPhotoQR</span>
  </a>
  <button class="menu-toggle" aria-label="Open menu" data-menu-toggle>☰</button>
  <nav class="nav" data-nav>
    <a href="index.html">Home</a>
    <a href="how-it-works.html">How it works</a>
    <a href="features.html">Features</a>
    <a href="pricing.html">Pricing</a>
    <a href="support.html">Support</a>
  </nav>
  <a class="nav-cta" href="https://app.myphotoqr.com/create">Buy album</a>
</header>'''
footer = '''
<footer class="footer">
  <div>
    <a class="brand footer-brand" href="index.html"><img src="img/logo-myphotoqr.jpg" alt="MyPhotoQR logo" class="brand-logo"><span>MyPhotoQR</span></a>
    <p>QR albums for weddings, birthdays, graduations, corporate events and every celebration worth remembering.</p>
  </div>
  <div class="footer-links">
    <a href="privacy.html">Privacy</a>
    <a href="terms.html">Terms</a>
    <a href="refunds.html">Refunds</a>
    <a href="support.html">Contact</a>
  </div>
  <p class="copyright">© 2026 MyPhotoQR. All rights reserved. Support: support@myphotoqr.com</p>
</footer>'''

def head(title, desc, canonical, extra=''):
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="keywords" content="{keywords_meta}">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <meta name="author" content="MyPhotoQR">
  <link rel="canonical" href="https://myphotoqr.com/{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="https://myphotoqr.com/{canonical}">
  <meta property="og:image" content="https://myphotoqr.com/img/og-myphotoqr.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="https://myphotoqr.com/img/og-myphotoqr.jpg">
  <link rel="icon" href="img/favicon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/styles.css">
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"SoftwareApplication","name":"MyPhotoQR","applicationCategory":"MultimediaApplication","operatingSystem":"Web","offers":{{"@type":"Offer","price":"19.99","priceCurrency":"USD","availability":"https://schema.org/InStock"}},"description":"A no-app QR album for event photo and video sharing.","url":"https://myphotoqr.com"}}</script>
  {extra}
</head>'''

home = head('MyPhotoQR | QR Album for Event Photo Sharing, No App Needed', 'Create a QR album for your event. Guests scan a QR code, upload photos and videos from their browser, enjoy a live gallery, and download everything after the event.', 'index.html') + f'''
<body>{nav}
<main>
<section class="hero section-pad">
  <div class="floating-badge badge-left"><img src="img/icon-gallery.png" alt="Live gallery icon"><span>Live gallery</span></div>
  <div class="floating-badge badge-right"><img src="img/icon-qr.png" alt="QR sharing icon"><span>QR ready</span></div>
  <div class="hero-copy">
    <p class="eyebrow">No app needed · Made for real events</p>
    <h1>Your QR Album — instant photo and video sharing for any event</h1>
    <p>Guests scan your QR code, upload from their phone, and every memory lands in one clean online album. You stay in control with privacy, moderation, live slideshow, and final export.</p>
    <div class="hero-actions"><a class="btn primary" href="https://app.myphotoqr.com/create">Buy album for $19.99</a><a class="btn secondary" href="features.html">View features</a></div>
    <p class="microcopy">Works on iPhone, Android, tablets and desktop browsers. Setup takes minutes.</p>
  </div>
  <div class="hero-visual">
    <img src="img/home-phone-mockup.jpg" alt="MyPhotoQR guest upload and live gallery phone mockup">
  </div>
</section>
<section class="section-pad compact center">
  <h2>Everything guests share, organized in one private event album</h2>
  <p class="section-lead">Stop chasing photos through group chats. MyPhotoQR gives every guest one simple place to upload photos, videos, notes and audio memories.</p>
  <div class="benefit-grid">
    <article><img src="img/icon-qr.png" alt="QR icon"><h3>QR ready to print</h3><p>Place the QR on tables, invitations, signs, screens or messages.</p></article>
    <article><img src="img/icon-upload.png" alt="Upload icon"><h3>Browser uploads</h3><p>Guests upload directly from their phones without downloading an app.</p></article>
    <article><img src="img/icon-slideshow.png" alt="Slideshow icon"><h3>Live slideshow</h3><p>Show approved memories on a TV or projector while the event is happening.</p></article>
    <article><img src="img/icon-download.png" alt="Download icon"><h3>Final ZIP export</h3><p>Download photos and videos after the event to keep them forever.</p></article>
  </div>
</section>
<section class="split section-pad alt">
  <div class="center"><p class="eyebrow">Built for every celebration</p><h2>One QR code for weddings, birthdays, graduations, parties and corporate events</h2><p>Whether your guests are at the table, on the dance floor, at a booth, or across the venue, they can upload memories in real time. Your album keeps everything structured and easy to review.</p><a class="text-link" href="how-it-works.html">See how it works →</a></div>
  <div class="image-board"><img src="img/event-collage.jpg" alt="Event collage with QR album examples"><img src="img/feature-slideshow.jpg" alt="Live gallery slideshow"></div>
</section>
<section class="flowbar section-pad">
  <div class="flowbar-track" aria-hidden="true"></div>
  <div class="flowbar-grid">
    <article><div class="flowbar-icon"><img src="img/icon-gallery.png" alt="Create a QR album"></div><h3>Create a QR album</h3><p>Set up your album in seconds with a custom design, name and description.</p><a class="btn primary" href="https://app.myphotoqr.com/create">Buy album</a></article>
    <article><div class="flowbar-icon"><img src="img/icon-qr.png" alt="Share your QR or Link"></div><h3>Share your QR or Link</h3><p>Share your unique QR code or link with anyone so they can access the album and start sharing instantly.</p></article>
    <article><div class="flowbar-icon"><img src="img/icon-upload.png" alt="Collect Memories"></div><h3>Collect Memories</h3><p>Watch photos, videos and notes appear in real time, all in one place.</p></article>
  </div>
</section>
<section class="section-pad center">
  <h2>What you get with one event album</h2>
  <div class="pill-row"><span>1 event album</span><span>QR + share links</span><span>Guest uploads</span><span>Live gallery</span><span>Moderation</span><span>Live slideshow</span><span>ZIP download</span><span>1 year storage</span></div>
</section>
<section class="cta-panel section-pad"><h2>Collect the memories your guests already captured</h2><p>Create one simple QR album and make photo sharing feel effortless from the first scan to the final download.</p><a class="btn primary" href="https://app.myphotoqr.com/create">Buy album for $19.99</a></section>
</main>{footer}<script src="js/main.js"></script></body></html>'''

how = head('How MyPhotoQR Works | Create, Share, Collect and Download Event Photos', 'Learn how to create a QR album, personalize it, share QR links with guests, collect photos and videos in real time, and export your event memories.', 'how-it-works.html') + f'''
<body>{nav}<main>
<section class="page-hero section-pad center"><p class="eyebrow">Simple from the first scan</p><h1>How it works?</h1><p>Set up your event album, share the QR code, collect memories live, and download everything when the celebration is over.</p></section>
<section class="flowbar section-pad">
  <div class="flowbar-track" aria-hidden="true"></div>
  <div class="flowbar-grid">
    <article><div class="flowbar-icon"><img src="img/icon-gallery.png" alt="Create a QR album"></div><h3>Create a QR album</h3><p>Set up your album in seconds with a custom design, name and description.</p><a class="btn primary" href="https://app.myphotoqr.com/create">Buy album</a></article>
    <article><div class="flowbar-icon"><img src="img/icon-qr.png" alt="Share your QR or Link"></div><h3>Share your QR or Link</h3><p>Share your unique QR code or link with anyone so they can access the album and start sharing instantly.</p></article>
    <article><div class="flowbar-icon"><img src="img/icon-upload.png" alt="Collect Memories"></div><h3>Collect Memories</h3><p>Watch photos, videos and notes appear in real time, all in one place.</p></article>
  </div>
</section>
<section class="timeline section-pad">
  <article><div class="step-icon"><img src="img/icon-gallery.png" alt="Create album"></div><h2>Create your QR album</h2><p>Add your event name, type, date, location, short message, cover image and banner. Your album starts with a clean setup made for guests.</p></article>
  <article><div class="step-icon"><img src="img/icon-slideshow.png" alt="Customize album"></div><h2>Customize the experience</h2><p>Choose colors, background, event label, emoji, privacy settings and upload rules for photos, videos, notes and audio memories.</p></article>
  <article><div class="step-icon"><img src="img/icon-qr.png" alt="Share QR"></div><h2>Share your QR or link</h2><p>Use your QR on printed signs, table cards, invitations, WhatsApp, Instagram, email or screens. Guests open it in their browser.</p></article>
  <article><div class="step-icon"><img src="img/icon-upload.png" alt="Receive uploads"></div><h2>Receive memories in real time</h2><p>Guests upload from iPhone, Android, tablet or desktop. Your live gallery updates as content arrives.</p></article>
  <article><div class="step-icon"><img src="img/icon-gallery.png" alt="Moderation"></div><h2>Approve, hide or feature</h2><p>Turn moderation on, auto-approve uploads, keep items pending, hide content, or highlight your favorite memories.</p></article>
  <article><div class="step-icon"><img src="img/icon-download.png" alt="Download album"></div><h2>Export the final album</h2><p>Download a ZIP with photos and videos so the event memories can stay on your phone, computer or cloud storage.</p></article>
</section>
<section class="split section-pad alt"><div><h2>Designed for a smooth guest experience</h2><p>No app store, no passwords, no complicated instructions. Guests scan, tap upload, choose a file, and send it to your album.</p></div><div class="image-board"><img src="img/feature-upload.jpg" alt="Guest upload screen"></div></section>
<section class="faq section-pad"><h2>Quick answers</h2>
  <details><summary>Do guests need to install an app?</summary><p>No. MyPhotoQR works from the browser on mobile, tablet and desktop.</p></details>
  <details><summary>Can I protect the album with a code?</summary><p>Yes. You can use access protection so only people with the code can view or upload.</p></details>
  <details><summary>Can I review uploads before they appear?</summary><p>Yes. Use moderation to approve, hide, feature or auto-approve content.</p></details>
  <details><summary>What happens if internet is slow?</summary><p>Guests can try again when the connection improves. For best results, place the QR near areas with strong mobile data or Wi‑Fi.</p></details>
</section>
<section class="cta-panel section-pad"><h2>Have your QR album ready before guests arrive</h2><a class="btn primary" href="https://app.myphotoqr.com/create">Buy album</a></section>
</main>{footer}<script src="js/main.js"></script></body></html>'''

features = head('MyPhotoQR Features | QR Event Album, Live Gallery, Moderation and Export', 'Explore MyPhotoQR features: custom QR album, guest photo and video uploads, live slideshow, privacy code, moderation, branding, and ZIP export.', 'features.html') + f'''
<body>{nav}<main>
<section class="page-hero section-pad center"><p class="eyebrow">Made for event memories</p><h1>Features that make photo sharing feel effortless</h1><p>Everything you need to collect, organize, moderate, display and keep the best content from your event.</p></section>
<section class="feature-list section-pad">
  <article><img src="img/feature-branding.jpg" alt="Album branding settings"><div><h2>Album and branding</h2><p>Make the album feel like your event with a name, description, event type, custom label, date, location, cover image, banner and theme colors.</p></div></article>
  <article><img src="img/feature-upload.jpg" alt="Guest upload screen"><div><h2>Guest uploads from the browser</h2><p>Allow guests to upload photos, videos, notes and audio memories from iPhone, Android, tablets or desktop without installing an app.</p></div></article>
  <article><img src="img/feature-slideshow.jpg" alt="Live slideshow"><div><h2>Live gallery and slideshow</h2><p>Turn uploaded memories into a live slideshow for TVs, projectors or screens at the venue. Use approved or featured content for a polished display.</p></div></article>
  <article><img src="img/feature-export.jpg" alt="Export album"><div><h2>Download and export</h2><p>After the event, export your album as a ZIP with photos and videos so you can keep everything on your phone or computer.</p></div></article>
</section>
<section class="section-pad center alt"><h2>Perfect for many types of events</h2><div class="use-grid"><span>Weddings</span><span>Birthdays</span><span>Graduations</span><span>Corporate events</span><span>Quinceañeras</span><span>Baby showers</span><span>Anniversaries</span><span>Family reunions</span><span>School events</span><span>Holiday parties</span></div></section>
<section class="cta-panel section-pad"><h2>Give every guest a simple way to share memories</h2><a class="btn primary" href="https://app.myphotoqr.com/create">Buy album for $19.99</a></section>
</main>{footer}<script src="js/main.js"></script></body></html>'''

pricing = head('MyPhotoQR Pricing | One-Time $19.99 QR Album for One Event', 'Create one QR album for one event with a one-time $19.99 payment. Includes QR links, guest uploads, live gallery, moderation, slideshow, ZIP export and 1 year storage.', 'pricing.html') + f'''
<body>{nav}<main>
<section class="page-hero section-pad center"><p class="eyebrow">One event. One payment.</p><h1>Simple pricing for your QR album</h1><p>No monthly subscription. Create one event album and collect memories from your guests.</p></section>
<section class="pricing-wrap section-pad">
  <article class="price-card">
    <p class="eyebrow">QR Album — one-time payment</p>
    <h2>$19.99</h2>
    <p class="price-note">Includes 1 album for 1 event with an admin panel.</p>
    <a class="btn primary full" href="https://app.myphotoqr.com/create">Buy album</a>
    <ul class="check-list">
      <li>1 event album</li><li>QR code and share links for guests</li><li>Guest uploads from the browser</li><li>Photos, videos, notes and audio memories</li><li>Live gallery for viewing content</li><li>Privacy and visibility controls</li><li>Album configuration: name, description, type, date, location, cover, banner and theme</li><li>Moderation: approve, hide, feature or auto-approve</li><li>Live slideshow for TV or projector</li><li>ZIP export with photos and videos</li><li>1 year active album and storage</li><li>Email support within 24–48 business hours</li>
    </ul>
  </article>
  <aside class="include-panel"><h2>What happens after payment?</h2><p>After checkout, you are redirected to your MyPhotoQR account so you can create and manage your album, personalize the experience, and start sharing your QR code.</p><div class="mini-steps"><span>1. Pay securely</span><span>2. Create album</span><span>3. Share QR</span><span>4. Collect memories</span><span>5. Download ZIP</span></div></aside>
</section>
<section class="faq section-pad"><h2>Pricing FAQ</h2>
  <details><summary>Is this a subscription?</summary><p>No. The $19.99 plan is a one-time payment for one event album.</p></details>
  <details><summary>How long does the album stay active?</summary><p>The album and uploaded files remain active for 1 year from the album creation date.</p></details>
  <details><summary>Are audio and notes included?</summary><p>Yes. The paid plan can include photos, videos, audio memories and notes when those upload options are enabled for the album.</p></details>
  <details><summary>Can I download everything?</summary><p>Yes. You can export the album as a ZIP with photos and videos.</p></details>
</section>
</main>{footer}<script src="js/main.js"></script></body></html>'''

support = head('MyPhotoQR Support | Help for QR Albums, Guest Uploads and Event Galleries', 'Get help with QR albums, guest uploads, live gallery, moderation, slideshow, download export, privacy settings and event setup.', 'support.html') + f'''
<body>{nav}<main>
<section class="page-hero section-pad center"><p class="eyebrow">Help when you need it</p><h1>Support for your QR album</h1><p>Questions about setup, QR sharing, guest uploads, moderation, slideshow or exports? We can help.</p></section>
<section class="support-grid section-pad">
  <article><h2>Contact support</h2><p>Email us at <a href="mailto:support@myphotoqr.com">support@myphotoqr.com</a>. Standard response time is 24–48 business hours.</p><a class="btn secondary" href="mailto:support@myphotoqr.com">Send email</a></article>
  <article><h2>Before your event</h2><p>Test your QR, open the upload page from a phone, check your album privacy, and confirm that your slideshow works on the screen you plan to use.</p></article>
  <article><h2>During your event</h2><p>Place QR signs where guests can see them, keep the link available in messages, and use moderation if you want to review content before it appears.</p></article>
</section>
<section class="faq section-pad"><h2>Support FAQ</h2>
  <details><summary>How do I print my QR code?</summary><p>Download your QR code from the album dashboard and place it on table cards, signs, invitations, screens or event programs.</p></details>
  <details><summary>What formats are supported?</summary><p>The album is designed for photos, videos, audio memories and notes. Exact upload limits can depend on the active album settings.</p></details>
  <details><summary>Can guests download the album?</summary><p>The album owner controls export and sharing options. The final ZIP export is available from the admin experience.</p></details>
  <details><summary>Can I change my album after sharing the QR?</summary><p>Yes. You can update the album name, description, theme, cover, settings and visibility from the admin panel.</p></details>
</section>
<section class="cta-panel section-pad"><h2>Ready to create your event album?</h2><a class="btn primary" href="https://app.myphotoqr.com/create">Buy album</a></section>
</main>{footer}<script src="js/main.js"></script></body></html>'''

legal_tpl = lambda title, desc, body: head(title, desc, title.lower().split('|')[0].strip().replace(' ','-')+'.html') + f'<body>{nav}<main><section class="legal section-pad"><h1>{title.split("|")[0].strip()}</h1>{body}</section></main>{footer}<script src="js/main.js"></script></body></html>'
privacy=legal_tpl('Privacy Policy | MyPhotoQR','Privacy information for MyPhotoQR event album users and guests.','<p>MyPhotoQR is designed to collect event memories through QR links and browser uploads. Album owners control visibility, sharing and moderation settings.</p><p>We collect account, album and upload information needed to operate the service. Uploaded content may include photos, videos, notes and audio memories shared by guests.</p><p>For privacy questions, contact support@myphotoqr.com.</p>')
terms=legal_tpl('Terms of Service | MyPhotoQR','Terms for using MyPhotoQR QR albums, guest uploads, live gallery and event sharing tools.','<p>By using MyPhotoQR, you agree to use the service lawfully and only upload content you have permission to share. Album owners are responsible for managing guest access and content moderation.</p><p>The one-time event album plan includes the features shown on the pricing page, subject to reasonable technical limits and acceptable use.</p><p>For terms questions, contact support@myphotoqr.com.</p>')
refunds=legal_tpl('Refund Policy | MyPhotoQR','Refund information for MyPhotoQR one-time QR album purchases.','<p>Because MyPhotoQR provides digital event album access, refund eligibility may depend on whether the album has been created, used, shared or received uploads.</p><p>Contact support@myphotoqr.com with your purchase email and event details. We review requests case by case.</p>')

files={'index.html':home,'how-it-works.html':how,'features.html':features,'pricing.html':pricing,'support.html':support,'privacy.html':privacy,'terms.html':terms,'refunds.html':refunds}
for name, content in files.items():
    (root/name).write_text(content, encoding='utf-8')

css = r'''
:root{--text:#0b0d12;--muted:#666b76;--line:#eceef3;--soft:#f8f7f5;--cream:#fff8ed;--pink:#fff0f7;--blue:#eff8ff;--accent:#ff4f7b;--orange:#ff8a36;--radius:34px;--max:1180px}*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font-family:Inter,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;color:var(--text);background:#fff}img{max-width:100%;display:block}a{color:inherit;text-decoration:none}.site-header{height:82px;display:flex;align-items:center;gap:28px;max-width:1280px;margin:0 auto;padding:0 28px;position:sticky;top:0;background:rgba(255,255,255,.88);backdrop-filter:blur(18px);border:1px solid var(--line);border-radius:var(--radius);box-shadow:0 10px 30px rgba(11,13,18,.06);z-index:20}.brand{display:flex;align-items:center;gap:10px;font-weight:800;letter-spacing:-.03em}.brand-logo{width:42px;height:42px;border-radius:0;object-fit:cover;background:transparent;border:0}.nav{display:flex;gap:34px;margin:0 auto;color:#30323a;font-size:15px}.nav a:hover{color:#000}.nav-cta,.btn{border-radius:999px;padding:14px 22px;font-weight:800;display:inline-flex;align-items:center;justify-content:center}.nav-cta,.btn.primary{background:#000;color:#fff}.btn.secondary{border:1px solid var(--line);background:#fff;color:#111}.btn.full{width:100%}.menu-toggle{display:none;background:#fff;border:1px solid var(--line);border-radius:16px;padding:10px 12px}.section-pad{padding:80px 28px;max-width:var(--max);margin:0 auto}.hero{min-height:760px;display:grid;grid-template-columns:1fr;place-items:center;text-align:center;position:relative;overflow:hidden;background:radial-gradient(circle at 5% 24%,#fff0b8 0,transparent 22%),radial-gradient(circle at 92% 60%,#ffe3ce 0,transparent 22%),linear-gradient(#fff,#fffdfa);max-width:none}.hero-copy{max-width:820px;margin-top:20px}.eyebrow{font-size:13px;text-transform:uppercase;letter-spacing:.16em;color:var(--accent);font-weight:900;margin:0 0 16px}h1,h2,h3,p{margin-top:0}h1{font-size:clamp(44px,7vw,86px);line-height:.96;letter-spacing:-.07em;margin-bottom:22px}h2{font-size:clamp(34px,5vw,58px);line-height:1;letter-spacing:-.06em;margin-bottom:18px}h3{font-size:22px;letter-spacing:-.04em;margin-bottom:8px}p{color:var(--muted);line-height:1.65;font-size:17px}.hero-copy>p:not(.eyebrow){font-size:19px}.hero-actions{display:flex;gap:12px;justify-content:center;margin:28px 0 12px}.microcopy{font-size:14px!important}.hero-visual{width:min(390px,80vw);margin-top:36px}.hero-visual img{border-radius:46px}.floating-badge{position:absolute;background:#fff;border:1px solid var(--line);border-radius:26px;padding:16px 18px;display:flex;align-items:center;gap:12px;font-weight:800;transform:rotate(-8deg)}.floating-badge img{width:38px;height:38px;border-radius:12px;object-fit:cover}.badge-left{left:7%;top:38%}.badge-right{right:9%;top:47%;transform:rotate(7deg)}.center{text-align:center}.compact{padding-top:70px}.section-lead{max-width:680px;margin:0 auto 44px}.benefit-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:22px;text-align:left}.benefit-grid article,.support-grid article,.price-card,.include-panel{border:1px solid var(--line);border-radius:var(--radius);padding:32px;background:#fff}.benefit-grid img{width:58px;height:58px;border-radius:0;object-fit:cover;margin-bottom:22px}.alt{background:linear-gradient(110deg,var(--cream),#fff 50%,var(--blue));max-width:none}.split{display:grid;grid-template-columns:minmax(0,560px) minmax(0,560px);justify-content:center;gap:70px;align-items:center}.split>div:first-child{max-width:560px;justify-self:center}.image-board img{border-radius:38px}.text-link{font-weight:900;border-bottom:2px solid #000}.pill-row{display:flex;flex-wrap:wrap;gap:12px;justify-content:center;max-width:900px;margin:32px auto 0}.pill-row span,.use-grid span{border:1px solid var(--line);border-radius:999px;padding:14px 18px;font-weight:800;background:#fff}.cta-panel{text-align:center;background:linear-gradient(120deg,#fff7e8,#fff,#f4f8ff);border-radius:46px;margin-bottom:80px}.alt+.cta-panel{margin-top:40px}.cta-panel p{max-width:650px;margin:0 auto 28px}.page-hero{padding-top:96px;padding-bottom:42px}.page-hero p:not(.eyebrow){max-width:740px;margin:0 auto}.timeline{display:grid;grid-template-columns:repeat(3,1fr);gap:46px}.timeline article{text-align:center}.step-icon{margin:0 auto 28px}.step-icon img{width:64px;height:64px;object-fit:contain;border-radius:0}.faq{max-width:880px}.faq h2{text-align:center}.faq details{border-top:1px solid var(--line);padding:24px 0}.faq details:last-child{border-bottom:1px solid var(--line)}.faq summary{font-weight:900;font-size:20px;cursor:pointer;letter-spacing:-.03em}.faq p{margin:12px 0 0}.feature-list{display:grid;gap:26px}.feature-list article{display:grid;grid-template-columns:260px 1fr;gap:38px;align-items:center;border-bottom:1px solid var(--line);padding-bottom:26px}.feature-list img{height:180px;width:260px;object-fit:cover;border-radius:28px}.use-grid{display:flex;flex-wrap:wrap;justify-content:center;gap:14px;max-width:900px;margin:36px auto 0}.pricing-wrap{display:grid;grid-template-columns:minmax(320px,520px) 1fr;gap:38px;align-items:start}.price-card h2{font-size:72px}.price-note{margin-top:-10px}.check-list{list-style:none;margin:28px 0 0;padding:0;display:grid;gap:14px}.check-list li{padding-left:30px;position:relative;color:#30323a}.check-list li:before{content:"✓";position:absolute;left:0;top:0;font-weight:900;color:#03a57a}.mini-steps{display:grid;gap:12px;margin-top:26px}.mini-steps span{padding:16px 18px;background:#fff;border:1px solid var(--line);border-radius:18px;font-weight:800}.support-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}.legal{max-width:860px}.footer{border-top:1px solid var(--line);padding:46px 28px;max-width:1280px;margin:0 auto;display:grid;gap:24px}.footer p{max-width:520px;font-size:15px}.footer-links{display:flex;flex-wrap:wrap;gap:20px;font-weight:800}.copyright{font-size:13px!important;color:#8a8f98}@media(max-width:900px){.site-header{height:auto;min-height:72px;flex-wrap:wrap}.menu-toggle{display:block;margin-left:auto}.nav,.nav-cta{display:none}.nav.open{display:flex;order:5;width:100%;flex-direction:column;gap:12px;padding:18px 0}.hero{min-height:auto;padding-top:42px}.hero-actions{flex-direction:column}.floating-badge{display:none}.benefit-grid,.timeline,.support-grid,.pricing-wrap,.split{grid-template-columns:1fr}.split>div:first-child{justify-self:auto}.feature-list article{grid-template-columns:1fr}.feature-list img{width:100%;height:auto}h1{font-size:46px}.section-pad{padding:58px 20px}.page-hero{padding-top:58px}.cta-panel{border-radius:32px;margin-left:20px;margin-right:20px}}'''
css += "\n.image-board{display:grid;gap:18px}\n.flowbar{max-width:980px;margin:0 auto;position:relative;--flowpad:80px}.flowbar-track{position:absolute;top:calc(var(--flowpad) + 62px);left:6%;right:6%;height:10px;border-radius:999px;background:linear-gradient(90deg,#ffe08f,#ff66b7,#a98bff,#8fd0ff);opacity:.95;z-index:1}.flowbar-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:48px;position:relative;text-align:center;z-index:2}.flowbar-icon{width:124px;height:124px;border:4px solid #050505;border-radius:50%;display:grid;place-items:center;margin:0 auto 18px;background:#fff;box-shadow:0 18px 34px rgba(11,13,18,.10);position:relative;z-index:2}.flowbar-icon img{width:44px;height:44px;object-fit:contain;border-radius:0}.flowbar-grid h3{font-size:30px;letter-spacing:-.05em;margin:0 0 10px}.flowbar-grid p{margin:0 auto;max-width:320px}.flowbar-grid .btn{margin-top:14px}@media(max-width:900px){.flowbar{--flowpad:58px}.flowbar-track{display:none}.flowbar-grid{grid-template-columns:1fr;gap:26px}.flowbar-icon{box-shadow:0 10px 20px rgba(11,13,18,.10)}}.page-hero+.flowbar.section-pad{padding-top:40px;--flowpad:40px}@media(max-width:900px){.page-hero+.flowbar.section-pad{padding-top:24px;--flowpad:24px}}\n"
(root/'css/styles.css').write_text(css,encoding='utf-8')
js="""const menuButton=document.querySelector('[data-menu-toggle]');const nav=document.querySelector('[data-nav]');if(menuButton&&nav){menuButton.addEventListener('click',()=>nav.classList.toggle('open'));}"""
(root/'js/main.js').write_text(js,encoding='utf-8')

# placeholder manifest
(root/'IMG_REFERENCES.txt').write_text('''Replace these referenced images with your final files:\n\nimg/logo-myphotoqr.jpg\nimg/favicon.png\nimg/og-myphotoqr.jpg\nimg/home-phone-mockup.jpg\nimg/event-collage.jpg\nimg/icon-gallery.png\nimg/icon-qr.png\nimg/icon-upload.png\nimg/icon-slideshow.png\nimg/icon-download.png\nimg/feature-branding.jpg\nimg/feature-upload.jpg\nimg/feature-slideshow.jpg\nimg/feature-export.jpg\n''',encoding='utf-8')
