"""Content bodies for bpmfinder.ca. Imported by build_articles.py."""

PUB = "ca-pub-0646320966060599"
AD = """<div class="ad-slot" aria-label="Advertisement">
  <div class="ad-label">Advertisement</div>
  <ins class="adsbygoogle" style="display:block" data-ad-client="{pub}" data-ad-format="auto" data-full-width-responsive="true"></ins>
  <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
</div>""".format(pub=PUB)

RELATED = {
    "how-to-find-bpm.html": [
        ("/tap-tempo-guide.html", "Tap tempo guide"),
        ("/bpm-for-djs.html", "BPM for DJs"),
        ("/delay-times-from-bpm.html", "Delay times from BPM"),
    ],
    "bpm-for-djs.html": [
        ("/how-to-find-bpm.html", "How to find a song&rsquo;s BPM"),
        ("/half-time-double-time.html", "Half-time and double-time"),
        ("/delay-times-from-bpm.html", "Delay times from BPM"),
    ],
    "delay-times-from-bpm.html": [
        ("/how-to-find-bpm.html", "How to find a song&rsquo;s BPM"),
        ("/bpm-for-djs.html", "BPM for DJs"),
        ("/tap-tempo-guide.html", "Tap tempo guide"),
    ],
    "tap-tempo-guide.html": [
        ("/how-to-find-bpm.html", "How to find a song&rsquo;s BPM"),
        ("/half-time-double-time.html", "Half-time and double-time"),
        ("/bpm-for-djs.html", "BPM for DJs"),
    ],
    "half-time-double-time.html": [
        ("/how-to-find-bpm.html", "How to find a song&rsquo;s BPM"),
        ("/bpm-for-djs.html", "BPM for DJs"),
        ("/tap-tempo-guide.html", "Tap tempo guide"),
    ],
    "bpm-for-running.html": [
        ("/how-to-find-bpm.html", "How to find a song&rsquo;s BPM"),
        ("/bpm-for-djs.html", "BPM for DJs"),
        ("/tap-tempo-guide.html", "Tap tempo guide"),
    ],
    "bpm-detection-accuracy.html": [
        ("/how-to-find-bpm.html", "How to find a song&rsquo;s BPM"),
        ("/tap-tempo-guide.html", "Tap tempo guide"),
        ("/bpm-for-djs.html", "BPM for DJs"),
    ],
}


def related(slug):
    items = RELATED.get(slug, [])
    if not items:
        return ""
    links = "".join(f'<li><a href="{href}">{label}</a></li>' for href, label in items)
    return f'<div class="related"><h2>Related guides</h2><ul>{links}</ul></div>'


AUTHOR = """<div class="author-box">
  <strong>Justin Helmer</strong> publishes BPMfinder.ca and records as
  <a href="https://excavationpro.ca/">Excavationpro</a>. He writes about tempo, music tools, and the
  practical side of making records without a label. <a href="/about.html">About the site</a>.
</div>"""


PAGES = {}

# ---------------------------------------------------------------- how to find
PAGES["how-to-find-bpm.html"] = dict(
    title="How to Find a Song&rsquo;s BPM (Step-by-Step) | BPMfinder.ca",
    desc="A practical workflow for finding a song&rsquo;s BPM: choose the right section, read confidence, check half/double, and confirm with tap tempo.",
    path="/how-to-find-bpm.html",
    active="guides",
    h1="How to find a song&rsquo;s BPM (step-by-step)",
    lead="You do not need a DAW, an account, or an upload to find a song&rsquo;s tempo. You need a clean section of audio, a detector you trust, and one habit: check half-time and double-time before you write the number down.",
    minutes="8 min read",
    updated="2026-10-20",
    tags=["tempo", "workflow", "beginners"],
    body=f"""
<article class="card">
  <h2>1. What BPM actually measures</h2>
  <p>Beats per minute is a count, not a genre. At 120 BPM, four beats pass every two seconds, so one beat lasts 500 milliseconds. At 90 BPM, a beat lasts about 667 milliseconds. That number is useful because it tells a DAW where to put the grid, tells a DJ how much pitch correction a blend needs, and tells a dancer how fast the pulse is.</p>
  <p>It does not tell you how the track feels. A 70 BPM trap record and a 140 BPM house record can share a pulse; the difference is where the snare lands and how the subdivisions are played. This is why two people can disagree about the &ldquo;real&rdquo; BPM of the same song and both be counting correctly. Pick a convention, write it down, and stay consistent across your project.</p>
  <h2>2. Before you analyze: choose the right section</h2>
  <p>Most bad BPM readings are caused by a bad input, not a bad detector.</p>
  <ul>
    <li><strong>Use 20&ndash;40 seconds with a steady pulse.</strong> A verse, a drop, or a chorus with drums is ideal.</li>
    <li><strong>Avoid intros, outros, and breakdowns.</strong> Pads, risers, and spoken intros give the detector very little to lock onto.</li>
    <li><strong>Use a file you own.</strong> MP3, WAV, and FLAC work in modern browsers. Streaming-service files are usually protected, so export or record a clip you have the rights to use.</li>
    <li><strong>Do not use a clip shorter than about ten seconds.</strong> There are not enough repetitions for a stable estimate.</li>
  </ul>
  <p>If the song changes tempo, analyze the section you will actually use. A single BPM for a track with a ritardando or a half-time bridge is a fiction; note the tempo of each section instead.</p>
</article>
{AD}
<article class="card">
  <h2>3. Run the detector and read the confidence</h2>
  <p>Open the <a href="/app.html">free BPM tool</a>, drop the file, and wait for the result. The tool analyzes the audio in your browser; it does not require an account, and the file is not uploaded to a server for tempo detection.</p>
  <p>You will get two numbers: BPM and a confidence score. Treat confidence as a hint, not a grade. A high score on a four-on-the-floor house track is normal. A lower score on live jazz, a rubato piano intro, or a field recording is also normal. The question is not &ldquo;is the score high?&rdquo; but &ldquo;does the number match the pulse I hear?&rdquo; Play the track and count along for eight bars. If your count and the detector agree, move on. If they do not, do the next step before you touch the project tempo.</p>
<figure class="figure">
  <img src="/assets/screenshots/bpm-result-128.png" alt="BPMfinder showing 128.0 BPM and full confidence for a 128 BPM click track" width="600" height="640" loading="lazy">
  <figcaption>The tool reporting 128.0 BPM and full confidence for a generated click track. The confidence bar reflects how tightly the detected beats cluster, not whether the count matches your ear. Screenshot: BPMfinder.ca.</figcaption>
</figure>
  <h2>4. Check half-time and double-time before you trust it</h2>
  <p>Half-time and double-time are the most common source of wrong BPM values, and the easiest to fix. A track that feels like 70 BPM may be counted at 140. A drum-and-bass tune at 174 may feel like 87 if you only follow the kick. A boom-bap loop at 90 may read as 180 if the detector locks to the hi-hats. None of those readings is &ldquo;broken&rdquo; &mdash; they are different counting levels of the same pulse.</p>
  <p>Ask yourself: <strong>where do the snare and the main backbeat land?</strong> If the snare hits on beats two and four of a slow count, the slow number is usually the useful one. If the energy is carried by fast subdivisions, the double may be the better session tempo. Write down which convention you chose. Changing it later is cheap; discovering it after you have tracked eight bars is not. The <a href="/half-time-double-time.html">half-time and double-time guide</a> goes deeper, and the <a href="/bpm-for-djs.html">BPM for DJs guide</a> covers beatmatching.</p>
  <h2>5. Confirm with tap tempo</h2>
  <p>Tap tempo is the simplest sanity check ever invented. Tap along with the track for eight bars &mdash; not two, not four. Eight bars gives you enough taps to average out a nervous finger. Compare the average with the detector. If they are within a BPM or two, you are done. If they are far apart, go back to a cleaner section and repeat both steps.</p>
  <p>Do not tap the hi-hat if you want the song&rsquo;s main tempo. Tap the pulse you would clap to. That is the number a drummer, a DJ, or a DAW grid will agree with.</p>
</article>
<article class="card">
  <h2>6. When automatic detection fails</h2>
  <p>Some material is genuinely hard, and no detector should pretend otherwise.</p>
  <ul>
    <li><strong>Rubato and live drums.</strong> Tempo breathes. A single number may be wrong for half the track. Note a range, or analyze a steady section.</li>
    <li><strong>Ambient, drone, and spoken word.</strong> There may be no stable beat to find. A low confidence score is the honest answer.</li>
    <li><strong>Short clips and fades.</strong> The detector needs repetition; a five-second intro may not contain enough.</li>
    <li><strong>Heavily compressed or clipped audio.</strong> Transients get smeared, and the detector may lock onto the wrong pulse. A cleaner export usually fixes it.</li>
    <li><strong>Tempo changes.</strong> Analyze each section separately. Do not average a 90 BPM verse and a 140 BPM drop into one meaningless number.</li>
  </ul>
  <p>If the result still feels wrong, trust your ears and use tap tempo. The tool is a second opinion, not a judge. Our <a href="/bpm-detection-accuracy.html">measured accuracy test</a> shows where the detector is strong and where it is not.</p>
  <h2>7. Record the result where you will use it</h2>
  <p>A BPM you cannot find again is a BPM you will re-detect. Put it where the work happens:</p>
  <ul>
    <li>In the DAW session tempo, before you record MIDI or loop-based audio.</li>
    <li>In the filename or the playlist notes, especially for a DJ set.</li>
    <li>In the track metadata or a simple session note, with the half/double convention you chose.</li>
    <li>In the arrangement notes if the song changes tempo.</li>
  </ul>
  <p>For a DJ set, BPM belongs next to key and energy, not in a separate spreadsheet you will forget to open. For a production session, it belongs in the project template so every collaborator starts on the same grid.</p>
  <h2>Common mistakes</h2>
  <ul>
    <li>Analyzing a three-second clip with no drums.</li>
    <li>Assuming every track has one &ldquo;true&rdquo; BPM with no half-time option.</li>
    <li>Ignoring swing and human timing on live recordings.</li>
    <li>Trusting a single detector pass without listening.</li>
    <li>Writing the number down without noting which count you used.</li>
  </ul>
  <h2>8. A five-minute workflow</h2>
  <ol>
    <li>Pick a 20&ndash;40 second section with steady drums.</li>
    <li>Drop it into the <a href="/app.html">BPM tool</a>.</li>
    <li>Read BPM and confidence.</li>
    <li>Check half-time and double-time against the snare.</li>
    <li>Tap eight bars and compare.</li>
    <li>Write the number and the counting convention where you will use it.</li>
  </ol>
  <p>That is the whole job. The rest is practice.</p>
</article>
<article class="card faq">
  <h2>FAQ</h2>
  <h3>Why does the tool say 140 when the song feels like 70?</h3>
  <p>Both can be correct. The detector may be counting double-time subdivisions. Check where the snare and backbeat land, then choose the count that matches how you will use the tempo.</p>
  <h3>What is a good confidence score?</h3>
  <p>There is no universal threshold. High confidence on a clear electronic beat is expected; lower confidence on live, rubato, or ambient material is normal. Use the score to decide whether to double-check, not to decide whether the result is &ldquo;allowed.&rdquo;</p>
  <h3>Does the tool upload my audio?</h3>
  <p>No. The analysis runs in your browser. The <a href="/privacy.html">privacy policy</a> explains what the hosting and advertising layers may log.</p>
  <h3>Can I find BPM from a Spotify or Apple Music link?</h3>
  <p>Not reliably. Streaming files are usually protected. Use a file you own or a short clip you have the rights to use.</p>
  <h3>What formats work?</h3>
  <p>MP3, WAV, and FLAC in current browsers. If a file will not decode, export a short 16-bit WAV clip and try again.</p>
  <h3>What if the song changes tempo?</h3>
  <p>Analyze each section separately and write down the tempo for each. A single number is only useful if the pulse is stable.</p>
</article>
{related("how-to-find-bpm.html")}
<article class="card">
  <h2>Practice listening</h2>
  <p>If you want something to test the workflow on, the free player at <a href="https://asiancoastline.com/">asiancoastline.com</a> streams the Excavationpro catalog without an account. Pick a track, run the BPM check, then listen for where the snare actually lands.</p>
</article>
{AUTHOR}
""",
    faqs=[
        ("Why does the tool say 140 when the song feels like 70?", "Both can be correct. The detector may be counting double-time subdivisions. Check where the snare and backbeat land, then choose the count that matches how you will use the tempo."),
        ("What is a good confidence score?", "There is no universal threshold. High confidence on a clear electronic beat is expected; lower confidence on live, rubato, or ambient material is normal. Use the score to decide whether to double-check."),
        ("Does the tool upload my audio?", "No. The analysis runs in the browser; the file is not uploaded for tempo detection."),
        ("Can I find BPM from a Spotify or Apple Music link?", "Not reliably. Streaming files are usually protected; use a file you own or a clip you have the rights to use."),
        ("What formats work?", "MP3, WAV, and FLAC in current browsers. If a file will not decode, export a short 16-bit WAV clip."),
        ("What if the song changes tempo?", "Analyze each section separately and record the tempo for each section."),
    ],
    howto=[
        ("Pick a 20-40 second section with steady drums.", "Use a verse, drop, or chorus. Avoid intros and breakdowns with no clear pulse."),
        ("Run the detector.", "Drop the file into the free BPM tool and read the BPM and confidence."),
        ("Check half-time and double-time.", "Compare the reported number with where the snare and backbeat land."),
        ("Confirm with tap tempo.", "Tap along for eight bars and compare the average with the detector."),
        ("Record the tempo.", "Write the BPM and the counting convention into the DAW session, filename, or playlist notes."),
    ],
)

