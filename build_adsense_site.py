#!/usr/bin/env python3
"""
Rebuild bpmfinder.ca as AdSense-ready multi-page content site.
- Substantial original text (not thin SPA)
- Privacy / Terms / About / Contact
- Guide articles
- Working tool at app.html (kept)
- ads.txt + sitemap + robots
"""
from __future__ import annotations

from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PUB = "ca-pub-0646320966060599"
YEAR = str(date.today().year)

CSS = """
:root {
  --bg: #f6f5f2; --card: #fff; --ink: #1a1a1a; --muted: #555;
  --line: #e2ddd4; --accent: #0b6e4f; --accent2: #16324f; --link: #0a5c8a;
}
* { box-sizing: border-box; }
body { margin: 0; font-family: Georgia, "Times New Roman", serif; color: var(--ink);
  background: var(--bg); line-height: 1.7; font-size: 18px; }
a { color: var(--link); }
.wrap { max-width: 780px; margin: 0 auto; padding: 0 1.2rem; }
header.site { background: var(--card); border-bottom: 1px solid var(--line);
  padding: .9rem 0; position: sticky; top: 0; z-index: 30; }
.nav { display: flex; flex-wrap: wrap; gap: .7rem 1rem; align-items: center; justify-content: space-between; }
.brand { font-family: system-ui,sans-serif; font-weight: 800; color: var(--accent2); text-decoration: none; letter-spacing: .02em; }
.navlinks { display: flex; flex-wrap: wrap; gap: .55rem .9rem; font-family: system-ui,sans-serif; font-size: .88rem; }
.navlinks a { text-decoration: none; color: var(--muted); }
.navlinks a:hover, .navlinks a[aria-current="page"] { color: var(--accent); font-weight: 600; }
.hero { padding: 2rem 0 1rem; }
.hero h1 { font-size: clamp(1.65rem, 4vw, 2.25rem); line-height: 1.25; margin: 0 0 .7rem; color: var(--accent2); }
.lead { color: var(--muted); font-size: 1.08rem; margin: 0 0 1.1rem; }
.cta-row { display: flex; flex-wrap: wrap; gap: .6rem; font-family: system-ui,sans-serif; }
.btn { display: inline-block; padding: .68rem 1.05rem; border-radius: 8px; text-decoration: none !important;
  font-weight: 700; font-size: .9rem; border: 1px solid var(--line); background: var(--card); color: var(--accent2); }
.btn.primary { background: var(--accent); border-color: var(--accent); color: #fff; }
.notice { margin: 1.1rem 0 0; padding: .85rem 1rem; background: #eef6f2; border: 1px solid #c5e0d4;
  border-radius: 10px; font-family: system-ui,sans-serif; font-size: .9rem; }
.card { background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 1.35rem 1.25rem; margin: 1.1rem 0; }
.card h2 { margin: 0 0 .45rem; font-size: 1.28rem; color: var(--accent2); }
.card h3 { margin: 1rem 0 .3rem; font-size: 1.05rem; }
.meta { font-family: system-ui,sans-serif; font-size: .8rem; color: var(--muted); margin-bottom: .55rem; }
.ad-slot { margin: 1.1rem 0; min-height: 90px; padding: 8px; background: var(--card);
  border: 1px dashed var(--line); border-radius: 8px; text-align: center; }
.ad-label { font-family: system-ui,sans-serif; font-size: 10px; text-transform: uppercase; letter-spacing: .08em; color: #999; margin-bottom: 6px; }
.grid2 { display: grid; gap: .9rem; }
@media (min-width: 700px) { .grid2 { grid-template-columns: 1fr 1fr; } }
.tile { display: block; padding: 1rem; background: var(--card); border: 1px solid var(--line);
  border-radius: 10px; text-decoration: none; color: inherit; }
.tile strong { display: block; color: var(--accent2); margin-bottom: .25rem; font-family: system-ui,sans-serif; }
.tile span { color: var(--muted); font-size: .92rem; }
footer.site { border-top: 1px solid var(--line); padding: 1.4rem 0 2.5rem; margin-top: 1.5rem;
  font-family: system-ui,sans-serif; font-size: .86rem; color: var(--muted); }
footer.site nav { display: flex; flex-wrap: wrap; gap: .45rem 1rem; margin-bottom: .6rem; }
ul, ol { padding-left: 1.2rem; }
table.simple { width: 100%; border-collapse: collapse; font-size: .95rem; }
table.simple th, table.simple td { border: 1px solid var(--line); padding: .45rem .55rem; text-align: left; }
table.simple th { background: #f0eee8; font-family: system-ui,sans-serif; font-size: .85rem; }
"""


