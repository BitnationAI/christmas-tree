import json, html
LOGO = {
  "source": "ATTACHED OFFICIAL LOGO FILES",
  "strictness": "Critical",
  "instruction": "Reproduce every attached logo exactly as supplied: identical shapes, letters, colours, spacing and proportions. Never redraw, restyle, recolour, simplify, warp, crop, outline or add effects. Scale uniformly only. Logos sit flat on the fabric following its curve, nothing more.",
  "if_unsure": "Leave a clean blank rectangle labelled with the logo file name instead of guessing."
}
P1 = {
  "meta": {"role": "Senior sportswear designer creating a professional kit concept board", "output": "One landscape concept board, 16:9, clean studio presentation"},
  "brief": {"team": "{TEAM}", "concept_name": "{CONCEPT_NAME}", "theme": "{THEME}", "format": "{FORMAT} coloured cricket playing kit",
            "colours": {"primary": "{PRIMARY_HEX}", "secondary": "{SECONDARY_HEX}", "accent": "{ACCENT_HEX}"},
            "pattern_idea": "{PATTERN_IDEA}, integrated subtly into side panels and sleeves, never over logo areas"},
  "board_layout": {
    "panel_1": "Hero front view of the playing shirt, flat lay, perfectly symmetrical",
    "panel_2": "Back view of the shirt with player name across the shoulders and a large number centred",
    "panel_3": "Side view showing sleeve, side panel and seam lines",
    "panel_4": "Cricket playing pants, front and back views, matching panels and piping",
    "panel_5": "Detail close-ups: collar, sleeve cuff, fabric texture (breathable athletic mesh), side vent, waistband",
    "panel_6": "Colour chips with hex codes and a sample of the number and lettering font",
    "panel_7": "Small mood image of a professional cricketer wearing the kit in a floodlit stadium"
  },
  "garment_specs": {
    "shirt": "Short sleeve, modern athletic cut, polo or V collar with placket, raglan sleeves, ventilated mesh side panels, sublimated print",
    "pants": "Tapered cricket playing trousers, elasticated waist with drawcord, side panels in kit colours, piping down the outer leg",
    "fit": "{FIT}"
  },
  "logo_placement": {
    "left_chest": "TITANS_CREST.png",
    "centre_chest": "{MAIN_SPONSOR_FILE}",
    "right_chest": "KIT_SUPPLIER.png",
    "sleeve": "Secondary sponsor file if attached, otherwise leave blank",
    "pants_left_thigh": "TITANS_CREST.png, small"
  },
  "logo_rules": LOGO,
  "style": {"render": "Photorealistic fabric with realistic seams, stitching and drape, clean neutral grey studio background, soft even lighting",
            "presentation": "Premium sportswear brand concept board, tidy grid, small panel labels"},
  "negative_constraints": ["No redrawn or invented logos", "No extra sponsors", "No misspelt text", "No cartoon style", "No distorted garments", "No pattern over logo areas", "No watermarks"],
  "combined_prompt_text": "Professional sportswear concept board, 16:9, for the {TEAM} {FORMAT} cricket playing kit, concept '{CONCEPT_NAME}', theme {THEME}, colours {PRIMARY_HEX} / {SECONDARY_HEX} / {ACCENT_HEX}, {FIT}. Panels: front shirt, back shirt with name and number, side view, pants front and back, detail close-ups, colour chips, small on-player mood shot. Use the attached official logo files exactly as supplied in the stated positions, never redrawn or restyled; if unsure, leave a labelled blank box. Photoreal fabric, clean grey studio background."
}
P2 = {
  "meta": {"role": "Technical sportswear designer preparing flats for a kit supplier", "output": "Two images: 1) shirt front, back and side; 2) pants front and back. White background, 4:3"},
  "reference": {"source": "ATTACHED CHOSEN STORYBOARD", "strictness": "Critical", "instruction": "Keep the design, colours, panels, pattern and proportions exactly as in the chosen concept."},
  "style": "Clean technical flat illustration, precise outlines, accurate seams and stitch lines, flat colour fills using the exact hex codes, no shading, no model",
  "logo_zones": {"instruction": "Do NOT draw any logo. Leave each logo position as a clean white rectangle with a thin grey border and a small label.",
                 "zones": ["LEFT CHEST: TITANS CREST", "CENTRE CHEST: MAIN SPONSOR", "RIGHT CHEST: KIT SUPPLIER", "SLEEVE: SECONDARY SPONSOR", "PANTS LEFT THIGH: TITANS CREST"]},
  "annotations": ["Collar style", "Fabric: breathable athletic mesh", "Panel colours with hex codes", "Name and number area on the back"],
  "negative_constraints": ["No logos or brand marks of any kind", "No invented text", "No perspective distortion", "No background scenery"],
  "combined_prompt_text": "Technical flats of the attached chosen Titans kit concept, design unchanged. Image 1: shirt front, back and side. Image 2: pants front and back. White background, precise outlines, exact hex colour fills, no shading. Do not draw any logos: leave a labelled blank rectangle at each logo position. Add short annotations for collar, fabric and panel colours."
}
P3 = {
  "meta": {"role": "Elite sports campaign photographer and retoucher", "output": "One photorealistic campaign image, 9:16 vertical"},
  "subject": {"who": "Adult professional cricketer, {CRICKETER}", "skin_and_face": "Natural skin texture, real sweat sheen, focused determined expression"},
  "wardrobe": {"source": "ATTACHED CHOSEN KIT DESIGN", "strictness": "Critical", "instruction": "Dress the player in the attached kit exactly: same colours, panels, pattern, collar and pants. Fabric stretches and folds naturally with the movement."},
  "logo_rules": LOGO,
  "action": {"pose": "{ACTION}", "perspective": "Connected forced perspective: body, arm, hand and bat or ball form one continuous believable line toward the camera", "motion": "Frozen peak moment, fine dust or grass flecks in the air"},
  "typography": {"main_word": "{MAIN_WORD}", "style": "Huge bold condensed letters behind the player, colour {ACCENT_HEX}, partly hidden by the player's body for depth", "rule": "Spell the word exactly, no other text anywhere"},
  "environment": {"setting": "{ENVIRONMENT}", "framing": "Full-bleed stadium background, no borders, no footer band"},
  "lighting": "Dramatic floodlight rim light outlining the player, soft fill on the face, crisp contrast",
  "camera": {"lens": "35mm", "aspect_ratio": "9:16", "focus": "Tack-sharp on the player and kit, background gently blurred"},
  "negative_constraints": ["No floating or duplicated equipment", "No distorted hands or extra fingers", "No plastic or airbrushed skin", "No redrawn, warped or invented logos", "No extra sponsors", "No footer band or frame", "No misspelt text"],
  "combined_prompt_text": "Photorealistic 9:16 cricket campaign image of an adult professional cricketer, {CRICKETER}, {ACTION}, wearing the attached Titans kit exactly as designed. Connected forced perspective toward the camera, frozen peak moment. Huge condensed word '{MAIN_WORD}' in {ACCENT_HEX} behind the player, partly hidden by the body. {ENVIRONMENT}, full-bleed stadium, floodlight rim light, 35mm, tack-sharp subject. Use the attached official logo files exactly as supplied, never redrawn. No distorted hands, no floating equipment, no plastic skin, no footer band."
}
P4 = {
  "edit_mode": "Surgical edit of the attached image",
  "change_only": "{ONE CHANGE, for example: make the collar {ACCENT_HEX}}",
  "keep_identical": ["Every logo, pixel for pixel", "All other colours", "Pattern and panel layout", "Garment shape and proportions", "Background, lighting and camera angle"],
  "rule": "If the change would affect anything in keep_identical, change less, not more."
}
prompts = [
 ("Prompt 1, the storyboard (start here)", "Run this three times with three different themes, then pick the strongest board. Fill in the {CURLY} parts first.",
  "Fill in: CONCEPT_NAME (e.g. Northern Thunder) · THEME (pride of the north, lightning, heritage, modern speed, fan culture) · TEAM (Momentum Multiply Titans or Fidelity Titans) · FIT (men's athletic fit or women's tailored fit) · MAIN_SPONSOR_FILE (MOMENTUM_MULTIPLY.png or FIDELITY.png) · PRIMARY_HEX, SECONDARY_HEX, ACCENT_HEX · PATTERN_IDEA · FORMAT (one-day or T20).", P1),
 ("Prompt 2, production flats with blank logo zones", "Attach the storyboard you picked. The AI draws the clean supplier flats and deliberately leaves the logo spaces empty, so the real logos go in afterwards.", None, P2),
 ("Prompt 3, on-player hero shot", "Attach the chosen kit image plus the logo files. This gives the team a real-looking photo for sign-off and for social media.",
  "Fill in: CRICKETER (e.g. fast bowler, mid-20s) · ACTION (e.g. at the point of delivery) · MAIN_WORD (RISE, ROAR, TITANS or BELIEVE) · ENVIRONMENT (e.g. floodlit night match at a packed stadium) · ACCENT_HEX.", P3),
 ("Prompt 4, small changes without redoing everything", "Attach the image you want to adjust. One change per message. In ChatGPT, use the select tool to paint over only the area you want changed.", None, P4),
]
F = "font-family:Georgia,'Times New Roman',serif;"
def p(t, top=16): return f'<div style="{F}font-size:15px;line-height:24px;color:#1c1a18;padding-top:{top}px">{t}</div>'
def step(n, t): return f'<tr><td style="{F}font-size:14px;line-height:21px;color:#c0392b;font-weight:bold;vertical-align:top;padding:5px 10px 5px 0;width:18px">{n}</td><td style="{F}font-size:14px;line-height:21px;color:#2a2724;padding:5px 0">{t}</td></tr>'
PRE = "background-color:#0f1115;color:#e8e6e3;font-family:'Courier New',Courier,monospace;font-size:12px;line-height:17px;padding:14px 16px;margin:8px 0 22px 0;white-space:pre-wrap;word-wrap:break-word;word-break:break-word;border-left:3px solid #c0392b"
steps = [
 ("0", "<strong>One-time setup.</strong> Make a Gemini Gem or a ChatGPT Project called \"Titans Kit Design\". Upload the official logos as transparent PNGs named clearly (TITANS_CREST.png, MOMENTUM_MULTIPLY.png, FIDELITY.png, KIT_SUPPLIER.png), the brand colour codes, and front, back and side photos of the current kit. Then <strong>also attach the logo files to every image prompt</strong>; the image tools follow attached files far more reliably than stored ones."),
 ("1", "<strong>Storyboard</strong> (Prompt 1). One page per idea: front, back, side, pants, details, colours and a mood shot. Make three, pick one."),
 ("2", "<strong>Production flats</strong> (Prompt 2). Clean front, back and side drawings of the chosen kit with blank, labelled logo spaces."),
 ("3", "<strong>On-player hero shot</strong> (Prompt 3). A photoreal image of a player in the kit for sign-off and social media."),
 ("4", "<strong>Small changes</strong> (Prompt 4). One change per message so the AI never redoes the whole design."),
 ("5", "<strong>Logo check and finish.</strong> Zoom to 100% and compare every logo with the original file; reject anything with a changed letter or shape. Before anything goes to the supplier, place the real logo files on the flats in Canva or Illustrator."),
]
h = []
h.append('<div style="margin:0;padding:0;background-color:#f4f3f1"><div style="max-width:640px;margin:0 auto;background-color:#f4f3f1;padding:28px 18px">')
h.append(f'<div style="text-align:center;padding:6px 0 2px 0"><div style="{F}font-size:19px;letter-spacing:6px;color:#0a0a0a">QUANTUMBERRY AI</div><div style="{F}font-size:13px;font-style:italic;color:#5a5651;padding-top:9px">From design to automation, we make technology think for you.</div></div>')
h.append('<div style="height:2px;background-color:#c0392b;margin:18px 0 0 0;line-height:2px;font-size:0"> </div><div style="background-color:#ffffff;padding:30px 30px 26px 30px">')
h.append(f'<div style="background-color:#f7f9fb;border-top:3px solid #1a7fbf;padding:16px 18px;margin:0 0 24px 0"><div style="{F}font-size:11px;letter-spacing:2px;color:#1a7fbf;padding-bottom:9px">IN BRIEF</div><div style="{F}font-size:14px;line-height:21px;color:#2a2724">A better way to design the new men\'s and women\'s playing shirts and pants: start with a storyboard, then refine. Four detailed copy-paste prompts that work in Gemini and ChatGPT, each with strict logo rules built in, plus a final step that guarantees the logos are 100% correct.</div></div>')
h.append(p("Hi Karen,", 0))
h.append(p("I have replaced the short prompts I sent earlier with a proper kit-design pack. It tackles the two problems you hit on our call: the logos coming out wrong, and small edits redoing the whole design."))
h.append(p("<strong>Why a storyboard first.</strong> Instead of generating one shirt at a time, each prompt produces a full concept board: front, back, side, pants, close-ups, colours and a player wearing it. You and the team can compare three directions side by side on one page each, pick one, and every later step uses that board as the fixed reference."))
h.append(p("<strong>Why the prompts look like code.</strong> They are written in JSON, a structured format both Gemini and ChatGPT read very well. Every detail sits in its own labelled field, so nothing gets forgotten. Just copy the whole block, swap the words in {CURLY BRACKETS} for your choices, and paste it in with the logo files attached. Each one also ends with a plain-English summary line that reinforces the brief."))
h.append(p("<strong>How the logos stay intact.</strong> Two layers. Every prompt carries strict logo rules and uses the attached official files, which gets them right most of the time. Because image AI can still slightly redraw a logo, the supplier drawings leave the logo spaces blank and the real files are placed on top at the end. That last step is what makes them 100% correct."))
h.append(f'<div style="{F}font-size:11px;letter-spacing:2px;color:#1a7fbf;padding:26px 0 8px 0">THE WORKFLOW</div><table cellpadding="0" cellspacing="0" border="0" style="width:100%">' + "".join(step(n,t) for n,t in steps) + '</table>')
h.append(f'<div style="{F}font-size:11px;letter-spacing:2px;color:#1a7fbf;padding:26px 0 4px 0">THE PROMPTS</div>')
for title, intro, fill, obj in prompts:
    h.append(f'<div style="{F}font-size:15px;line-height:24px;color:#1c1a18;padding-top:14px"><span style="color:#c0392b;font-weight:bold">—</span>  <strong>{html.escape(title)}</strong></div>')
    h.append(f'<div style="{F}font-size:14px;line-height:21px;color:#5a5651;padding-top:4px">{html.escape(intro)}</div>')
    if fill: h.append(f'<div style="{F}font-size:13px;line-height:20px;color:#2a2724;background-color:#f7f6f4;padding:10px 12px;margin-top:8px">{html.escape(fill)}</div>')
    h.append(f'<pre style="{PRE}">{html.escape(json.dumps(obj, indent=2, ensure_ascii=False))}</pre>')