# ---------------------------------------------------------------- bpm for DJs
PAGES["bpm-for-djs.html"] = dict(
    title="BPM for DJs: Beatmatching, Phrasing & Set Planning | BPMfinder.ca",
    desc="How working DJs use BPM for beatmatching, phrasing, and set energy, with pitch-fader math, genre ranges, and a 20-minute practice drill.",
    path="/bpm-for-djs.html",
    active="guides",
    h1="BPM for DJs: beatmatching, phrasing, and set planning",
    lead="BPM is not a genre label and it is not a score. It is a planning number: how much pitch correction a blend needs, where a phrase starts, and how the energy moves across a set.",
    minutes="7 min read",
    updated="2026-10-20",
    tags=["DJ", "beatmatching", "set planning"],
    body=f"""
<article class="card">
  <h2>Why DJs care about BPM</h2>
  <p>Two records can only blend cleanly when their pulses agree. If one is at 124 BPM and the other at 128, you either move one with the pitch fader or you find a transition that does not require a sustained blend. Knowing the numbers before you load the next track turns a guess into a decision.</p>
  <p>BPM also shapes the emotional arc of a set. A warm-up at 118&ndash;122 feels different from a peak-time run at 128&ndash;134, even when the records share a genre. The number is not the energy, but it is one of the levers that controls it.</p>
  <h2>The pitch-fader math</h2>
  <p>Pitch correction is a percentage, not a BPM difference. To move a track from its original tempo to a target tempo:</p>
  <p><strong>percent change = ((target / original) &minus; 1) &times; 100</strong></p>
  <ul>
    <li>124 &rarr; 128 BPM: <strong>+3.2%</strong></li>
    <li>128 &rarr; 124 BPM: <strong>&minus;3.1%</strong></li>
    <li>120 &rarr; 126 BPM: <strong>+5.0%</strong></li>
    <li>174 &rarr; 87 BPM: <strong>&minus;50%</strong> (a half-time blend, not a small nudge)</li>
  </ul>
  <p>On a CDJ or controller, a 6% range is often enough for house and techno. A 10% or 16% range gives more room but can make vocals sound unnatural. If the correction is large, consider a half-time or double-time transition instead of forcing the pitch.</p>
</article>
{AD}
<article class="card">
  <h2>Phrasing: where the blend actually lands</h2>
  <p>Most dance music is built in 8-bar and 16-bar phrases. A blend that starts in the middle of a phrase can sound like two songs colliding even when the BPM is perfect. Count from a clear downbeat, then start the incoming track on a phrase boundary &mdash; usually the first beat of an 8 or 16-bar block.</p>
  <p>A practical habit: cue the incoming track four bars before the phrase you want, then bring it in on the downbeat. If the outgoing track has a breakdown, use that space to swap the low end rather than layering two kicks.</p>
  <h2>Set energy is not the same as BPM</h2>
  <p>A 128 BPM record with a sparse arrangement can feel calmer than a 122 BPM record with a busy vocal and a hard kick. Plan the set with three columns: BPM, key, and energy. Move one variable at a time. If you jump 10 BPM and 10 energy points at once, the room feels the jump even if the blend is technically clean.</p>
  <h2>Common tempo ranges</h2>
  <p>These are conventions, not rules. Use them as a starting point, then trust the record. For a longer producer-facing read on browser tempo detection, see <a href="https://deepseekoracle.com/articles/free-bpm-detection-guide.html">DeepSeek Oracle&rsquo;s BPM detection guide</a>.</p>
  <div class="table-wrap"><table class="simple">
    <thead><tr><th>Style</th><th>Typical BPM</th><th>Note</th></tr></thead>
    <tbody>
      <tr><td>Hip-hop / boom-bap</td><td>70&ndash;100</td><td>Often counted at double time for DJ tools</td></tr>
      <tr><td>House</td><td>118&ndash;128</td><td>Deep house sits lower; tech house sits higher</td></tr>
      <tr><td>Techno</td><td>125&ndash;150</td><td>Hard techno can push beyond 150</td></tr>
      <tr><td>Disco / funk</td><td>110&ndash;125</td><td>Live drums may drift a few BPM</td></tr>
      <tr><td>Drum &amp; bass</td><td>160&ndash;180</td><td>Often felt as half-time at 80&ndash;90</td></tr>
      <tr><td>Dubstep / halftime</td><td>140 (felt at 70)</td><td>The half-time count is the useful one</td></tr>
    </tbody>
  </table></div>
  <h2>A simple setlist method</h2>
  <p>Write three columns: BPM, key, and energy. Sort by energy first, then by BPM inside each block. A set that moves from 120 to 126 across ten tracks feels like a build; a set that jumps 120, 128, 122, 130 feels restless even when every individual blend is clean.</p>
  <p>Leave one or two slots open. The room will tell you whether the next block should be faster or deeper, and a fixed list with no room for that decision is a playlist, not a set.</p>
  <h2>A 20-minute practice drill</h2>
  <ol>
    <li>Pick five tracks between 120 and 128 BPM.</li>
    <li>Write the BPM and key of each one before you load it.</li>
    <li>Blend two tracks using only the pitch fader; note the percentage.</li>
    <li>Repeat with a 4-bar blend, then an 8-bar blend.</li>
    <li>Finish with one half-time transition (for example 174 &rarr; 87).</li>
  </ol>
  <p>The goal is not a perfect mix. It is knowing what a 3% correction sounds like before the room is full.</p>
</article>
<article class="card faq">
  <h2>FAQ</h2>
  <h3>Should I beatmatch by ear or by BPM?</h3>
  <p>Both. BPM tells you where to start; your ears tell you whether the blend actually locks. Use the number to narrow the search, then trust the transient.</p>
  <h3>Is a 6% pitch range enough?</h3>
  <p>For most house and techno, yes. If you regularly move between 120 and 128, a 6% range covers it with room to spare. Larger jumps need a different transition or a wider range.</p>
  <h3>Why do some tracks sound faster than their BPM?</h3>
  <p>Subdivision density, vocal energy, and arrangement matter. A busy 124 can feel faster than a sparse 130. Plan energy separately from tempo.</p>
  <h3>What about harmonic mixing?</h3>
  <p>Key matters, but it is a separate axis from BPM. Use a key tag or Camelot notation alongside the tempo, and do not force a blend that clashes harmonically just because the BPM matches.</p>
</article>
<article class="card">
  <h2>Live vs preparation</h2>
  <p>Preparation is where BPM earns its keep: tagging, cue points, phrase marks, and a set arc. Live, the number should recede. If you are staring at a BPM readout while the room is moving, you are using the tool too late. Know the range of the next three tracks, then listen.</p>
  <p>Confidence ranges help here. A track you have tested at 124&ndash;126 can take a small nudge; a track with a live drummer and a drifting tempo should be left alone or blended at a phrase boundary. Write the range, not a false decimal.</p>
</article>
<article class="card">
  <h2>Preparing a set file before the gig</h2>
  <p>A BPM column is only useful if the rest of the file is ready. Before a set, export a simple list with four fields: title, BPM, key, and a one-line energy note. The note can be as short as &ldquo;warm-up&rdquo;, &ldquo;vocal peak&rdquo;, or &ldquo;close&rdquo;. When you are loading tracks in a dark room, that line is faster to read than a waveform.</p>
  <p>Set cue points at the first downbeat and at the start of the phrase you plan to mix. If a track has a long intro, cue the first useful bar rather than the first sound. If it has a cold start, mark the drop. The goal is to remove decisions from the moment when you are already listening to the room.</p>
  <p>Check the gain before the set, not during it. A track that is 3 dB louder than the rest will feel like an energy jump even if the BPM is identical. Match loudness in rehearsal, then use the energy note for the arrangement.</p>
  <h2>Three-deck thinking</h2>
  <p>With three decks, BPM becomes a scheduling problem. You can hold a steady pulse on one deck, bring a second in for a phrase, and use the third for a short vocal or percussion layer. Write the BPM of every layer, not just the main track. A 128 BPM loop against a 124 BPM track is a 3.2% correction; against a 140 BPM track it is a different transition entirely.</p>
  <p>If you use sync, the BPM number still matters because it tells you whether the sync result is plausible. A synced 87 against a 174 track is a half-time relationship, not an error. A synced 174 against a 128 track is a jump; decide whether that is the effect you want.</p>
</article>
{related("bpm-for-djs.html")}
{AUTHOR}
""",
    faqs=[
        ("Should I beatmatch by ear or by BPM?", "Both. BPM tells you where to start; your ears tell you whether the blend locks."),
        ("Is a 6% pitch range enough?", "For most house and techno, yes. A 6% range covers 120-128 with room to spare."),
        ("Why do some tracks sound faster than their BPM?", "Subdivision density, vocal energy, and arrangement matter. Plan energy separately from tempo."),
        ("What about harmonic mixing?", "Key is a separate axis from BPM. Use a key tag alongside tempo and do not force a clash."),
    ],
)

