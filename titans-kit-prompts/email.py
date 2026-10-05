"""Builds the short branded email to Karen (house layout copied from the sent Dr Faul / SA Grand Tour emails).
Writes email_karen.html (with cid logo) and email_karen.txt."""
import base64, os
here = os.path.dirname(os.path.abspath(__file__))
F = "font-family:Georgia,'Times New Roman',serif;"
def tbl(inner, margin=""):
    st = ' style="margin:' + margin + '"' if margin else ""
    return '<table width="100%" cellpadding="0" cellspacing="0" border="0"' + st + '><tbody>' + inner + '</tbody></table>'
def row(txt, pad="14px 0 0 0", size=15, color="#3a3a36", lh=26, extra=""):
    return f'<tr><td style="padding:{pad};{F}font-size:{size}px;line-height:{lh}px;color:{color};{extra}">{txt}</td></tr>'
def head(t): return tbl(row(f'<span style="color:#c0392b">—  </span>{t}', pad="0", size=17, color="#1a1a1a"), "34px 0 0 0")
def kv(k, v, c="#1a1a1a"):
    return f'<tr><td width="140" valign="top" style="padding:6px 0;{F}font-size:14px;line-height:22px;color:#8a8a80">{k}</td><td style="padding:6px 0;{F}font-size:14px;line-height:22px;color:{c}">{v}</td></tr>'
BOOK = "https://cal.com/quantumberry/30min-free-consult"
h = []
h.append(f'<table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#f2f4ec"><tbody><tr><td align="center" style="padding:34px 14px"><table width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:600px;background-color:#fafaf5"><tbody><tr><td style="padding:44px 46px 40px 46px">')
h.append(tbl(f'<tr><td align="center" style="padding:0 0 18px 0;{F}font-size:13px;line-height:20px;color:#c0392b;font-weight:bold">[ATTACH Titans-Kit-Design-Prompt-Pack.pdf BEFORE SENDING, then delete this line]</td></tr>'))
h.append(tbl(''
  f'<tr><td align="center" style="padding:0;{F}font-size:15px;letter-spacing:4.5px;color:#1a1a1a;text-transform:uppercase;line-height:22px">QUANTUMBERRY AI</td></tr>'
  f'<tr><td align="center" style="padding:9px 0 0 0;{F}font-style:italic;font-size:12.5px;color:#8a8a80;line-height:18px">From design to automation, we make technology think for you.</td></tr>'
  '<tr><td align="center" style="padding:18px 0 0 0"><table cellpadding="0" cellspacing="0" border="0" align="center"><tbody><tr><td style="width:42px;height:2px;background-color:#c0392b;line-height:2px;font-size:0"> </td></tr></tbody></table></td></tr>'))
h.append(tbl(row("Designing the<br>new Titans kit", pad="34px 0 0 0", size=26, color="#1a1a1a", lh=34)))
h.append(tbl(row("Hi Karen,", pad="24px 0 0 0") +
  row("The prompt pack for the new men's and women's playing shirts and pants is attached. It works in both Gemini and ChatGPT, and it fixes the two things we spoke about: logos coming out wrong, and small edits redoing the whole design.") +
  row("You start with a storyboard of each idea, pick the best one, and refine it step by step. The official logo files are always used, so the logos stay intact.")))
h.append(tbl('<tr><td style="height:3px;background-color:#1a5fa8;line-height:3px;font-size:0"> </td></tr>'
  f'<tr><td align="center" style="padding:20px 12px 0 12px;{F}font-size:10.5px;letter-spacing:2.6px;color:#1a5fa8;text-transform:uppercase">ATTACHED</td></tr>'
  f'<tr><td align="center" style="padding:11px 16px 4px 16px;{F}font-size:26px;line-height:34px;color:#1a1a1a">Titans Kit Design<br>Prompt Pack</td></tr>'
  f'<tr><td align="center" style="padding:0 16px 20px 16px;{F}font-style:italic;font-size:12.5px;line-height:20px;color:#8a8a80">PDF, 8 pages, copy-paste prompts</td></tr>'
  '<tr><td style="height:1px;background-color:#deded6;line-height:1px;font-size:0"> </td></tr>', "32px 0 0 0"))
h.append(head("What is inside"))
h.append(tbl('<tr><td style="padding:13px 0 0 0"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tbody>' +
  kv("Step 1", "Storyboard of each shirt idea: front, back, side, pants and details") +
  kv("Step 2", "Clean drawings for the supplier, with blank logo spaces") +
  kv("Step 3", "A photo of a player wearing the kit") +
  kv("Step 4", "Small edits without redoing the design") +
  kv("Logos", "Always the official files, placed last by hand", "#c0392b") + '</tbody></table></td></tr>'))