h.append(p("<strong>Women's kit.</strong> Run Prompt 1 again with TEAM set to Fidelity Titans, FIT set to women's tailored fit and MAIN_SPONSOR_FILE set to FIDELITY.png. Keep the same concept name and colours so the two kits read as one family.", 6))
h.append(p("<strong>Gemini or ChatGPT?</strong> Both work. Gemini (choose the image model in the Gem) tends to hold a design steadier across edits; ChatGPT's select tool is the easiest way to change one small area. Try the same storyboard prompt in both and keep whichever you like."))
h.append(p("Once Tukisi sends me the front, back and side photos of the current shirts, I will run a sample through myself and send you the result so you can see what good output looks like."))
h.append(p("When you have a moment, could you also send through the clothing inventory sheets with the player lists and item costs. That is what populates the stock-take app so you are testing it on your real data rather than dummy entries."))
h.append('<div style="height:1px;background-color:#e4e1dd;margin:26px 0 20px 0;line-height:1px;font-size:0"> </div>')
h.append(f'<div style="{F}font-size:14px;line-height:21px;color:#1c1a18">Chad Douglas<br><span style="color:#5a5651">Founder &amp; CEO, QuantumBerry AI</span><br><a href="https://quantumberryai.co.za" style="color:#1a7fbf;text-decoration:none">quantumberryai.co.za</a></div></div>')
h.append(f'<div style="background-color:#0a0a0a;padding:17px 20px;text-align:center"><div style="{F}font-size:12px;letter-spacing:2px;color:#f2f0ed">INTELLIGENT SYSTEMS. REAL WORLD IMPACT.</div></div></div></div>')
open("email.html","w").write("".join(h))
# plain text
import re
t = ["Hi Karen,", "",
"I have replaced the short prompts I sent earlier with a proper kit-design pack. It tackles the two problems you hit on our call: the logos coming out wrong, and small edits redoing the whole design.", "",
"Why a storyboard first: each prompt produces a full concept board (front, back, side, pants, close-ups, colours and a player wearing it). Make three, compare them, pick one, and every later step uses that board as the fixed reference.", "",
"Why the prompts look like code: they are JSON, a structured format Gemini and ChatGPT both read very well. Copy the whole block, swap the words in {CURLY BRACKETS} for your choices, and paste it in with the logo files attached.", "",
"How the logos stay intact: every prompt carries strict logo rules and uses the attached official files. Because image AI can still slightly redraw a logo, the supplier drawings leave the logo spaces blank and the real files are placed on top at the end.", "",
"THE WORKFLOW", ""]
for n, s in steps: t.append(f"{n}. " + re.sub("<[^>]+>", "", s).replace("&quot;", '"'))
t += ["", "THE PROMPTS", ""]
for title, intro, fill, obj in prompts:
    t += [title.upper(), intro]
    if fill: t.append(fill)
    t += ["", json.dumps(obj, indent=2, ensure_ascii=False), ""]
t += ["Women's kit: run Prompt 1 again with TEAM = Fidelity Titans, FIT = women's tailored fit and MAIN_SPONSOR_FILE = FIDELITY.png. Keep the same concept name and colours so the two kits read as one family.", "",
"Gemini or ChatGPT? Both work. Gemini tends to hold a design steadier across edits; ChatGPT's select tool is the easiest way to change one small area. Try the same storyboard prompt in both.", "",
"Once Tukisi sends me the front, back and side photos of the current shirts, I will run a sample through myself and send you the result so you can see what good output looks like.", "",
"When you have a moment, could you also send through the clothing inventory sheets with the player lists and item costs. That is what populates the stock-take app so you are testing it on your real data rather than dummy entries.", "",
"Chad Douglas", "Founder & CEO, QuantumBerry AI", "quantumberryai.co.za"]
open("email.txt","w").write("\n".join(t))
for _,_,_,o in prompts: json.loads(json.dumps(o))
print(len(open("email.html").read()), len(open("email.txt").read()))