# ---------------------------------------------------------------- delay times
def delay_rows():
    rows = []
    for bpm in (60, 70, 80, 90, 100, 110, 120, 128, 140, 150, 160, 174, 180):
        q = 60000 / bpm
        rows.append(
            f"<tr><td>{bpm}</td><td>{q:.0f}</td><td>{q/2:.0f}</td><td>{q*0.75:.0f}</td><td>{q/4:.0f}</td><td>{q/3:.0f}</td></tr>"
        )
    return "\n".join(rows)


PAGES["delay-times-from-bpm.html"] = dict(
    title="Delay Times from BPM: Note-Value Chart & Formula | BPMfinder.ca",
    desc="Convert BPM to delay and reverb times with the 60000/BPM formula, a full note-value table, and practical examples for 90, 120, 128, 140, and 174 BPM.",
    path="/delay-times-from-bpm.html",
    active="guides",
    h1="Delay times from BPM: the note-value chart",
    lead="Every tempo-synced delay is a division of the beat. Once you know the BPM, the milliseconds are arithmetic &mdash; and the arithmetic is the difference between a delay that sits in the groove and one that smears it.",
    minutes="7 min read",
    updated="2026-10-20",
    tags=["delay", "reverb", "mixing"],
    body=f"""
<article class="card">
  <h2>The basic formula</h2>
  <p>One beat in milliseconds is <strong>60,000 &divide; BPM</strong>. At 120 BPM, one beat is 500 ms. A quarter-note delay is 500 ms; an eighth-note delay is 250 ms; a sixteenth-note delay is 125 ms. A dotted eighth is 1.5 times the eighth (375 ms at 120), and a triplet is two-thirds of the straight value.</p>
  <p>This is the same math a DAW uses when you set a delay to &ldquo;1/8 dotted&rdquo; and change the project tempo. Doing it by hand is useful when you are working outside a DAW, matching a hardware pedal, or checking why a plugin&rsquo;s sync feels wrong.</p>
  <h2>Note values at common tempos</h2>
  <div class="table-wrap"><table class="simple">
    <thead><tr><th>BPM</th><th>Quarter</th><th>Eighth</th><th>Dotted 8th</th><th>16th</th><th>Triplet 8th</th></tr></thead>
    <tbody>
{delay_rows()}
    </tbody>
  </table></div>
  <p>All values are milliseconds, rounded to the nearest millisecond. Use the table as a starting point, then fine-tune by ear; a few milliseconds can change the feel of a rhythmic delay.</p>
  <p>If you do not want to do the arithmetic, the <a href="/app.html">BPM tool</a> shows delay times for the tempo it detects, including the note values above. The table is still useful when you are working from a known BPM without a file.</p>
  <p><strong>Musical warning:</strong> a mathematically correct delay can still be wrong for the arrangement. A delay that lands exactly on the grid may fight a swing feel, and a delay that is slightly late may sit better than a perfect eighth. The formula gives you the target; your ears decide whether to use it.</p>
</article>
{AD}
<article class="card">
  <h2>Worked examples</h2>
  <p><strong>120 BPM:</strong> quarter 500 ms, eighth 250 ms, dotted eighth 375 ms, sixteenth 125 ms. A 250 ms ping-pong delay sits on the eighth note; a 375 ms delay pushes against the beat in that familiar dotted-eighth way.</p>
  <p><strong>128 BPM:</strong> quarter 469 ms, eighth 234 ms, dotted eighth 352 ms, sixteenth 117 ms. This is the house tempo where a 3/16 delay often feels bigger than a straight eighth.</p>
  <p><strong>140 BPM:</strong> quarter 429 ms, eighth 214 ms, dotted eighth 321 ms, sixteenth 107 ms. At this tempo, short delays start to sound like doubling rather than echo; filter them if the mix gets crowded.</p>
  <p><strong>174 BPM:</strong> quarter 345 ms, eighth 172 ms, dotted eighth 259 ms, sixteenth 86 ms. Drum-and-bass delays often work best at the eighth or dotted eighth, with the feedback low enough to avoid clutter.</p>
  <h2>Ping-pong, dotted eighth, and pre-delay</h2>
  <p>A ping-pong delay alternates left and right. It widens a mono source without making it louder, which is why it is common on vocals and plucks. The timing is still the note value; the stereo pattern is a separate choice.</p>
  <p>Reverb pre-delay is not the same as a delay, but the math helps. A short pre-delay (20&ndash;60 ms) keeps a vocal from sounding glued to the reverb. A tempo-synced pre-delay can be useful on percussive material, but it is usually better to set it by feel.</p>
  <h2>Tempo-synced vs manual</h2>
  <p>If the DAW session has a stable tempo, use tempo sync. If the track drifts, if you are working with live drums, or if you want a delay that deliberately ignores the grid, set the time manually. Manual delays are also useful when a plugin&rsquo;s sync implementation rounds in a way you do not like.</p>
  <h2>Common mistakes</h2>
  <ul>
    <li>Using a quarter-note delay on a busy arrangement; it fights the vocal.</li>
    <li>Setting feedback too high, so the delay outlasts the phrase.</li>
    <li>Forgetting to high-pass the delay return; low-end repeats muddy the kick.</li>
    <li>Assuming every genre wants a dotted eighth; sometimes a straight eighth is cleaner.</li>
    <li>Changing the project tempo after printing a delay without re-checking the time.</li>
  </ul>
</article>
<article class="card faq">
  <h2>FAQ</h2>
  <h3>What is the formula for delay time?</h3>
  <p>60,000 divided by BPM gives one beat in milliseconds. Divide or multiply for the note value you want.</p>
  <h3>What is a dotted eighth delay?</h3>
  <p>An eighth note multiplied by 1.5. At 120 BPM, the eighth is 250 ms, so the dotted eighth is 375 ms.</p>
  <h3>Should delay be synced to the grid?</h3>
  <p>For electronic music with a stable tempo, usually yes. For live or drifting material, set it by ear.</p>
  <h3>Why does my delay sound out of time?</h3>
  <p>Check whether the plugin is using the project tempo, whether the note value is straight or dotted, and whether the track has a tempo change.</p>
</article>
<article class="card">
  <h2>Delay or reverb: which one do you need?</h2>
  <p>A delay repeats the signal; a reverb simulates a space. If you want a rhythmic answer to a vocal line, use a delay. If you want the source to sit in a room, use a reverb. The note-value table is for the delay; reverb uses time in a different way, although pre-delay can be tempo-aware.</p>
  <p>A common combination is a short room reverb for glue and a tempo-synced delay for movement. Put the reverb first in the chain and the delay after it, then high-pass the delay return so the low end does not turn into mud. If the mix already has a lot of sustain, a shorter delay with low feedback will be more useful than a long wash.</p>
  <h2>A workflow for dialing a delay</h2>
  <ol>
    <li>Set the note value from the table (start with the eighth or dotted eighth).</li>
    <li>Set feedback low &mdash; one or two repeats is enough for most vocals.</li>
    <li>High-pass the return around 300&ndash;500 Hz so it does not crowd the kick.</li>
    <li>Automate the send rather than the return; let the delay appear only where the arrangement has space.</li>
    <li>Check the mix in mono; a wide ping-pong can disappear or dominate when summed.</li>
  </ol>
  <p>If the delay feels late, shorten it by a few milliseconds rather than changing the note value. If it feels cluttered, reduce feedback before reducing the level; the repeats are usually the problem, not the first echo.</p>
</article>
{related("delay-times-from-bpm.html")}
{AUTHOR}
""",
    faqs=[
        ("What is the formula for delay time?", "60,000 divided by BPM gives one beat in milliseconds. Divide or multiply for the note value."),
        ("What is a dotted eighth delay?", "An eighth note multiplied by 1.5. At 120 BPM the eighth is 250 ms, so the dotted eighth is 375 ms."),
        ("Should delay be synced to the grid?", "For stable electronic music, usually yes; for live or drifting material, set it by ear."),
        ("Why does my delay sound out of time?", "Check the project tempo, straight vs dotted value, and any tempo change in the track."),
    ],
)