def head(title: str, desc: str, path: str, extra: str = "") -> str:
    can = f"https://bpmfinder.ca{path}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="Justin Helmer">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<link rel="canonical" href="{can}">
<meta name="google-adsense-account" content="{PUB}">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={PUB}" crossorigin="anonymous"></script>
<meta property="og:type" content="website">
<meta property="og:url" content="{can}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:site_name" content="BPMfinder.ca">
<meta name="twitter:card" content="summary">
<meta name="twitter:site" content="@Excavationpro">
<meta name="theme-color" content="#f6f5f2">
<style>{CSS}</style>
{extra}
</head>
"""


def nav(active: str = "") -> str:
    links = [
        ("/", "Home"),
        ("/app.html", "BPM tool"),
        ("/guides.html", "Guides"),
        ("/how-to-find-bpm.html", "How to find BPM"),
        ("/about.html", "About"),
        ("/contact.html", "Contact"),
        ("/privacy.html", "Privacy"),
    ]
    items = []
    for href, label in links:
        cur = ' aria-current="page"' if active == href else ""
        items.append(f'<a href="{href}"{cur}>{label}</a>')
    return f"""<header class="site">
  <div class="wrap nav">
    <a class="brand" href="/">BPMfinder.ca</a>
    <nav class="navlinks" aria-label="Primary">
      {" ".join(items)}
    </nav>
  </div>
</header>
"""


def footer() -> str:
    return f"""<footer class="site">
  <div class="wrap">
    <nav aria-label="Footer">
      <a href="/">Home</a>
      <a href="/app.html">BPM tool</a>
      <a href="/guides.html">Guides</a>
      <a href="/how-to-find-bpm.html">How to find BPM</a>
      <a href="/bpm-for-djs.html">BPM for DJs</a>
      <a href="/tap-tempo-guide.html">Tap tempo</a>
      <a href="/about.html">About</a>
      <a href="/contact.html">Contact</a>
      <a href="/privacy.html">Privacy</a>
      <a href="/terms.html">Terms</a>
    </nav>
    <p>© {YEAR} Justin Helmer · BPMfinder.ca — free educational BPM guides and a free private browser tempo tool.
    Contact: <a href="mailto:excavationstation@gmail.com">excavationstation@gmail.com</a></p>
  </div>
</footer>
"""


def ad_slot() -> str:
    return f"""  <div class="ad-slot" aria-label="Advertisement">
    <div class="ad-label">Advertisement</div>
    <ins class="adsbygoogle" style="display:block" data-ad-client="{PUB}" data-ad-format="auto" data-full-width-responsive="true"></ins>
    <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
  </div>
