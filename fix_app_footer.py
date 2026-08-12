from pathlib import Path

p = Path("app.html")
t = p.read_text(encoding="utf-8")
need = ["/privacy.html", "/contact.html", "/about.html", "/guides.html", "/terms.html"]
missing = [n for n in need if n not in t]
print("missing", missing)
if "BPMfinder.ca — free BPM tool" not in t and "</body>" in t:
    inject = """
<footer style="font-family:system-ui,sans-serif;font-size:13px;padding:1.2rem;border-top:1px solid #ddd;margin-top:2rem;background:#fafafa">
  <div style="max-width:900px;margin:0 auto">
    <a href="/">Home</a> ·
    <a href="/guides.html">Guides</a> ·
    <a href="/about.html">About</a> ·
    <a href="/contact.html">Contact</a> ·
    <a href="/privacy.html">Privacy</a> ·
    <a href="/terms.html">Terms</a>
    <p style="color:#666;margin:.5rem 0 0">BPMfinder.ca — free BPM tool. Audio analyzed in your browser.</p>
  </div>
</footer>
"""
    t = t.replace("</body>", inject + "</body>", 1)
    p.write_text(t, encoding="utf-8")
    print("footer injected")
else:
    print("footer ok/skip")
