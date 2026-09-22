"""Regenerate VOICEOVER.md from the <aside class="notes"> blocks in index.html.
Run after editing any slide's notes:  python tools/extract_voiceover.py"""
import re, html, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
src = (root / "index.html").read_text(encoding="utf-8")
slides = re.findall(r'<section class="slide[^"]*"[^>]*data-part="([^"]*)"[^>]*data-title="([^"]*)"[^>]*>(.*?)</section>', src, re.S)
out = ["# Voiceover script", "", "Prompt Engineering, from Zero to Everything. Research Friday talk by Parv Agarwal.", "",
       "Delivery notes: about 150 words per minute. Each slide runs 60 to 110 seconds; the full script runs 55 to 65 minutes. "
       "Pause on interactive slides and do the action described in the script. Press N during the talk to see this text under the slide.", ""]
words = 0
current_part = None
for i, (part, title, body) in enumerate(slides, 1):
    m = re.search(r'<aside class="notes">(.*?)</aside>', body, re.S)
    paras = re.findall(r"<p>(.*?)</p>", m.group(1), re.S) if m else []
    if part != current_part:
        out += [f"## {html.unescape(part)}", ""]; current_part = part
    out += [f"### Slide {i}: {html.unescape(title)}", ""]
    for p in paras:
        t = html.unescape(re.sub(r"<[^>]+>", "", p)).strip()
        t = re.sub(r"\s+", " ", t)
        words += len(t.split()); out += [t, ""]
out.insert(4, f"Total: {len(slides)} slides, {words:,} words, roughly {round(words/150)} minutes at a calm pace.")
out.insert(5, "")
(root / "VOICEOVER.md").write_text("\n".join(out), encoding="utf-8")
print(f"{len(slides)} slides, {words} words")