# ---------------------------------------------------------------- tap tempo
PAGES["tap-tempo-guide.html"] = dict(
    title="Tap Tempo Guide: Accurate BPM by Hand | BPMfinder.ca",
    desc="How to tap tempo accurately in eight-bar phrases, average out drift, and know when to trust your ears instead of an automatic BPM detector.",
    path="/tap-tempo-guide.html",
    active="guides",
    h1="Tap tempo guide: when automatic detection fails",
    lead="Tap tempo is the oldest tempo detector in the room: a human, a steady pulse, and a stopwatch. It is still the best second opinion when an algorithm is not sure.",
    minutes="6 min read",
    updated="2026-10-20",
    tags=["tap tempo", "workflow", "live music"],
    body=f"""
<article class="card">
  <h2>Why tap tempo still matters</h2>
  <p>Automatic detection is fast, but it can lock onto a subdivision, a shaker, or a kick pattern that is not the pulse you would clap to. Tap tempo gives you a direct comparison between the machine&rsquo;s number and your body&rsquo;s sense of the beat. When they agree, you can move on. When they do not, the disagreement is the information.</p>
  <p>Tap tempo also works on material that is hard to analyze: a live drum performance, a rubato piano intro, a phone recording, or a track with a long spoken-word section. You do not need a clean file or a stable grid &mdash; you need a pulse you can feel.</p>
  <h2>How to tap well</h2>
  <ol>
    <li><strong>Start on a downbeat.</strong> Wait for a clear bar start, then tap the pulse you would count as 1, 2, 3, 4.</li>
    <li><strong>Tap eight bars.</strong> Two bars is not enough to average out a nervous finger; eight bars gives you a stable sample.</li>
    <li><strong>Use a consistent surface.</strong> A keyboard key, a mouse button, or the screen is fine &mdash; just keep it the same for the whole pass.</li>
    <li><strong>Do not tap the hi-hat.</strong> Tap the pulse that the drums and bass agree on.</li>
    <li><strong>Compare, then repeat.</strong> If the result is far from the detector, tap again on a different section.</li>
  </ol>
  <h2>What to do when taps drift</h2>
  <p>Drift is normal. A few milliseconds of variation is human; the average is what matters. If your taps are consistently speeding up or slowing down, you are probably following a phrase rather than a pulse. Reset and start again on a clear downbeat.</p>
  <p>If the track has a ritardando or a live drummer who pushes and pulls, a single tap-tempo number is only an average. Note the range instead: &ldquo;about 92&ndash;96 BPM, slower at the end.&rdquo; That is more useful than a false precision.</p>
</article>
{AD}
<article class="card">
  <h2>When automatic detection fails</h2>
  <p>Use tap tempo when the detector gives you a low-confidence result, when the track has no clear kick, when the intro is ambient, or when the reported BPM is exactly half or double what you feel. Those are not failures of the tool; they are cases where the human ear has better information.</p>
  <p>Our <a href="/bpm-detection-accuracy.html">accuracy test</a> found that the detector handles steady electronic pulses very well, but can return half-time or double-time at the extremes. Tap tempo is the fastest way to catch that.</p>
  <h2>Counting tips</h2>
  <p>Count out loud in a low voice, or mouth the numbers. Counting under your breath tends to collapse into the subdivision. Start on a downbeat and keep the numbers even; if you speed up the count, you are following the music rather than measuring it.</p>
  <p>If the track is in 3/4 or 6/8, tap the felt pulse rather than forcing four. A waltz counted in four will give you a number that no drummer in the room recognizes.</p>
  <h2>A practice drill</h2>
  <ol>
    <li>Play a track you know well &mdash; the free player at <a href="https://asiancoastline.com/">Asian Coastline</a> is a good source.</li>
    <li>Tap eight bars without looking at the BPM readout.</li>
    <li>Write down your number.</li>
    <li>Run the automatic detector on the same section.</li>
    <li>Compare. If they differ, decide which count the snare supports.</li>
  </ol>
  <p>Do this five times with different genres. You will start to hear the difference between a detector error and a counting choice.</p>
</article>
<article class="card faq">
  <h2>FAQ</h2>
  <h3>How many taps do I need?</h3>
  <p>At least eight bars. More taps average out small timing errors, but tapping for too long invites drift.</p>
  <h3>Why is my tap tempo different from the detector?</h3>
  <p>You may be tapping a different counting level (half or double), or the detector may have locked onto a subdivision. Check the snare and backbeat.</p>
  <h3>Does tap tempo work on live recordings?</h3>
  <p>Yes, but treat the result as a range if the tempo breathes. A single number is only meaningful for a stable pulse.</p>
  <h3>Can I tap with a keyboard?</h3>
  <p>Yes. The spacebar or a mouse button works; consistency matters more than the surface.</p>
</article>
<article class="card">
  <h2>Tap tempo in a DAW vs a phone</h2>
  <p>In a DAW, tap tempo usually sets the session tempo directly. That is convenient, but it can overwrite a tempo map you already built. If the project has tempo changes, tap into a separate tempo lane or note the value first, then decide where it belongs.</p>
  <p>On a phone, the risk is latency. Bluetooth audio adds delay between the sound you hear and the moment you tap. If you must tap over Bluetooth, do not trust the absolute number; use the taps to compare two sections, or switch to wired headphones for the check.</p>
  <h2>Common tapping mistakes</h2>
  <ul>
    <li><strong>Tapping the subdivision instead of the pulse.</strong> If you tap every hi-hat, you will get double or quadruple the tempo.</li>
    <li><strong>Starting mid-phrase.</strong> A tap sequence that begins on beat 3 will average against the wrong grid.</li>
    <li><strong>Tapping too briefly.</strong> Four taps is a guess; eight bars is a sample.</li>
    <li><strong>Watching the readout.</strong> Looking at the number can make you correct toward it. Tap first, then look.</li>
  </ul>
  <p>The best tap-tempo check is boring: same surface, same count, eight bars, then compare. If the number is unstable, the performance is unstable, not necessarily the tool.</p>
</article>
<article class="card">
  <h2>What tap tempo cannot fix</h2>
  <p>Tap tempo gives you an average pulse. It cannot tell you which section of a changing track is the &ldquo;real&rdquo; tempo, and it cannot separate a drummer&rsquo;s expressive push from a drift in the recording. If the tempo moves, write down a range and the section it belongs to.</p>
  <p>It also cannot rescue a file that is too short or too noisy to hear clearly. In those cases, the useful move is to find a cleaner section, not to tap harder. The tool and the hand are both estimates; the arrangement is the ground truth.</p>
</article>
{related("tap-tempo-guide.html")}
{AUTHOR}
""",
    faqs=[
        ("How many taps do I need?", "At least eight bars. More taps average out small timing errors, but too long invites drift."),
        ("Why is my tap tempo different from the detector?", "You may be tapping a different counting level, or the detector locked onto a subdivision."),
        ("Does tap tempo work on live recordings?", "Yes, but treat the result as a range if the tempo breathes."),
        ("Can I tap with a keyboard?", "Yes. Consistency matters more than the surface."),
    ],
)

# ---------------------------------------------------------------- half/double
PAGES["half-time-double-time.html"] = dict(
    title="Half-Time vs Double-Time BPM Explained | BPMfinder.ca",
    desc="Why the same groove can be 70 or 140 BPM, how to tell which count the track wants, and how to set a DAW session or DJ set without confusion.",
    path="/half-time-double-time.html",
    active="guides",
    h1="Half-time and double-time, explained",
    lead="The same groove can be counted at 70 or 140 BPM and both answers can be correct. The useful question is not &ldquo;which number is true?&rdquo; but &ldquo;which count helps me use the track?&rdquo;",
    minutes="6 min read",
    updated="2026-10-20",
    tags=["half-time", "double-time", "counting"],
    body=f"""
<article class="card">
  <h2>One pulse, two counts</h2>
  <p>A half-time feel puts the backbeat at half the speed of the underlying pulse. A double-time feel does the opposite: the surface moves twice as fast while the main pulse stays put. Drum-and-bass at 174 BPM can feel like 87; a trap record at 70 can be counted at 140; a boom-bap loop at 90 can read as 180 if the detector follows the hi-hats.</p>
  <p>The audio has not changed. The counting frame has. This is why a detector can return a number that is exactly double or half of what you expected and still be describing the same groove.</p>
  <h2>How to tell which count the track wants</h2>
  <ul>
    <li><strong>Find the snare.</strong> If the snare lands on beats 2 and 4 of a slow count, the slow number is usually the useful one.</li>
    <li><strong>Find the main pulse you would clap to.</strong> That is the count a drummer or DJ will share.</li>
    <li><strong>Check the subdivisions.</strong> If the energy is carried by fast hi-hats or arpeggios, the double may be the better session tempo.</li>
    <li><strong>Check the genre convention.</strong> DnB is usually counted at 174, not 87; trap is often counted at 140, not 70.</li>
  </ul>
</article>
{AD}
<article class="card">
  <h2>Examples that make it concrete</h2>
  <p><strong>70 / 140:</strong> a slow trap or halftime record. The kick and snare feel like 70; the hi-hats and vocal runs suggest 140. For a DAW session, 140 often makes programming easier; for a DJ set, 70 may match the energy better.</p>
  <p><strong>85 / 170:</strong> a drum-and-bass or halftime hybrid. The breakbeat moves at 170, but the main backbeat can feel like 85. Count the break for editing; count the half for blending with slower material.</p>
  <p><strong>64 / 128:</strong> a house track with a half-time vocal. The four-on-the-floor kick is 128; the vocal phrase may sit at 64. Do not average them &mdash; choose the grid that matches the drums.</p>
  <h2>DAW sessions and collaboration</h2>
  <p>Write the count in the session name or the project notes. &ldquo;140 BPM, halftime feel&rdquo; is clearer than a bare number. If you send a stem to a collaborator, tell them which count you used for the grid. A drummer who counts the track at 70 and a producer who programs at 140 can disagree about every edit even though they are hearing the same pulse.</p>
  <h2>Why this matters for BPM detection</h2>
  <p>Detectors estimate the repetition rate of transients. They do not know your counting convention. When a result looks exactly double or half, treat it as a question, not an error. Our <a href="/bpm-detection-accuracy.html">accuracy test</a> shows this happening at slow and fast extremes, and the <a href="/tap-tempo-guide.html">tap tempo guide</a> shows how to settle it by ear.</p>
</article>
<article class="card faq">
  <h2>FAQ</h2>
  <h3>Is 70 BPM the same as 140 BPM?</h3>
  <p>They can describe the same pulse at different counting levels. The audio is the same; the grid and the feel notation are different.</p>
  <h3>Which one should I use in my DAW?</h3>
  <p>Use the count that matches the drums and makes editing comfortable. For trap and halftime, 140 is common; for a slow jam, 70 may be clearer.</p>
  <h3>Why does the detector pick the wrong one?</h3>
  <p>It locks onto repeating transients, not musical intent. Check the snare and the subdivisions, then choose the count you need.</p>
  <h3>Can a track switch between them?</h3>
  <p>Yes. A halftime bridge or a double-time drop is a real arrangement device. Note the tempo for each section.</p>
</article>
<article class="card">
  <h2>Three listening tests</h2>
  <p><strong>The clap test.</strong> Clap the pulse you would naturally clap to. If the track&rsquo;s snare answers your clap on 2 and 4, you are probably on the slow count. If the clap feels like it is chasing the hi-hats, you are on the double.</p>
  <p><strong>The head-nod test.</strong> Nod once per kick. If you find yourself nodding twice as fast as the bassline, the track may be using a double-time surface over a slower pulse.</p>
  <p><strong>The edit test.</strong> Try to place a four-bar loop. If the loop feels like it takes forever to come around, your grid is probably too slow; if it feels frantic, your grid is probably too fast.</p>
  <h2>Writing it in a session</h2>
  <p>Put the count in the project name: <code>Artist - Title - 140 halftime</code>. If you use a tempo map, write the felt count in the marker at the first bar. When you send a stem, include one sentence: &ldquo;grid is 140, halftime feel; the backbeat is at 70.&rdquo; That single sentence prevents most collaboration confusion.</p>
  <p>For a DJ set, write both numbers when they matter: <code>174 / 87</code>. The first is the breakbeat tempo, the second is the felt pulse for blending. A double label is more useful than a debate.</p>
</article>
{related("half-time-double-time.html")}
{AUTHOR}
""",
    faqs=[
        ("Is 70 BPM the same as 140 BPM?", "They can describe the same pulse at different counting levels. The audio is the same; the grid and notation differ."),
        ("Which one should I use in my DAW?", "Use the count that matches the drums and makes editing comfortable."),
        ("Why does the detector pick the wrong one?", "It locks onto repeating transients, not musical intent. Check the snare and subdivisions."),
        ("Can a track switch between them?", "Yes. A halftime bridge or double-time drop is a real arrangement device; note each section."),
    ],
)

