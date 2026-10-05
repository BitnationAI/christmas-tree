import re, subprocess, sys
HEAD = '''<div class="hd"><div class="brand"><img src="assets/emblem.png" alt=""><div><b>QuantumBerry AI</b><small>APPLIED AI ENGINEERING</small></div></div><div class="r">PARTNER INTRODUCTION<br>NO. QB-PI-2026-01</div></div><div class="hdrule"></div>'''
def foot(n):
    return f'<div class="ft"><span>QuantumBerry AI</span><span>Partner Introduction &nbsp;·&nbsp; 2026 &nbsp;·&nbsp; quantumberryai.co.za</span><b>{n}</b></div>'
s = open("template.html").read()
s = s.replace("{{HEAD}}", HEAD)
s = re.sub(r"\{\{FOOT:(\d+)\}\}", lambda m: foot(m.group(1)), s)
open("QuantumBerry-AI-Introduction.html", "w").write(s)
CH = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
subprocess.run([CH, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                "--allow-file-access-from-files", "--print-to-pdf=QuantumBerry-AI-Introduction.pdf",
                "file://" + __import__("os").getcwd() + "/QuantumBerry-AI-Introduction.html"],
               stderr=subprocess.DEVNULL)
