"""Builds the Titans kit-design prompt pack PDF in the QuantumBerry brand.
Prompts come from gen.py (single source); CSS and assets reuse dr-faul-pack."""
import json, html, re, os, subprocess, importlib.util
here = os.path.dirname(os.path.abspath(__file__)); os.chdir(here)
spec = importlib.util.spec_from_file_location("gen", "gen.py"); 
src = open("gen.py").read().split("F = ")[0]  # only the prompt definitions
g = {}; exec(src, g)
P1, P2, P3, P4 = g["P1"], g["P2"], g["P3"], g["P4"]

def dump(o, ind=0, width=104):
    """JSON with short dicts/lists kept on one line, so prompts fit a page."""
    flat = json.dumps(o, ensure_ascii=False)
    if not isinstance(o, (dict, list)) or len(flat) + ind <= width: return flat
    pad = "  " * (ind // 2 + 1); end = "  " * (ind // 2)
    if isinstance(o, dict):
        items = [f'{pad}{json.dumps(k)}: {dump(v, ind + 2, width)}' for k, v in o.items()]
        return "{\n" + ",\n".join(items) + "\n" + end + "}"
    return "[\n" + ",\n".join(pad + dump(v, ind + 2, width) for v in o) + "\n" + end + "]"
for p in (P1, P2, P3, P4): assert json.loads(dump(p)) == p

t = open("../dr-faul-pack/template.html").read()
css = t[t.index("<style>") + 7:t.index("</style>")].replace("url(assets/", "url(../dr-faul-pack/assets/")
css += """
.code{background:#0F1115;color:#E8E6E3;font-family:"DM Mono",monospace;font-size:6.9pt;line-height:1.42;padding:4.5mm 5mm;border-left:1.3mm solid var(--red);white-space:pre-wrap;word-break:break-word}
.code .k{color:#7FB8E0}.code .s{color:#F0D9A8}
.fill{display:grid;grid-template-columns:auto 1fr;gap:0;margin:3mm 0 4mm;border-top:1px solid var(--line)}
.fill div{padding:1.6mm 3mm;border-bottom:1px solid var(--line);font-size:8.4pt}
.fill div:nth-child(odd){font-family:"DM Mono";font-weight:500;font-size:7pt;color:var(--blue);letter-spacing:.06em}
.howto{display:flex;gap:2.5mm;margin:3mm 0 4mm}
.howto div{flex:1;background:var(--panel);padding:2.6mm 3mm;font-size:8pt;line-height:1.4;color:var(--mute);border-top:.8mm solid var(--blue)}
.howto b{display:block;color:#111;font-size:8.4pt;margin-bottom:.6mm}
"""
HEAD = '<div class="hd"><div class="brand"><img src="../dr-faul-pack/assets/emblem.png" alt=""><div><b>QuantumBerry AI</b><small>APPLIED AI ENGINEERING</small></div></div><div class="r">TITANS KIT DESIGN<br>NO. QB-TK-2026-01</div></div><div class="hdrule"></div>'
def foot(n): return f'<div class="ft"><span>QuantumBerry AI</span><span>Titans Kit Design Prompt Pack &nbsp;·&nbsp; 2026 &nbsp;·&nbsp; quantumberryai.co.za</span><b>{n:02d}</b></div>'
def code(o):
    s = html.escape(dump(o))
    s = re.sub(r'(&quot;[^&]*?&quot;)(:)', r'<span class="k">\1</span>\2', s)
    return f'<div class="code">{s}</div>'
def page(n, inner): return f'<section class="page">{HEAD}<div class="body">{inner}</div>{foot(n)}</section>'
def head(num, title, lead):
    return f'<div class="sec"><span class="n">{num}</span><h2>{title}</h2></div><div class="rule"></div><p class="lead" style="font-size:10pt">{lead}</p>'
def fill(rows): return '<div class="fill">' + "".join(f"<div>{a}</div><div>{b}</div>" for a, b in rows) + "</div>"
def howto(*steps): return '<div class="howto">' + "".join(f"<div><b>{a}</b>{b}</div>" for a, b in steps) + "</div>"

pages = []
pages.append("""<section class="page dark cover"><div class="topbar"></div>
<div class="lockup"><img src="../dr-faul-pack/assets/emblem.png" alt=""><div><b>QuantumBerry AI</b><small>Applied AI Engineering Studio &nbsp;·&nbsp; Cape Town, South Africa</small></div></div>
<div class="redbar"></div><div class="lab">AI Prompt Pack &nbsp;·&nbsp; Titans Cricket</div>
<h1>Design the<br>new kit.<br><em>Keep every<br>logo intact.</em></h1>
<div class="sub">A storyboard-first workflow and four copy-paste prompts for designing the Titans men's and women's playing shirts and pants in Gemini or ChatGPT.</div>
<div class="meta"><div><small>Prepared for</small><b>Karen Smithies</b><span>Titans Cricket</span></div><div><small>Issued</small><b>October 2026</b><span>Revision 01</span></div><div><small>Reference</small><b>QB-TK-2026-01</b><span>Kit Design Prompts</span></div></div>
<div class="tag">Intelligent systems. <b>Real world impact.</b></div>
<div class="cl"><span>chad@quantumberryai.co.za</span><span>quantumberryai.co.za</span></div></section>""")

pages.append(page(2, head("01", "How it works", "Start with a storyboard, then refine one step at a time. Each prompt is written in JSON so every detail sits in its own labelled field and nothing gets forgotten.") + """
<div class="grid3" style="margin-top:5mm">
<div class="card"><div class="k">Why</div><h4>Storyboard first</h4><p>Each run gives one page per idea: front, back, side, pants, close-ups, colours and a player wearing it. Make three, pick one, and every later step uses it as the reference.</p></div>
<div class="card b"><div class="k">Why</div><h4>JSON prompts</h4><p>Gemini and ChatGPT both read JSON well. Copy the whole block, swap the {CURLY} words for your choices, paste it in. The last line repeats the brief in plain English.</p></div>
<div class="card"><div class="k">Rule</div><h4>Logos stay intact</h4><p>Every prompt uses the attached official logo files with strict rules. The supplier drawings leave the logo spaces blank, and the real files go on last.</p></div>
</div>
<h3>The workflow</h3>
<div class="steps">
<div class="s"><i>00</i><div><b>One-time setup</b><span>Create a Gemini Gem or ChatGPT Project called "Titans Kit Design". Upload the official logos as transparent PNGs (TITANS_CREST.png, MOMENTUM_MULTIPLY.png, FIDELITY.png, KIT_SUPPLIER.png), the brand colour codes, and front, back and side photos of the current kit.</span></div></div>
<div class="s"><i>01</i><div><b>Storyboard</b><span>Prompt 1. Run three themes, compare the boards, pick one.</span></div></div>
<div class="s"><i>02</i><div><b>Production flats</b><span>Prompt 2. Clean supplier drawings of the chosen kit with blank, labelled logo spaces.</span></div></div>
<div class="s"><i>03</i><div><b>On-player hero shot</b><span>Prompt 3. A photoreal player in the kit for sign-off and social media.</span></div></div>
<div class="s"><i>04</i><div><b>Small changes</b><span>Prompt 4. One change per message, so the AI never redoes the whole design.</span></div></div>
<div class="s"><i>05</i><div><b>Logo check and finish</b><span>Zoom to 100% and compare every logo with the original file. Place the real logo files on the flats in Canva or Illustrator before anything goes to the supplier.</span></div></div>
</div>
<div class="callout"><div class="k">The golden rule</div><p><b>Attach the logo files to every prompt</b>, even inside the Gem or Project. Image tools follow attached files far more reliably than stored ones.</p></div>"""))

pages.append(page(3, head("02", "Prompt 1 &middot; Storyboard", "Start here. Attach the logo files, fill in the words in {CURLY BRACKETS}, paste the block from the next page, and run it three times with three different themes.") +
  howto(("Attach","All the official logo files"),("Fill in","The words in {CURLY BRACKETS} below"),("Run","Three times, three themes, then pick one board")) +
  fill([("CONCEPT_NAME","A name for the idea, e.g. Northern Thunder"),("THEME","Pride of the north, lightning, heritage, modern speed or fan culture"),
        ("TEAM","Momentum Multiply Titans (men) or Fidelity Titans (women)"),("FIT","Men's athletic fit or women's tailored fit"),
        ("MAIN_SPONSOR_FILE","MOMENTUM_MULTIPLY.png or FIDELITY.png"),("PRIMARY / SECONDARY / ACCENT_HEX","Colour codes, e.g. #0B2D5B"),
        ("PATTERN_IDEA","e.g. subtle lightning lines, a diamond weave"),("FORMAT","One-day or T20")]) +
  """<h3>What you get back</h3><div class="grid2" style="margin-top:3mm">
<div class="card"><div class="k">Shirt</div><h4>Front, back and side</h4><p>Symmetrical front view, back with name and number, side view showing sleeve and side panels.</p></div>
<div class="card b"><div class="k">Pants</div><h4>Front and back</h4><p>Tapered playing pants with matching panels and piping.</p></div>
<div class="card b"><div class="k">Details</div><h4>Close-ups and colours</h4><p>Collar, cuff, fabric texture, waistband, plus colour chips with hex codes and a number font sample.</p></div>
<div class="card"><div class="k">Mood</div><h4>On a player</h4><p>A small image of a cricketer wearing the kit in a floodlit stadium.</p></div></div>
<div class="callout"><div class="k">Tip</div><p>If a board puts a pattern over a logo or adds a sponsor that isn't attached, run it again rather than editing. The storyboard is cheap; the later steps rely on it being right.</p></div>"""))
pages.append(page(4, '<div class="kick">Prompt 1 &middot; Storyboard &middot; copy this whole block</div>' + code(P1)))
pages.append(page(5, head("03", "Prompt 2 &middot; Production flats", "Attach the storyboard you picked. The AI draws clean front, back and side drawings for the supplier and deliberately leaves the logo spaces empty.") +
  howto(("Attach","The chosen storyboard image"),("Paste","Prompt 2 exactly as is"),("Then","Place the real logo files into the blank boxes in Canva or Illustrator")) + code(P2) +
  '<div class="callout"><div class="k">Why blank logo spaces</div><p>Image AI can still slightly redraw a logo, even with strict rules. Leaving the spaces blank and placing the official files yourself is the only way to guarantee every logo is 100% correct on what goes to the supplier.</p></div>'))

pages.append(page(6, head("04", "Prompt 3 &middot; On-player hero shot", "Attach the chosen kit image and the logo files. This gives the team a real-looking photo for sign-off and social media.") +
  howto(("Attach","Chosen kit image plus the logo files"),("Fill in","The words in {CURLY BRACKETS} below"),("Use it for","Sign-off, launch posts and sponsor previews")) +
  fill([("CRICKETER","e.g. fast bowler, mid-20s"),("ACTION","e.g. at the point of delivery"),("MAIN_WORD","RISE, ROAR, TITANS or BELIEVE"),
        ("ENVIRONMENT","e.g. floodlit night match at a packed stadium"),("ACCENT_HEX","The accent colour from the chosen kit")]) +
  """<h3>What makes it look real</h3><ul class="bl">
<li><b>Connected perspective:</b> body, arm, hand and bat or ball form one believable line toward the camera.</li>
<li><b>Real skin and sweat,</b> not plastic or airbrushed.</li>
<li><b>Floodlight rim light</b> outlining the player against a full-bleed stadium.</li>
<li><b>One bold word</b> behind the player in the kit's accent colour, partly hidden by the body for depth.</li></ul>
<div class="callout"><div class="k">Check before sharing</div><p>Look closely at hands, the bat and every logo. If a logo is off, place the official file over it in Canva before the image is used anywhere.</p></div>"""))
pages.append(page(7, '<div class="kick">Prompt 3 &middot; On-player hero shot &middot; copy this whole block</div>' + code(P3)))
pages.append(page(8, head("05", "Prompt 4 &middot; Small changes", "Use this whenever you want to adjust one thing. It stops the AI from redoing the whole design.") +
  howto(("Attach","The image you want to adjust"),("Change","One thing per message"),("ChatGPT tip","Use the select tool to paint over only the area to change")) + code(P4) +
  """<h3>Women's kit</h3><p>Run Prompt 1 again with <b>TEAM</b> = Fidelity Titans, <b>FIT</b> = women's tailored fit and <b>MAIN_SPONSOR_FILE</b> = FIDELITY.png. Keep the same concept name and colours so the two kits read as one family.</p>
<h3>Gemini or ChatGPT?</h3><p>Both work. Gemini tends to hold a design steadier across edits; ChatGPT's select tool is the easiest way to change one small area. Try the same storyboard prompt in both and keep whichever you like.</p>
<h3>Logo checklist before anything is approved</h3>
<ul class="bl"><li><b>Zoom to 100%</b> and compare each logo with the original file, letter by letter.</li><li><b>Reject</b> any image with a changed letter, shape, colour or proportion.</li><li><b>Final files:</b> the official logos are placed by hand on the production flats.</li><li><b>No extra sponsors</b> or text the AI added on its own.</li></ul>
<div class="callout"><div class="k">Next step</div><p>Chad will take you through these prompts on a short call and run the first storyboard with you.</p></div>"""))

doc = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>QuantumBerry AI | Titans Kit Design Prompt Pack</title><style>{css}</style></head><body>{"".join(pages)}</body></html>'
open("Titans-Kit-Design-Prompt-Pack.html", "w").write(doc)
CH = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
subprocess.run([CH, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer", "--allow-file-access-from-files",
                "--print-to-pdf=Titans-Kit-Design-Prompt-Pack.pdf", "file://" + here + "/Titans-Kit-Design-Prompt-Pack.html"], stderr=subprocess.DEVNULL)