# ---------------------------------------------------------------- running
PAGES["bpm-for-running.html"] = dict(
    title="BPM for Running: Match Music to Your Cadence | BPMfinder.ca",
    desc="How to match music BPM to running cadence, build a warm-up-to-cooldown playlist, and avoid the half-time confusion that ruins workout mixes.",
    path="/bpm-for-running.html",
    active="guides",
    h1="BPM for running: match the music to your cadence",
    lead="Running has a tempo. Most runners land somewhere between 150 and 180 steps per minute, and a playlist that matches that pulse feels like it is pulling you forward instead of fighting you.",
    minutes="6 min read",
    updated="2026-10-20",
    tags=["running", "cadence", "playlists"],
    body=f"""
<article class="card">
  <h2>Cadence, not genre</h2>
  <p>Running cadence is the number of steps you take per minute. A relaxed jog might sit near 150&ndash;160; a faster run often lands near 170&ndash;180. Music BPM is not identical to steps per minute, but a track at 160 BPM gives you a pulse every 0.375 seconds &mdash; a natural scaffold for a 160-step cadence.</p>
  <p>You do not have to match exactly. A difference of a few BPM is fine; a difference of 20 is not. The goal is a pulse that supports your stride, not a metronome that makes you overstride.</p>
  <h2>BPM vs steps per minute</h2>
  <p>If a track is counted at half-time, its felt pulse may be half the reported BPM. A 174 BPM drum-and-bass track can feel like 87, which is too slow for running even though the number looks fast. Use the <a href="/half-time-double-time.html">half/double guide</a> to check which count you are actually hearing.</p>
  <p>Walking is different: most walkers sit near 100&ndash;130 steps per minute. A 120 BPM playlist is a better walking companion than a 170 BPM one.</p>
</article>
{AD}
<article class="card">
  <h2>Build the playlist as an arc</h2>
  <ol>
    <li><strong>Warm-up (5&ndash;10 min):</strong> 120&ndash;140 BPM. Let the body wake up before the pulse climbs.</li>
    <li><strong>Steady run:</strong> 150&ndash;165 BPM. This is the bulk of the session; choose tracks you can ignore.</li>
    <li><strong>Intervals or push:</strong> 165&ndash;180 BPM. Short blocks, then back to steady.</li>
    <li><strong>Cooldown:</strong> 100&ndash;130 BPM. Bring the pulse down instead of stopping cold.</li>
  </ol>
  <p>Do not stack every high-BPM track at the start. A playlist that jumps from 120 to 180 in one song feels like a mistake, even if each track is good on its own.</p>
  <h2>Test the list before you need it</h2>
  <p>Run the first ten minutes once and notice whether you are matching the music or fighting it. If you keep skipping tracks, the BPM is probably wrong for that part of the session, not the song. Adjust the arc, not the volume.</p>
  <p>If you want a listening catalog to test the workflow on, the free player at <a href="https://asiancoastline.com/">asiancoastline.com</a> streams the Excavationpro catalog without an account.</p>
  <h2>Safety note</h2>
  <p>This is music guidance, not medical advice. If you have a heart condition, an injury, or you are returning to running, talk to a qualified professional before using cadence or heart-rate targets.</p>
</article>
<article class="card faq">
  <h2>FAQ</h2>
  <h3>What BPM is best for running?</h3>
  <p>Most runners do well with 150&ndash;180 BPM, but the right number is your cadence, not a universal target.</p>
  <h3>Is 180 BPM the “correct” cadence?</h3>
  <p>It is a common target, not a rule. Height, pace, and experience change what is comfortable.</p>
  <h3>Why does a 174 BPM track feel slow?</h3>
  <p>It may be counted at half-time, so the felt pulse is 87. Check the snare and the main pulse.</p>
  <h3>Can I use the BPM tool for workout music?</h3>
  <p>Yes. Drop a track into the <a href="/app.html">free tool</a>, read the BPM, and build the playlist around the count you actually hear.</p>
</article>
<article class="card">
  <h2>An example 40-minute arc</h2>
  <div class="table-wrap"><table class="simple">
    <thead><tr><th>Block</th><th>Time</th><th>BPM</th><th>Job</th></tr></thead>
    <tbody>
      <tr><td>Walk-in</td><td>0&ndash;5 min</td><td>115&ndash;125</td><td>Warm up, check headphones, settle breathing</td></tr>
      <tr><td>Easy run</td><td>5&ndash;15 min</td><td>150&ndash;158</td><td>Find a sustainable stride</td></tr>
      <tr><td>Steady</td><td>15&ndash;28 min</td><td>160&ndash;168</td><td>Hold form; ignore the music</td></tr>
      <tr><td>Push</td><td>28&ndash;34 min</td><td>170&ndash;180</td><td>Short intervals or a hill</td></tr>
      <tr><td>Cooldown</td><td>34&ndash;40 min</td><td>110&ndash;130</td><td>Bring the pulse down</td></tr>
    </tbody>
  </table></div>
  <p>This is an example, not a prescription. The useful part is the shape: the BPM rises gradually, holds, peaks briefly, then falls. A playlist that starts at 180 and stays there is a 40-minute sprint, not a run.</p>
  <h2>When cadence drifts</h2>
  <p>If you notice your steps falling behind the music, do not speed up the playlist mid-run. Check whether the track is actually counted at half-time, then choose a song with a clearer pulse. If your cadence is drifting because of fatigue, slow the music down rather than forcing the stride. The playlist should support the body, not override it.</p>
  <p>For intervals, a short BPM jump is useful: 160 for the recovery, 175 for the work interval, then back. The contrast is the point. Keep the jump within about 15&ndash;20 BPM so the transition does not feel like a different song entirely.</p>
  <p>If you run with a metronome instead of music, set it to your current cadence rather than a target from a book. Then raise it by one or two steps per minute over several weeks. A sudden jump from 160 to 180 is a recipe for overstriding; a gradual change gives your body time to adapt.</p>
</article>
{related("bpm-for-running.html")}
{AUTHOR}
""",
    faqs=[
        ("What BPM is best for running?", "Most runners do well with 150-180 BPM, but the right number is your cadence."),
        ("Is 180 BPM the correct cadence?", "It is a common target, not a rule. Height, pace, and experience change what is comfortable."),
        ("Why does a 174 BPM track feel slow?", "It may be counted at half-time, so the felt pulse is 87."),
        ("Can I use the BPM tool for workout music?", "Yes. Drop a track into the tool, read the BPM, and build around the count you hear."),
    ],
)