"""


def page(title: str, desc: str, path: str, active: str, body: str, ld: str = "") -> str:
    return (
        head(title, desc, path, ld)
        + "<body>\n"
        + nav(active)
        + '<div class="wrap">\n'
        + body
        + "\n</div>\n"
        + footer()
        + "\n</body>\n</html>\n"
    )


def write(name: str, content: str) -> None:
    (ROOT / name).write_text(content, encoding="utf-8")
    print("wrote", name, len(content))


def main() -> None:
    # --- index ---
    ld = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebSite",
      "name": "BPMfinder.ca",
      "url": "https://bpmfinder.ca/",
      "description": "Free BPM guides and a private browser tempo detector.",
      "publisher": { "@id": "https://bpmfinder.ca/#org" }
    },
    {
      "@type": "Organization",
      "@id": "https://bpmfinder.ca/#org",
      "name": "BPMfinder.ca / Justin Helmer",
      "url": "https://bpmfinder.ca/",
      "email": "excavationstation@gmail.com",
      "sameAs": ["https://x.com/Excavationpro", "https://github.com/DeepSeekOracle"]
    },
    {
      "@type": "WebApplication",
      "name": "Free BPM Finder tool",
      "url": "https://bpmfinder.ca/app.html",
      "applicationCategory": "MultimediaApplication",
      "operatingSystem": "Any modern browser",
      "offers": { "@type": "Offer", "price": "0", "priceCurrency": "CAD" },
      "isAccessibleForFree": true
    }
  ]
}
</script>"""
    index_body = f"""
  <section class="hero">
    <h1>Free online BPM finder — guides and a private browser tool</h1>
    <p class="lead">
      BPMfinder.ca helps DJs, producers, dancers, and music students
      <strong>find the tempo of a song</strong> without installing software.
      Read original, practical guides on this site, then open the free tool to analyze
      MP3, WAV, or FLAC files privately in your browser.
    </p>
    <div class="cta-row">
      <a class="btn primary" href="/app.html">Open free BPM tool →</a>
      <a class="btn" href="/how-to-find-bpm.html">How to find BPM step-by-step</a>
      <a class="btn" href="/guides.html">All guides</a>
    </div>
    <p class="notice">
      <strong>Site status:</strong> Live and free. The interactive detector is at
      <a href="/app.html">bpmfinder.ca/app.html</a>. Audio is analyzed on your device — no account required.
    </p>
  </section>

{ad_slot()}

  <main>
    <article class="card" id="how-it-works">
      <h2>How free browser BPM detection works</h2>
      <p class="meta">Educational overview · Justin Helmer · Updated 2026</p>
      <p>
        Beats per minute (BPM) is how many pulses fit into one minute of music. Automatic detectors look for
        repeating energy — usually kick drums or strong transients — and estimate how often those events occur.
        On a clear electronic beat the result is often stable. On ambient music, spoken word, or swing-heavy
        performances, the detector may lock to a half-time or double-time feel.
      </p>
      <p>
        Browser tools can decode audio with the Web Audio API and run detection locally. That means unreleased
        demos do not need to be uploaded to a stranger’s server for a basic tempo check. Free tools still need
        human judgment: use half/double buttons, tap tempo, and your ears before you commit a project tempo.
      </p>
      <h3>A simple workflow that works</h3>
      <ol>
        <li>Open the free tool at <a href="/app.html">/app.html</a>.</li>
        <li>Drop a 20–40 second section with drums when possible.</li>
        <li>Read BPM and confidence.</li>
        <li>Try half or double if the groove feels wrong.</li>
        <li>Confirm with tap tempo for eight bars.</li>
        <li>Copy BPM or use delay-time notes for production.</li>
      </ol>
      <p><a href="/app.html"><strong>Launch the free BPM tool →</strong></a></p>
    </article>

    <article class="card">
      <h2>When half-time and double-time matter</h2>
      <p>
        Hip-hop and trap often sit near 70–90 or 140–180 depending on how you count. Drum-and-bass lives near
        170–180 but can feel like half when you only track the kick. Good free tools expose one-click half and
        double so you match your DAW or DJ software convention without re-running analysis.
      </p>
      <p>
        If you are building a setlist, pick one counting style and stick to it. Consistency across tracks is more
        useful than arguing about metric theory. Our <a href="/bpm-for-djs.html">BPM for DJs guide</a> explains
        how tempo notes help beatmatching without overcomplicating your night.
      </p>
    </article>

    <article class="card">
      <h2>Privacy: your audio can stay on your device</h2>
      <p>
        BPMfinder’s tool page analyzes files in the browser. That is a better default for unreleased music than
        “upload for processing” sites that store files. Always keep offline masters safe; free stream copies and
        analysis clips are derivatives, not archives.
      </p>
      <p>
        We explain cookies and advertising (including Google AdSense when approved) on our
        <a href="/privacy.html">Privacy policy</a>. Contact details are on the
        <a href="/contact.html">Contact page</a>.
      </p>
    </article>

    <article class="card">
      <h2>Guides for real studio and dance-floor questions</h2>
      <div class="grid2">
        <a class="tile" href="/how-to-find-bpm.html"><strong>How to find a song’s BPM</strong><span>Step-by-step tempo detection without software installs.</span></a>
        <a class="tile" href="/tap-tempo-guide.html"><strong>Tap tempo guide</strong><span>When automatic detection fails, train your ear with tapping.</span></a>
        <a class="tile" href="/bpm-for-djs.html"><strong>BPM for DJs</strong><span>Beatmatching, setlist planning, and confidence ranges.</span></a>
        <a class="tile" href="/delay-times-from-bpm.html"><strong>Delay times from BPM</strong><span>Convert tempo to note lengths for delays and FX.</span></a>
      </div>
    </article>

    <article class="card" id="faq">
      <h2>FAQ</h2>
      <h3>Is BPMfinder free?</h3>
      <p>Yes. Guides and the tool are free. Optional donations and ads (when approved) help with hosting.</p>
      <h3>Do I need an account?</h3>
      <p>No account is required to read guides or use the detector.</p>
      <h3>What formats work?</h3>
      <p>Common formats such as MP3, WAV, and FLAC work in modern browsers. If one fails, convert a short clip to WAV.</p>
      <h3>Where is the full tool?</h3>
      <p>The interactive app is at <a href="/app.html">https://bpmfinder.ca/app.html</a>.</p>
      <h3>Who runs this site?</h3>
      <p>BPMfinder.ca is published by Justin Helmer. See <a href="/about.html">About</a> and <a href="/contact.html">Contact</a>.</p>
      <h3>Is the site down?</h3>
      <p>No — if you are reading this page, the site is operational. If a page fails, try https://www.bpmfinder.ca/ or clear DNS cache after recent DNS changes.</p>
    </article>

    <article class="card">
      <h2>About the publisher</h2>
      <p>
        BPMfinder.ca is published by <strong>Justin Helmer</strong> (Excavationpro / LYGO). Related free projects include
        the music portal at <a href="https://asiancoastline.com/">asiancoastline.com</a> and writing at
        <a href="https://eternalhaven.ca/">eternalhaven.ca</a>. This site focuses on practical tempo education and a free tool —
        not spam, not a parked domain, and not a single-line landing page.
      </p>
    </article>
  </main>
"""
    write(
        "index.html",
        page(
            "Free BPM Finder Guide — How to Detect Song Tempo Online | BPMfinder.ca",
            "Learn how free online BPM detection works, how to check song tempo privately in your browser, and open the free BPMfinder tool. Guides for DJs, producers, and dancers by Justin Helmer.",
            "/",
            "/",
            index_body,
            ld,
        ),
    )

    # --- guides hub ---
    guides_body = f"""
  <section class="hero">
    <h1>BPM guides for real sessions</h1>
    <p class="lead">Original educational articles on tempo detection, DJ workflow, tap tempo, and delay timing. Written for humans who actually make or play music.</p>
    <div class="cta-row"><a class="btn primary" href="/app.html">Open free BPM tool</a></div>
  </section>
{ad_slot()}
  <main>
    <article class="card">
      <h2>Start here</h2>
      <div class="grid2">
        <a class="tile" href="/how-to-find-bpm.html"><strong>How to find BPM</strong><span>Complete beginner-to-studio workflow.</span></a>
        <a class="tile" href="/tap-tempo-guide.html"><strong>Tap tempo guide</strong><span>Manual tempo when algorithms disagree.</span></a>
        <a class="tile" href="/bpm-for-djs.html"><strong>BPM for DJs</strong><span>Beatmatching and set consistency.</span></a>
        <a class="tile" href="/delay-times-from-bpm.html"><strong>Delay times from BPM</strong><span>Note values for delays and sidechain feel.</span></a>
      </div>
    </article>
    <article class="card">
      <h2>What these guides are for</h2>
      <p>
        Many “BPM finder” pages are thin tool shells with almost no explanation. BPMfinder.ca pairs a free detector
        with original writing so you understand <em>why</em> a number appeared, when to ignore it, and how to use tempo
        in practice. That combination — useful tool + real educational content — is intentional.
      </p>
    </article>
  </main>
"""
    write(
        "guides.html",
        page(
            "BPM Guides — Tempo Detection Tutorials | BPMfinder.ca",
            "Free original BPM guides: how to find song tempo, tap tempo, DJ beatmatching, and delay times from BPM.",
            "/guides.html",
            "/guides.html",
            guides_body,
        ),
    )

    # --- how to find bpm ---
    how_body = f"""
  <section class="hero">
    <h1>How to find a song’s BPM (step-by-step)</h1>
    <p class="lead">A practical method to detect tempo online or in your DAW — without guessing forever.</p>
    <div class="cta-row"><a class="btn primary" href="/app.html">Try free tool</a><a class="btn" href="/guides.html">All guides</a></div>
  </section>
{ad_slot()}
  <main>
    <article class="card">
      <h2>1. Choose a clear section of the track</h2>
      <p>Pick 20–40 seconds with a steady pulse. Intros with only pads and no kick often confuse automatic detectors. Verses or drop sections with drums usually work better.</p>
      <h2>2. Prefer a clean file when you can</h2>
      <p>Streaming rips with heavy compression still work, but a short WAV export from your DAW is ideal. If the browser fails to decode a format, convert a clip to 16-bit WAV and try again.</p>
      <h2>3. Run automatic detection</h2>
      <p>On <a href="/app.html">BPMfinder’s free tool</a>, drop the file and wait for BPM and confidence. High confidence on electronic music is common. Live jazz or free-time sections may score lower — that is normal.</p>
      <h2>4. Check half and double</h2>
      <p>If the number feels twice as fast or half as slow as your body wants to move, use half/double. Your counting convention should match the software or dancers you work with.</p>
      <h2>5. Confirm with tap tempo</h2>
      <p>Tap along for eight bars. Average the taps. If tap and automatic disagree by more than a few BPM, trust the feel for performance and re-check a cleaner section for production.</p>
      <h2>6. Write the number where you will see it</h2>
      <p>Put BPM in the filename, playlist notes, or session template. Tempo only helps if you can find it again under pressure.</p>
    </article>
    <article class="card">
      <h2>Common mistakes</h2>
      <ul>
        <li>Analyzing a 3-second clip with no drums</li>
        <li>Assuming every track has one “true” BPM with no half-time option</li>
        <li>Ignoring swing and human timing on live recordings</li>
        <li>Trusting a single detector without listening</li>
      </ul>
      <p>Next: <a href="/tap-tempo-guide.html">Tap tempo guide</a> · <a href="/bpm-for-djs.html">BPM for DJs</a></p>
    </article>
  </main>
"""
    write(
        "how-to-find-bpm.html",
        page(
            "How to Find a Song’s BPM Online — Free Step-by-Step Guide | BPMfinder.ca",
            "Learn how to find a song’s BPM online: choose a clear section, run detection, check half/double tempo, and confirm with tap tempo.",
            "/how-to-find-bpm.html",
            "/how-to-find-bpm.html",
            how_body,
        ),
    )

    # --- tap tempo ---
    tap_body = f"""
  <section class="hero">
    <h1>Tap tempo guide — when automatic BPM detection fails</h1>
    <p class="lead">Your ears and hands are still the final authority. Here is how to tap tempo accurately.</p>
    <div class="cta-row"><a class="btn primary" href="/app.html">Open tool with tap tempo</a></div>
  </section>
{ad_slot()}
  <main>
    <article class="card">
      <h2>Why tap tempo still matters</h2>
      <p>
        Algorithms excel on four-on-the-floor kicks. They struggle with rubato classical, spoken word, sparse ambient,
        or tracks that change tempo mid-song. Tap tempo is the honest backup: you define the pulse you will perform to.
      </p>
      <h2>How to tap well</h2>
      <ol>
        <li>Play the track at a comfortable volume.</li>
        <li>Find a repeating accent (kick, snare, or clap).</li>
        <li>Tap on each accent for at least 8–16 hits.</li>
        <li>Ignore one-off fills; return to the main grid.</li>
        <li>If you rush, restart — averages include your mistakes.</li>
      </ol>
      <h2>Counting tips</h2>
      <p>
        Count “1-and-2-and” for eighth notes if quarters feel too slow. For trap, decide whether you are counting the
        half-time head-nod or the double-time hi-hat grid. Write which convention you used next to the BPM.
      </p>
      <h2>Practice exercise</h2>
      <p>
        Take three songs you know. Tap each twice. Compare your results to the free detector on
        <a href="/app.html">app.html</a>. When they match within 1–2 BPM, your internal clock is studio-ready.
      </p>
    </article>
  </main>
"""
    write(
        "tap-tempo-guide.html",
        page(
            "Tap Tempo Guide — Manual BPM When Detectors Disagree | BPMfinder.ca",
            "Learn accurate tap tempo technique for DJs and producers when automatic BPM detection fails or feels wrong.",
            "/tap-tempo-guide.html",
            "",
            tap_body,
        ),
    )

    # --- bpm for djs ---
    dj_body = f"""
  <section class="hero">
    <h1>BPM for DJs — beatmatching and setlist planning</h1>
    <p class="lead">Tempo is a planning tool, not a personality test. Use it to build smoother transitions.</p>
    <div class="cta-row"><a class="btn primary" href="/app.html">Detect track BPM free</a></div>
  </section>
{ad_slot()}
  <main>
    <article class="card">
      <h2>Why DJs care about BPM</h2>
      <p>
        Knowing approximate BPM helps you order a set, plan energy arcs, and decide whether a transition needs a long
        blend or a quick cut. It does not replace listening — it reduces surprises when the dancefloor is already moving.
      </p>
      <h2>A simple setlist method</h2>
      <ol>
        <li>Analyze each candidate track with a free tool or your library software.</li>
        <li>Group songs into ±3–5 BPM neighborhoods when possible.</li>
        <li>Mark half-time/double-time conventions so 87 and 174 are not mixed up.</li>
        <li>Leave intentional jumps for energy — just plan them.</li>
      </ol>
      <h2>Live vs prep</h2>
      <p>
        Prep is for map-making. Live is for reading the room. If a prepared BPM is wrong, trust the floor and re-tap.
        Free tools like BPMfinder are useful at home; on stage, practice quick tap tempo recovery.
      </p>
      <h2>Confidence ranges</h2>
      <p>
        Treat automatic BPM as a hypothesis. High confidence on club music is usually reliable. Low confidence means
        verify. See also <a href="/how-to-find-bpm.html">how to find BPM</a>.
      </p>
    </article>
  </main>
"""
    write(
        "bpm-for-djs.html",
        page(
            "BPM for DJs — Beatmatching, Setlists, and Tempo Notes | BPMfinder.ca",
            "Practical BPM advice for DJs: beatmatching neighborhoods, half-time traps, and setlist planning with free tempo tools.",
            "/bpm-for-djs.html",
            "",
            dj_body,
        ),
    )

    # --- delay times ---
    delay_body = f"""
  <section class="hero">
    <h1>Delay times from BPM — note lengths producers use</h1>
    <p class="lead">Convert tempo into milliseconds for delays, reverbs, and sidechain feel.</p>
    <div class="cta-row"><a class="btn primary" href="/app.html">Get BPM first</a></div>
  </section>
{ad_slot()}
  <main>
    <article class="card">
      <h2>The basic formula</h2>
      <p>One beat in milliseconds ≈ <strong>60000 ÷ BPM</strong>.</p>
      <p>Example: 120 BPM → 60000 ÷ 120 = <strong>500 ms</strong> per quarter note.</p>
      <table class="simple">
        <thead><tr><th>Note</th><th>Multiplier</th><th>At 120 BPM</th></tr></thead>
        <tbody>
          <tr><td>1/4</td><td>1 × beat</td><td>500 ms</td></tr>
          <tr><td>1/8</td><td>0.5 × beat</td><td>250 ms</td></tr>
          <tr><td>1/16</td><td>0.25 × beat</td><td>125 ms</td></tr>
          <tr><td>Dotted 1/8</td><td>0.75 × beat</td><td>375 ms</td></tr>
          <tr><td>Triplet 1/8</td><td>1/3 × beat</td><td>~167 ms</td></tr>
        </tbody>
      </table>
      <h2>How to use this with BPMfinder</h2>
      <ol>
        <li>Detect BPM on <a href="/app.html">app.html</a>.</li>
        <li>Compute 60000 ÷ BPM for the quarter-note length.</li>
        <li>Multiply for the note value you want.</li>
        <li>Enter that value into your delay plugin.</li>
      </ol>
      <p>
        Some tools show delay tables automatically. The math stays the same whether you calculate by hand or use a helper.
      </p>
      <h2>Musical warning</h2>
      <p>
        Perfect grid delays can sound robotic on human performances. Use tempo-synced values as a starting point, then
        nudge by ear. Production is still listening first.
      </p>
    </article>
  </main>
"""
    write(
        "delay-times-from-bpm.html",
        page(
            "Delay Times from BPM — Convert Tempo to Milliseconds | BPMfinder.ca",
            "Convert BPM to delay times in milliseconds: quarter, eighth, sixteenth, dotted, and triplet note lengths for producers.",
            "/delay-times-from-bpm.html",
            "",
            delay_body,
        ),
    )

    # --- about ---
    about_body = f"""
  <section class="hero">
    <h1>About BPMfinder.ca</h1>
    <p class="lead">A free educational BPM site and private browser tempo tool operated by Justin Helmer.</p>
  </section>
  <main>
    <article class="card">
      <h2>What we offer</h2>
      <p>
        BPMfinder.ca provides original guides about tempo detection and a free tool that analyzes audio in your browser.
        The goal is practical help for music makers — not clickbait, not malware, not a parked domain.
      </p>
      <h2>Who publishes this site</h2>
      <p>
        <strong>Justin Helmer</strong> (Excavationpro / LYGO) publishes BPMfinder.ca. Related free projects include
        music listening tools and creative experiments under the same stewardship. Contact email:
        <a href="mailto:excavationstation@gmail.com">excavationstation@gmail.com</a>.
      </p>
      <h2>Advertising</h2>
      <p>
        When Google AdSense is approved, ads may appear to support hosting. Ads must not interfere with the free tool’s
        core function. See <a href="/privacy.html">Privacy</a> and <a href="/terms.html">Terms</a>.
      </p>
      <h2>Related links</h2>
      <ul>
        <li><a href="https://asiancoastline.com/">Music portal (asiancoastline.com)</a></li>
        <li><a href="https://eternalhaven.ca/">Eternal Haven</a></li>
        <li><a href="https://www.paypal.com/paypalme/ExcavationPro">Support via PayPal</a></li>
      </ul>
    </article>
  </main>
"""
    write(
        "about.html",
        page(
            "About BPMfinder.ca — Free BPM Tool & Guides by Justin Helmer",
            "About BPMfinder.ca: free BPM guides and a private browser tempo detector published by Justin Helmer.",
            "/about.html",
            "/about.html",
            about_body,
        ),
    )

    # --- contact ---
    contact_body = f"""
  <section class="hero">
    <h1>Contact BPMfinder.ca</h1>
    <p class="lead">Questions about the free BPM tool, guides, privacy, or advertising on this site.</p>
  </section>
  <main>
    <article class="card">
      <h2>Email</h2>
      <p><a href="mailto:excavationstation@gmail.com">excavationstation@gmail.com</a></p>
      <p>Please allow a few business days for a reply. Include “BPMfinder” in the subject if your question is about this domain.</p>
      <h2>Publisher</h2>
      <p>Justin Helmer · Canada</p>
      <h2>Support free tools</h2>
      <p>Optional: <a href="https://www.paypal.com/paypalme/ExcavationPro">PayPal.me/ExcavationPro</a></p>
      <h2>Policy pages</h2>
      <p><a href="/privacy.html">Privacy policy</a> · <a href="/terms.html">Terms of use</a></p>
    </article>
  </main>
"""
    write(
        "contact.html",
        page(
            "Contact — BPMfinder.ca",
            "Contact Justin Helmer about BPMfinder.ca free BPM tool, guides, privacy, or site issues.",
            "/contact.html",
            "/contact.html",
            contact_body,
        ),
    )

    # --- privacy expanded ---
    privacy_body = f"""
  <section class="hero">
    <h1>Privacy Policy — BPMfinder.ca</h1>
    <p class="meta">Last updated: 2026-08-09 · Publisher: Justin Helmer</p>
  </section>
  <main>
    <article class="card">
      <h2>Summary</h2>
      <p>BPMfinder.ca provides free educational content and a free browser-based BPM tool. We aim to keep analysis private by default and to be transparent about advertising cookies if AdSense is active.</p>
      <h2>Audio processing</h2>
      <p>When you use the tool at <a href="/app.html">app.html</a>, audio you select is processed <strong>locally in your browser</strong> using web technologies such as the Web Audio API. We do not require an account. The default tool is designed so files are not uploaded to our servers solely for BPM detection.</p>
      <h2>Logs and hosting</h2>
      <p>Like most websites, hosting providers and CDNs (including GitHub Pages infrastructure) may process standard technical logs such as IP address, user agent, and requested URLs for security and reliability.</p>
      <h2>Cookies and advertising</h2>
      <p>We may use cookies and similar technologies for essential site function and, when approved, Google AdSense advertising (publisher ID <code>{PUB}</code>). Google and partners may collect device and browser information according to their policies.</p>
      <p>Google resources: <a href="https://policies.google.com/technologies/ads">Advertising</a> · <a href="https://policies.google.com/privacy">Privacy</a> · <a href="https://adssettings.google.com/">Ad Settings</a></p>
      <h2>Children</h2>
      <p>This site is a general music education tool. We do not knowingly collect personal information from children for accounts, because no account system is required.</p>
      <h2>Contact</h2>
      <p>Privacy questions: <a href="mailto:excavationstation@gmail.com">excavationstation@gmail.com</a> · <a href="/contact.html">Contact page</a></p>
      <p><a href="/">Home</a> · <a href="/terms.html">Terms</a></p>
    </article>
  </main>
"""
    write(
        "privacy.html",
        page(
            "Privacy Policy — BPMfinder.ca",
            "Privacy policy for BPMfinder.ca: local browser BPM analysis, cookies, Google AdSense, and contact details.",
            "/privacy.html",
            "/privacy.html",
            privacy_body,
        ),
    )

    # --- terms ---
    terms_body = f"""
  <section class="hero">
    <h1>Terms of use — BPMfinder.ca</h1>
    <p class="meta">Last updated: 2026-08-09</p>
  </section>
  <main>
    <article class="card">
      <h2>Acceptance</h2>
      <p>By using BPMfinder.ca you agree to these terms. If you do not agree, do not use the site.</p>
      <h2>Service description</h2>
      <p>We provide free educational articles and a free browser-based tempo estimation tool. Results are estimates and may be wrong. Always verify critical tempos with your ears and professional tools when needed.</p>
      <h2>No warranty</h2>
      <p>The site is provided “as is” without warranties of accuracy, uptime, or fitness for a particular purpose.</p>
      <h2>Acceptable use</h2>
      <p>Do not abuse the site, attempt to disrupt service, scrape in a way that harms availability, or use the service for unlawful purposes.</p>
      <h2>Intellectual property</h2>
      <p>Site text and branding are owned by Justin Helmer unless otherwise noted. You retain rights to your own audio files; we do not claim ownership of music you analyze locally.</p>
      <h2>Contact</h2>
      <p><a href="mailto:excavationstation@gmail.com">excavationstation@gmail.com</a></p>
      <p><a href="/privacy.html">Privacy policy</a></p>
    </article>
  </main>
"""
    write(
        "terms.html",
        page(
            "Terms of Use — BPMfinder.ca",
            "Terms of use for BPMfinder.ca free BPM tool and educational guides.",
            "/terms.html",
            "",
            terms_body,
        ),
    )

    # ads / robots / sitemap
    (ROOT / "ads.txt").write_text(
        "google.com, pub-0646320966060599, DIRECT, f08c47fec0942fa0\n",
        encoding="utf-8",
    )
    (ROOT / "robots.txt").write_text(
        """User-agent: *
Allow: /

Sitemap: https://bpmfinder.ca/sitemap.xml
""",
        encoding="utf-8",
    )
    urls = [
        ("https://bpmfinder.ca/", "1.0"),
        ("https://bpmfinder.ca/app.html", "0.95"),
        ("https://bpmfinder.ca/guides.html", "0.9"),
        ("https://bpmfinder.ca/how-to-find-bpm.html", "0.9"),
        ("https://bpmfinder.ca/tap-tempo-guide.html", "0.85"),
        ("https://bpmfinder.ca/bpm-for-djs.html", "0.85"),
        ("https://bpmfinder.ca/delay-times-from-bpm.html", "0.85"),
        ("https://bpmfinder.ca/about.html", "0.7"),
        ("https://bpmfinder.ca/contact.html", "0.7"),
        ("https://bpmfinder.ca/privacy.html", "0.5"),
        ("https://bpmfinder.ca/terms.html", "0.5"),
    ]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, pri in urls:
        sm.append(
            f"  <url><loc>{loc}</loc><changefreq>weekly</changefreq><priority>{pri}</priority></url>"
        )
    sm.append("</urlset>\n")
    (ROOT / "sitemap.xml").write_text("\n".join(sm), encoding="utf-8")

    # light touch on app.html footer: ensure privacy/contact links if missing
    app = ROOT / "app.html"
    if app.is_file():
        t = app.read_text(encoding="utf-8")
        if 'href="/contact.html"' not in t and "contact.html" not in t:
            t = t.replace(
                '[Privacy policy](/privacy.html)',
                '[Privacy policy](/privacy.html) · [Contact](/contact.html) · [About](/about.html) · [Guides](/guides.html)',
            )
            # also plain html variants
            t = t.replace(
                'href="/privacy.html">Privacy',
                'href="/privacy.html">Privacy</a> · <a href="/contact.html">Contact</a> · <a href="/about.html">About</a> · <a href="/guides.html">Guides',
            )
        if "google-adsense-account" not in t:
            t = t.replace(
                "<head>",
                f'<head>\n<meta name="google-adsense-account" content="{PUB}">',
                1,
            )
        app.write_text(t, encoding="utf-8")
        print("touched app.html links")

    print("OK — content expanded for AdSense")


if __name__ == "__main__":
    main()