h.append(head("Next step"))
h.append(tbl(row("Let's do a short call. I will take you through the prompts and run the first storyboard with you.", pad="13px 0 0 0", color="#6b6b63") +
  row("Please have the official logo files (transparent PNGs) and the brand colour codes ready.", color="#6b6b63")))
h.append(tbl(f'<tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" align="center" style="border-collapse:separate"><tbody><tr><td align="center" style="padding:14px 34px;border:1px solid #1a5fa8"><a href="{BOOK}" style="{F}font-size:12.5px;letter-spacing:2.4px;color:#1a5fa8;text-decoration:none;text-transform:uppercase">Book our call</a></td></tr></tbody></table></td></tr>'
  f'<tr><td align="center" style="padding:15px 0 0 0;{F}font-size:12.5px;line-height:19px;color:#6b6b63">or simply reply with a time that suits you</td></tr>', "32px 0 0 0"))
h.append(tbl(row("When you have a moment, could you also send the clothing inventory sheets with the player lists and item costs? That is what populates the stock-take app.", pad="0", color="#6b6b63"), "34px 0 0 0"))
h.append(tbl('<tr><td style="height:1px;background-color:#deded6;line-height:1px;font-size:0"> </td></tr>'
  f'<tr><td style="padding:22px 0 0 0;{F}font-size:15px;line-height:24px;color:#1a1a1a">Chat soon,</td></tr>'
  f'<tr><td style="padding:14px 0 0 0;{F}font-size:18px;line-height:24px;color:#1a1a1a">Chad Douglas</td></tr>'
  f'<tr><td style="padding:5px 0 0 0;{F}font-size:13.5px;line-height:21px;color:#6b6b63">Founder &amp; CEO  |  QuantumBerry AI</td></tr>'
  f'<tr><td style="padding:9px 0 0 0;{F}font-size:13px;line-height:22px;color:#6b6b63"><a href="mailto:chad@quantumberryai.co.za" style="color:#1a5fa8;text-decoration:none">chad@quantumberryai.co.za</a><br><a href="https://quantumberryai.co.za" style="color:#1a5fa8;text-decoration:none">quantumberryai.co.za</a>  ·  Cape Town, South Africa</td></tr>', "38px 0 0 0"))
h.append(tbl('<tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" align="center"><tbody><tr><td style="width:36px;height:2px;background-color:#c0392b;line-height:2px;font-size:0"> </td></tr></tbody></table></td></tr>'
  f'<tr><td align="center" style="padding:20px 0 0 0;{F}font-size:10.5px;letter-spacing:2.8px;color:#8a8a80;text-transform:uppercase">INTELLIGENT SYSTEMS.</td></tr>'
  f'<tr><td align="center" style="padding:7px 0 0 0;{F}font-size:10.5px;letter-spacing:2.8px;color:#c0392b;text-transform:uppercase">REAL WORLD IMPACT.</td></tr>', "40px 0 0 0"))
h.append('</td></tr></tbody></table></td></tr></tbody></table>')
doc = "".join(h)
open(os.path.join(here, "email_karen.html"), "w").write(doc)
# preview copy with the logo inlined
b64 = ""
txt = f"""[ATTACH Titans-Kit-Design-Prompt-Pack.pdf BEFORE SENDING, then delete this line]

QUANTUMBERRY AI
From design to automation, we make technology think for you.

Designing the
new Titans kit

Hi Karen,

The prompt pack for the new men's and women's playing shirts and pants is attached. It works in both Gemini and ChatGPT, and it fixes the two things we spoke about: logos coming out wrong, and small edits redoing the whole design.

You start with a storyboard of each idea, pick the best one, and refine it step by step. The official logo files are always used, so the logos stay intact.

ATTACHED
Titans Kit Design Prompt Pack
PDF, 8 pages, copy-paste prompts

— What is inside
Step 1: Storyboard of each shirt idea: front, back, side, pants and details
Step 2: Clean drawings for the supplier, with blank logo spaces
Step 3: A photo of a player wearing the kit
Step 4: Small edits without redoing the design
Logos: Always the official files, placed last by hand

— Next step
Let's do a short call. I will take you through the prompts and run the first storyboard with you.
Please have the official logo files (transparent PNGs) and the brand colour codes ready.

Book our call: {BOOK}
or simply reply with a time that suits you.

When you have a moment, could you also send the clothing inventory sheets with the player lists and item costs? That is what populates the stock-take app.

Chat soon,
Chad Douglas
Founder & CEO | QuantumBerry AI
chad@quantumberryai.co.za
quantumberryai.co.za · Cape Town, South Africa

INTELLIGENT SYSTEMS.
REAL WORLD IMPACT.
"""
open(os.path.join(here, "email_karen.txt"), "w").write(txt)