# ---------------------------------------------------------------- accuracy
PAGES["bpm-detection-accuracy.html"] = dict(
    title="How Accurate Is Browser BPM Detection? Tested | BPMfinder.ca",
    desc="A measured test of the browser BPM detector: 21 click tracks at 60-180 BPM, including noise and offbeat variants, with real results and limits.",
    path="/bpm-detection-accuracy.html",
    active="guides",
    h1="How accurate is browser BPM detection?",
    lead="We generated click tracks at known tempos, ran them through the actual BPMfinder tool, and recorded what came back. The result is useful precisely because it is not always perfect.",
    minutes="7 min read",
    updated="2026-10-20",
    tags=["accuracy", "testing", "method"],
    body=f"""
<article class="card">
  <h2>What “accuracy” means here</h2>
  <p>Tempo detection is an estimate. A useful test asks two questions: does the tool return the tempo you put in, and when it does not, is the error a musically sensible half-time or double-time count? We tested the second question as carefully as the first.</p>
  <p>This is a synthetic test, not a survey of real records. Click tracks are easier than music: they have clean transients, no vocals, no reverb, and no arrangement changes. Treat these numbers as a best case, not a promise about every MP3.</p>
  <h2>Method</h2>
  <ol>
    <li>Generate 30-second mono WAV click tracks at 60, 70, 80, 90, 100, 110, 120, 128, 140, 150, 160, 174, and 180 BPM.</li>
    <li>Create four noise variants (90, 120, 140, 174 BPM) and four offbeat variants with an added offbeat click.</li>
    <li>Load each file into the live <a href="/app.html">BPMfinder tool</a> in Chrome, one at a time.</li>
    <li>Record the returned BPM and the confidence meter. A result was counted as exact only if it matched the input within 0.5 BPM.</li>
  </ol>
</article>
{AD}
<article class="card">
  <h2>Results</h2>
  <div class="table-wrap"><table class="simple">
    <thead><tr><th>Input BPM</th><th>Clean</th><th>Noise</th><th>Offbeat</th></tr></thead>
    <tbody>
      <tr><td>60</td><td>no result in 30 s</td><td>&mdash;</td><td>&mdash;</td></tr>
      <tr><td>70</td><td>140 (double)</td><td>&mdash;</td><td>&mdash;</td></tr>
      <tr><td>80</td><td>160 (double)</td><td>&mdash;</td><td>&mdash;</td></tr>
      <tr><td>90</td><td>90</td><td>90</td><td>90</td></tr>
      <tr><td>100</td><td>100</td><td>&mdash;</td><td>&mdash;</td></tr>
      <tr><td>110</td><td>110</td><td>&mdash;</td><td>&mdash;</td></tr>
      <tr><td>120</td><td>120</td><td>120</td><td>120</td></tr>
      <tr><td>128</td><td>128</td><td>&mdash;</td><td>&mdash;</td></tr>
      <tr><td>140</td><td>140</td><td>140</td><td>140</td></tr>
      <tr><td>150</td><td>150</td><td>&mdash;</td><td>&mdash;</td></tr>
      <tr><td>160</td><td>160</td><td>&mdash;</td><td>&mdash;</td></tr>
      <tr><td>174</td><td>174</td><td>174</td><td>174</td></tr>
      <tr><td>180</td><td>90 (half)</td><td>&mdash;</td><td>&mdash;</td></tr>
    </tbody>
  </table></div>
  <p><strong>17 of 21 files returned the exact tempo.</strong> Three returned a musically related half or double (70 &rarr; 140, 80 &rarr; 160, 180 &rarr; 90). One file, at 60 BPM, produced no result within the 30-second window.</p>
  <h2>What the results mean</h2>
  <p>In the 90&ndash;174 BPM range, the detector was exact on every clean file and every noise or offbeat variant we tested. That is the range most electronic music, DJ tools, and practice tracks live in. The errors clustered at the slow and fast extremes, where the detector chose a different counting level rather than a random number.</p>
  <p>The 60 BPM timeout is the one result we would not gloss over. A 30-second click track at 60 BPM contains only 30 beats; the tool may need a longer file, a clearer transient, or a different input to return a value. For very slow material, use tap tempo as the primary check and treat the detector as a second opinion.</p>
  <h2>Limits and what we did not test</h2>
  <ul>
    <li>We did not test real commercial recordings, vocals, live drums, or rubato performances.</li>
    <li>We did not test every browser or every audio codec; the test ran in Chrome with WAV files.</li>
    <li>We did not measure speed or CPU use; the focus was the returned tempo.</li>
    <li>A synthetic click track is a best case. Real music will produce more errors, especially at tempo changes.</li>
  </ul>
  <h2>How to reproduce it</h2>
  <p>Generate a click track at a known BPM, load it into the <a href="/app.html">tool</a>, and compare the returned value with the input. If you get a half or double, check the snare and the main pulse before assuming the tool is wrong.</p>
</article>
<article class="card faq">
  <h2>FAQ</h2>
  <h3>Is browser BPM detection accurate?</h3>
  <p>For steady electronic material in the 90&ndash;174 BPM range, our test was exact on every clean file. Real music and extreme tempos are harder.</p>
  <h3>Why did 70 BPM return 140?</h3>
  <p>The detector counted double-time subdivisions. The pulse is related; the counting level is different.</p>
  <h3>Why did 60 BPM fail?</h3>
  <p>It produced no result within 30 seconds in our test. Very slow material may need a longer clip or tap tempo.</p>
  <h3>Can I trust the confidence score?</h3>
  <p>Use it as a hint. High confidence on a clear beat is expected; low confidence is a signal to double-check, not a verdict.</p>
</article>
<article class="card">
  <h2>What the confidence meter did</h2>
  <p>Most exact results displayed 100% confidence on the meter, including the noise and offbeat variants. The 70 BPM file that returned 140 displayed 40%. But the 80 BPM file that returned 160 and the 180 BPM file that returned 90 both displayed 100%. That is the important lesson: <strong>confidence measures how tightly the detected beats cluster, not whether the count matches your intention.</strong></p>
  <p>A high score means the detector found a consistent pulse. It does not mean the pulse is the one you would clap to. Always check the snare and the main backbeat before trusting a high-confidence half or double.</p>
  <p>For a producer-facing walkthrough of the same problem, see <a href="https://deepseekoracle.com/articles/free-bpm-detection-guide.html">DeepSeek Oracle&rsquo;s practical BPM guide</a>.</p>
  <h2>Why a synthetic test still matters</h2>
  <p>It isolates the detector from the variables that make real music hard: vocals, reverb, arrangement changes, live timing, and codec artifacts. If the tool cannot handle a clean click track at a given tempo, that is a baseline fact worth knowing. If it handles the click track but fails on a real record, the problem is likely the material, not the arithmetic.</p>
  <p>We will keep this page updated if the detector changes. The method is simple enough to repeat: generate a click track at a known BPM, load it into the <a href="/app.html">tool</a>, and compare. If you run the test and get a different result, send it in &mdash; a reproducible disagreement is more useful than a review.</p>
  <h2>What would make this test stronger</h2>
  <ul>
    <li>A set of licensed real recordings with known tempo annotations.</li>
    <li>Live drum performances with and without a click.</li>
    <li>Multiple browsers and codecs (MP3, AAC, FLAC, WAV).</li>
    <li>A measurement of detection time, not just the returned number.</li>
  </ul>
  <p>Those are future work, not claims. The table above is what we actually measured today.</p>
</article>
{related("bpm-detection-accuracy.html")}
{AUTHOR}
""",
    faqs=[
        ("Is browser BPM detection accurate?", "For steady electronic material in the 90-174 BPM range, our test was exact on every clean file. Real music and extreme tempos are harder."),
        ("Why did 70 BPM return 140?", "The detector counted double-time subdivisions. The pulse is related; the counting level is different."),
        ("Why did 60 BPM fail?", "It produced no result within 30 seconds in our test. Very slow material may need a longer clip or tap tempo."),
        ("Can I trust the confidence score?", "Use it as a hint. High confidence is expected on a clear beat; low confidence is a signal to double-check."),
    ],
)

# ---------------------------------------------------------------- tools hub
PAGES["tools.html"] = dict(
    title="Free Creator Tools — BPM, Soundboard & More | BPMfinder.ca",
    desc="A map of the free creator tools: the BPM finder, delay tables, Soundboard FX, AI Talk Radio, the music player, LYGO games, SkillHub, and guide sites.",
    path="/tools.html",
    active="tools",
    h1="Free tools for creators",
    lead="BPMfinder is one tool in a wider workshop. The same independent stack includes a live soundboard, an AI radio station, a music player, games, a skill catalog, and long-form guides.",
    minutes="4 min read",
    updated="2026-10-20",
    tags=["tools", "soundboard", "creators"],
    body=f"""
<article class="card">
  <h2>The tools, in one place</h2>
  <p>Most people arrive at BPMfinder for one job: find a tempo. That is the right place to start, but it is not the whole workshop. The tools below are built for the same kind of person &mdash; a producer, DJ, streamer, writer, or creator who wants a useful result without an account, a subscription, or an upload to a stranger&rsquo;s server.</p>
  <div class="notice"><strong>Featured: Soundboard FX.</strong> The live creator soundboard inside AI Talk Radio &mdash; open the station, then choose the Soundboard tab. <a href="https://chatagent.ca/talk-radio/">Open AI Talk Radio &rarr;</a></div>
  <div class="grid2">
    <a class="tile" href="/app.html"><strong>BPM Finder</strong><span>Private browser tempo detection with confidence, tap tempo, half/double, and delay times.</span></a>
    <a class="tile" href="/delay-times-from-bpm.html"><strong>Delay &amp; tempo tables</strong><span>Convert BPM to note-value milliseconds for delays, reverb, and session planning.</span></a>
    <a class="tile" href="/tap-tempo-guide.html"><strong>Tap tempo guide</strong><span>A manual check for the tracks and performances that confuse a detector.</span></a>
    <a class="tile" href="https://chatagent.ca/talk-radio/"><strong>Soundboard FX</strong><span>A live creator soundboard inside the AI Talk Radio studio &mdash; open the station, then the Soundboard tab.</span></a>
    <a class="tile" href="https://chatagent.ca/talk-radio/"><strong>AI Talk Radio</strong><span>The live studio around the soundboard: stations, shows, and a continuous stream.</span></a>
    <a class="tile" href="https://asiancoastline.com/"><strong>Free music player</strong><span>The Excavationpro catalog, streamed without an account. A good place to test a tempo workflow.</span></a>
    <a class="tile" href="https://chatagent.ca/games/"><strong>LYGO games</strong><span>Browser games and interactive experiments from the same workshop.</span></a>
    <a class="tile" href="https://chatagent.ca/lygoskillhub.html"><strong>LYGO SkillHub</strong><span>The public skill catalog and download portal for LYGO agents and builders.</span></a>
    <a class="tile" href="https://deepseekoracle.com/"><strong>AI &amp; creator guides</strong><span>Longer guides on BPM, local AI, and practical creator workflows.</span></a>
    <a class="tile" href="https://eternalhaven.ca/"><strong>Books &amp; games</strong><span>Eternal Haven&rsquo;s books, essays, music, and browser games.</span></a>
    <a class="tile" href="https://justinhelmer.ca/"><strong>Artist portal</strong><span>Justin Helmer&rsquo;s artist identity, lyrics, stores, and live rooms.</span></a>
    <a class="tile" href="https://excavationpro.ca/"><strong>Music &amp; essays</strong><span>The approved Excavationpro site: original music, writing, and a clear listening license.</span></a>
  </div>
</article>
<article class="card">
  <h2>How the tools fit together</h2>
  <p>Use BPMfinder when you need a number: the tempo of a track, a delay time, a half-time check. Use the Soundboard when the work is live &mdash; drops, stingers, reactions, and the small sounds that make a stream feel produced. Use the music player when you want something to listen to or test a tempo against. The guides explain the parts that a tool cannot: why a detector disagrees with your ear, how to plan a set, and when a number is the wrong question.</p>
  <p>The common thread is local-first: the BPM analysis runs in your browser, the player streams without an account, and the guides are readable without a signup. Some tools link out to a studio or a catalog, but the entry point is always a page you can use immediately.</p>
  <h2>What is free</h2>
  <p>The BPM tool, the delay tables, the guides, the music player, the games, the SkillHub catalog, and the Soundboard FX tab are free to open. Optional support links on some sites help pay for hosting and time; they do not unlock a different version of the tool or a ranking.</p>
  <h2>Start with the job</h2>
  <ul>
    <li><strong>I have a track and need the tempo.</strong> Open the <a href="/app.html">BPM Finder</a>, drop a 20&ndash;40 second section, then check half/double and tap tempo.</li>
    <li><strong>I am going live.</strong> Open <a href="https://chatagent.ca/talk-radio/">AI Talk Radio</a> and choose the Soundboard tab for drops, stingers, and reactions.</li>
    <li><strong>I am producing.</strong> Use the <a href="/delay-times-from-bpm.html">delay table</a> to turn tempo into note-value milliseconds, then dial the effect by ear.</li>
    <li><strong>I am learning.</strong> Read <a href="/how-to-find-bpm.html">How to find a song&rsquo;s BPM</a> first; it explains the workflow the other guides assume.</li>
  </ul>
</article>
<article class="card faq">
  <h2>FAQ</h2>
  <h3>Are all of these tools free?</h3>
  <p>Yes. The tools listed here are free to open. Some sites accept optional support, but no tool requires a payment or an account.</p>
  <h3>Where is the soundboard?</h3>
  <p>Open <a href="https://chatagent.ca/talk-radio/">AI Talk Radio</a>, then choose the <strong>Soundboard</strong> tab. It is part of the live studio, not a separate download.</p>
  <h3>Do the tools upload my files?</h3>
  <p>The BPM tool analyzes audio in your browser for tempo detection. The player streams from the catalog. The <a href="/privacy.html">privacy policy</a> covers the BPMfinder side in detail.</p>
  <h3>Which tool should I start with?</h3>
  <p>If you have a track and need its tempo, start with the <a href="/app.html">BPM Finder</a>. If you are planning a live stream, start with the Soundboard. If you are learning, start with <a href="/how-to-find-bpm.html">How to find a song&rsquo;s BPM</a>.</p>
</article>
""",
    faqs=[
        ("Are all of these tools free?", "Yes. The tools listed here are free to open; some sites accept optional support but none require payment or an account."),
        ("Where is the soundboard?", "Open AI Talk Radio at chatagent.ca/talk-radio/, then choose the Soundboard tab."),
        ("Do the tools upload my files?", "The BPM tool analyzes audio in the browser for tempo detection; the player streams from the catalog."),
        ("Which tool should I start with?", "Use the BPM Finder for tempo, the Soundboard for live work, or How to find a song's BPM if you are learning."),
    ],
)

PAGES["guides.html"] = dict(
    title="BPM Guides: Tempo, Tap Tempo, DJ Workflow & Delay | BPMfinder.ca",
    desc="Original BPM guides for producers, DJs, dancers, and runners: find tempo, check half-time, tap tempo, plan a set, and calculate delay times.",
    path="/guides.html",
    active="guides",
    h1="BPM guides for real sessions",
    lead="Original educational articles on tempo detection, DJ workflow, tap tempo, delay timing, and the counting choices that make a BPM number useful.",
    minutes="4 min read",
    updated="2026-10-20",
    tags=["guides"],
    body=f"""
<article class="card">
  <h2>Start with the job in front of you</h2>
  <p>Most people arrive here with one of four questions: how do I find the BPM of a song, why does the number look wrong, how do I use BPM in a DJ set, or how do I turn a tempo into a delay time? The guides below are organised around those jobs rather than around keywords.</p>
  <p>If you are new, read <a href="/how-to-find-bpm.html">How to find a song&rsquo;s BPM</a> first. It gives you the workflow the other guides assume: choose a clean section, read the confidence, check half-time, and confirm with tap tempo. If you already have a number and want to use it, go straight to the DJ, delay, or running guide.</p>
</article>
<article class="card">
  <h2>All guides</h2>
  <div class="grid2">
    <a class="tile" href="/how-to-find-bpm.html"><strong>How to find a song&rsquo;s BPM</strong><span>The complete workflow: section choice, confidence, half/double, tap tempo, and recording the result.</span></a>
    <a class="tile" href="/bpm-for-djs.html"><strong>BPM for DJs</strong><span>Pitch-fader math, phrasing, set energy, tempo ranges, and a 20-minute practice drill.</span></a>
    <a class="tile" href="/delay-times-from-bpm.html"><strong>Delay times from BPM</strong><span>The 60,000/BPM formula, a full note-value table, and practical examples at common tempos.</span></a>
    <a class="tile" href="/tap-tempo-guide.html"><strong>Tap tempo guide</strong><span>How to tap eight bars accurately and when to trust your ears over the detector.</span></a>
    <a class="tile" href="/half-time-double-time.html"><strong>Half-time and double-time</strong><span>Why 70 and 140 can describe the same groove, and how to choose the count you need.</span></a>
    <a class="tile" href="/bpm-for-running.html"><strong>BPM for running</strong><span>Match music to running cadence and build a warm-up-to-cooldown playlist.</span></a>
    <a class="tile" href="/bpm-detection-accuracy.html"><strong>How accurate is BPM detection?</strong><span>Our measured test: 21 generated click tracks, including noise and offbeat variants.</span></a>
  </div>
</article>
<article class="card">
  <h2>How these guides are made</h2>
  <p>Each guide is written to answer a real session question, not to fill a page. Where a claim can be measured, we measure it: the accuracy page reports the actual returned tempos, including the failures. Where a number is a convention rather than a rule &mdash; genre tempo ranges, for example &mdash; we say so.</p>
  <p>The free <a href="/app.html">browser BPM tool</a> is the companion to these guides. It analyzes audio locally in your browser; the <a href="/privacy.html">privacy policy</a> explains what is and is not uploaded.</p>
  <p>Have a question the guides do not answer? <a href="/contact.html">Contact us</a> and say which page you were reading.</p>
</article>
<article class="card">
  <h2>Choose a path</h2>
  <p><strong>If you are new to tempo:</strong> start with How to find a song&rsquo;s BPM, then read Half-time and double-time. Those two pages cover the mistakes that make every other number confusing.</p>
  <p><strong>If you are preparing a DJ set:</strong> read BPM for DJs, then Delay times from BPM. The first gives you the planning math; the second gives you the mix math.</p>
  <p><strong>If you are producing:</strong> read Delay times from BPM and the accuracy test. One shows how tempo becomes a time value; the other shows where the detector can mislead you.</p>
  <p><strong>If you are running:</strong> go straight to BPM for running and build the arc before you build the playlist.</p>
  <p>Every guide links back to the free <a href="/app.html">browser tool</a>, so you can test the idea on a real file instead of reading about it. If a page raises a question that is not answered, the <a href="/contact.html">contact page</a> is the fastest way to get it added.</p>
</article>
""",
)

# ---------------------------------------------------------------- about
PAGES["about.html"] = dict(
    title="About BPMfinder.ca — Free BPM Tool & Guides by Justin Helmer",
    desc="Who publishes BPMfinder.ca, why the free browser BPM tool exists, how the guides are tested, and how to contact the publisher.",
    path="/about.html",
    active="about",
    h1="About BPMfinder.ca",
    lead="BPMfinder.ca is a free browser tempo tool and an original guide library for people who make, play, or move to music.",
    minutes="3 min read",
    updated="2026-10-20",
    tags=["about"],
    body=f"""
<article class="card">
  <h2>What this site is</h2>
  <p>BPMfinder.ca provides a free tempo detector that runs in your browser and a set of practical guides about BPM, tap tempo, half-time, delay times, DJ workflow, and running cadence. The tool does not require an account, and audio is analyzed on your device rather than uploaded for tempo detection.</p>
  <p>The site is published by Justin Helmer under the Excavationpro / LYGO workshop. It sits alongside <a href="https://excavationpro.ca/">excavationpro.ca</a> (music and essays), <a href="https://asiancoastline.com/">asiancoastline.com</a> (the free listening portal), <a href="https://deepseekoracle.com/">deepseekoracle.com</a> (AI and creator guides), <a href="https://eternalhaven.ca/">eternalhaven.ca</a> (books and games), and <a href="https://chatagent.ca/">chatagent.ca</a> (AI agent guides and tools).</p>
  <h2>Why it exists</h2>
  <p>Most BPM pages are thin tool shells. You drop a file, get a number, and learn nothing about why the number appeared or when to ignore it. The goal here is the opposite: a useful tool plus enough explanation that you can check the result, understand half-time and double-time, and use the tempo in a real session.</p>
  <p>The tool was built for the cases where a full DAW is inconvenient: a phone, a laptop without plugins, a quick check before a DJ set, or a private demo that should not be uploaded to a stranger&rsquo;s server.</p>
  <h2>How the guides are tested</h2>
  <p>Claims that can be measured are measured. The <a href="/bpm-detection-accuracy.html">accuracy page</a> reports a real test of the detector against generated click tracks, including the cases where it returned a half or double count or failed. Genre tempo ranges are presented as conventions, not rules. When a guide gives a number, it shows the arithmetic or the method behind it.</p>
  <h2>Editorial standards</h2>
  <ul>
    <li>Original writing, not scraped or auto-spun text.</li>
    <li>One clear job per page; no doorway pages or keyword stuffing.</li>
    <li>Visible byline and update date on every guide.</li>
    <li>Corrections are made in place and noted in the update date.</li>
    <li>Advertising is labelled and kept off tool, policy, and error pages.</li>
  </ul>
  <h2>How the tool is maintained</h2>
  <p>The tool is a static browser page, not a cloud service. There is no account database to breach and no upload queue to maintain. When the detector changes, the accuracy page is re-run and the date is updated. When a guide is corrected, the change is made in place and the update date moves.</p>
  <p>If you find a repeatable bug, send the file format, the browser, the expected BPM, and the returned BPM. A reproducible report is worth more than a star rating.</p>
  <p>The site is deliberately small: a tool, a guide library, and the policy pages needed to run it honestly. There is no account system, no newsletter pop-up, and no paywall. If that changes, this page will say so.</p>
  <h2>Advertising and support</h2>
  <p>This site may show Google AdSense advertising to support hosting and writing. Ads are labelled and kept off the tool, policy, and error pages. If you prefer not to see personalized ads, the <a href="/privacy.html">privacy policy</a> explains the cookie controls. Optional support through PayPal is a gift, not a subscription.</p>
  <h2>Contact</h2>
  <p>Email <a href="mailto:excavationstation@gmail.com">excavationstation@gmail.com</a> with &ldquo;BPMfinder&rdquo; in the subject. Public updates are at <a href="https://x.com/Excavationpro">@Excavationpro</a>. The <a href="/contact.html">contact page</a> explains what to include and how privacy requests are handled.</p>
</article>
{AUTHOR}
""",
)

# ---------------------------------------------------------------- privacy
PAGES["privacy.html"] = dict(
    title="Privacy Policy — BPMfinder.ca",
    desc="How BPMfinder.ca handles audio, logs, cookies, Google AdSense, consent, and privacy requests. Audio analysis runs locally in your browser.",
    path="/privacy.html",
    active="privacy",
    h1="Privacy Policy — BPMfinder.ca",
    lead="This policy explains what happens when you use the free BPM tool, read a guide, or see an ad. The short version: your audio is analyzed in your browser, not uploaded for tempo detection.",
    minutes="4 min read",
    updated="2026-10-20",
    tags=["privacy"],
    body=f"""
<article class="card">
  <h2>Summary</h2>
  <p>BPMfinder.ca is a free educational site with a browser-based tempo tool. Audio is analyzed locally for detection, not uploaded to a server. We do not require an account, and we do not sell reader data. Advertising, when active, is served by Google AdSense under its own policies.</p>
  <h2>Audio processing</h2>
  <p>When you choose a file in the <a href="/app.html">BPM tool</a>, the audio is decoded and analyzed locally in your browser using web audio technologies. The file is not uploaded to our server for tempo detection, and we do not keep a copy of it.</p>
  <p>Your browser may still use memory and temporary storage while the page is open. Closing the tab releases that working state. If you use a browser feature that syncs files or history across devices, that behavior is controlled by your browser and its settings, not by this site.</p>
  <h2>What we collect</h2>
  <p>We do not require an account and we do not ask for your name or email to use the tool. If you email us, we receive whatever you choose to send, including your email address and message. We use it to reply and to handle privacy requests.</p>
  <p>Like most websites, our hosting provider (GitHub Pages) and content delivery network may process standard technical logs such as IP address, user agent, requested URL, and timestamps for security and reliability. We do not use those logs to identify individual readers.</p>
  <h2>Cookies and advertising</h2>
  <p>We may use cookies or similar storage for essential site function, such as remembering your cookie choice. When Google AdSense is active, Google and its partners may use cookies or device information to serve and measure ads, including ads based on visits to this site or other sites.</p>
  <p>The AdSense publisher ID for this site is <code>ca-pub-0646320966060599</code>. You can review Google&rsquo;s advertising and privacy controls at <a href="https://policies.google.com/technologies/ads">policies.google.com/technologies/ads</a> and manage personalized ads at <a href="https://adssettings.google.com/">adssettings.google.com</a>. You can also block or clear cookies in your browser; blocking advertising cookies may affect ad personalization but does not lock the guides or the tool.</p>
  <h2>Consent</h2>
  <p>The site shows a cookie banner with Accept and Decline. Your choice is stored locally in your browser. If you decline, the banner will not keep asking on every page. You can change your choice by clearing the site&rsquo;s local storage in your browser settings.</p>
  <h2>Third parties</h2>
  <ul>
    <li><strong>GitHub Pages</strong> — hosts the static site and may keep standard access logs.</li>
    <li><strong>Google AdSense</strong> — serves advertising when active and may set advertising cookies.</li>
    <li><strong>Google Fonts</strong> — serves the typefaces used on the page.</li>
    <li><strong>Payment links</strong> — if you choose to support the site through PayPal, PayPal&rsquo;s own privacy policy applies.</li>
  </ul>
  <h2>Retention and children</h2>
  <p>We do not maintain a database of reader accounts or uploaded audio. Email correspondence is kept only as long as needed to answer the request. This is a general music-education site; we do not knowingly collect personal information from children, and no account is required.</p>
  <h2>Changes and contact</h2>
  <p>If this policy changes, the update date at the top of the page will change. For privacy questions or requests, email <a href="mailto:excavationstation@gmail.com">excavationstation@gmail.com</a> with &ldquo;BPMfinder privacy&rdquo; in the subject. See also the <a href="/terms.html">terms of use</a>.</p>
</article>
""",
)

# ---------------------------------------------------------------- terms
PAGES["terms.html"] = dict(
    title="Terms of Use — BPMfinder.ca",
    desc="The terms for using BPMfinder.ca: the free tool, acceptable use, intellectual property, warranty and liability limits, and changes.",
    path="/terms.html",
    active="terms",
    h1="Terms of use — BPMfinder.ca",
    lead="These terms cover your use of the BPMfinder.ca website, the free browser BPM tool, and the guides. By using the site, you agree to them.",
    minutes="3 min read",
    updated="2026-10-20",
    tags=["terms"],
    body=f"""
<article class="card">
  <h2>The service</h2>
  <p>BPMfinder.ca provides a free browser-based tempo detector and original educational content about BPM, tap tempo, delay times, DJ workflow, and related topics. The tool is provided as-is; tempo detection is an estimate, not a guarantee. Always check an important result with your ears or a second method.</p>
  <h2>Acceptable use</h2>
  <ul>
    <li>Do not use the site to break the law or to infringe someone else&rsquo;s rights.</li>
    <li>Do not upload or process material you do not have the right to use.</li>
    <li>Do not attempt to disrupt the site, scrape it at abusive volume, or bypass security controls.</li>
    <li>Do not present the tool&rsquo;s output as a professional measurement without independent verification.</li>
  </ul>
  <h2>Intellectual property</h2>
  <p>The guides, site design, and original text are owned by Justin Helmer / Excavationpro unless otherwise stated. You may link to the pages and quote short passages with attribution. You may not republish the guides wholesale, resell them, or train a commercial model on them without written permission.</p>
  <p>The BPM tool is provided for personal and professional use. The name BPMfinder.ca and the site branding may not be used in a way that suggests endorsement of a third-party product.</p>
  <h2>No warranty</h2>
  <p>The site and tool are provided without warranties of any kind, express or implied, including fitness for a particular purpose and non-infringement. Tempo detection can be wrong, especially on live, ambient, rubato, or tempo-changing material. You are responsible for verifying any result you rely on.</p>
  <h2>Limitation of liability</h2>
  <p>To the maximum extent permitted by law, Justin Helmer / Excavationpro is not liable for indirect, incidental, special, or consequential damages arising from the use of the site or the tool, including lost work, lost revenue, or damage to a project.</p>
  <h2>Governing law and severability</h2>
  <p>These terms are governed by the laws applicable in the publisher&rsquo;s province of residence in Canada, without regard to conflict-of-law rules. If any provision is found unenforceable, the remaining provisions stay in effect.</p>
  <h2>Changes and contact</h2>
  <p>These terms may be updated; the date at the top of the page will change when they are. Questions about the terms can be sent to <a href="mailto:excavationstation@gmail.com">excavationstation@gmail.com</a> with &ldquo;BPMfinder terms&rdquo; in the subject. See also the <a href="/privacy.html">privacy policy</a>.</p>
</article>
""",
)

# ---------------------------------------------------------------- contact
PAGES["contact.html"] = dict(
    title="Contact BPMfinder.ca — Publisher & Support",
    desc="Contact BPMfinder.ca about the free BPM tool, a guide correction, privacy requests, or supporting the project.",
    path="/contact.html",
    active="contact",
    h1="Contact BPMfinder.ca",
    lead="Questions about the tool, a correction to a guide, a privacy request, or a broken link &mdash; email is the reliable route.",
    minutes="2 min read",
    updated="2026-10-20",
    tags=["contact"],
    body=f"""
<article class="card">
  <h2>Email</h2>
  <p><a href="mailto:excavationstation@gmail.com?subject=BPMfinder">excavationstation@gmail.com</a></p>
  <p>Please put <strong>&ldquo;BPMfinder&rdquo;</strong> in the subject line and allow a few business days for a reply. This is a small independent project, not a support desk.</p>
  <h2>What to include</h2>
  <ul>
    <li>For a tool question: the browser, the file format, and what you saw (the BPM or the error).</li>
    <li>For a guide correction: the page URL and the sentence you think is wrong.</li>
    <li>For a privacy request: the email you used and what you want changed or removed.</li>
    <li>For a broken link: the page you were on and the link that failed.</li>
  </ul>
  <p>Do not send passwords, API keys, or private audio you do not want a stranger to hear.</p>
  <h2>Publisher</h2>
  <p>Justin Helmer &middot; Canada. The site is part of the Excavationpro / LYGO workshop. Public updates are at <a href="https://x.com/Excavationpro">@Excavationpro</a> and the source projects are at <a href="https://github.com/DeepSeekOracle">github.com/DeepSeekOracle</a>.</p>
  <h2>Support the project</h2>
  <p>Optional support through <a href="https://www.paypal.com/paypalme/ExcavationPro">PayPal.me/ExcavationPro</a> helps pay for hosting and time. It does not buy a ranking, a custom guide, or a guarantee of support.</p>
  <h2>Response times and limits</h2>
  <p>Most messages get a reply within a few business days. I cannot debug a specific DAW project, recover a lost session, or provide legal advice about a sample or a licence. I can answer questions about the tool, correct a factual error in a guide, and route a privacy request.</p>
  <p>If you are reporting a BPM result that looks wrong, include the file format, the browser, the expected tempo, and the returned tempo. A short screen recording or a link to the file (only if you have the rights to share it) is more useful than a description.</p>
  <h2>Policy pages</h2>
  <p><a href="/privacy.html">Privacy policy</a> &middot; <a href="/terms.html">Terms of use</a> &middot; <a href="/about.html">About the site</a></p>
</article>
""",
)
