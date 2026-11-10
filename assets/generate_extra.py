"""Terminal-session and defense-in-depth SVGs for the profile README."""
import sys
from pathlib import Path
from xml.sax.saxutils import escape

out = Path(sys.argv[1])
SANS = "'Segoe UI', Ubuntu, 'Helvetica Neue', Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'JetBrains Mono', Menlo, Consolas, monospace"
BG = """<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0B1A20"/><stop offset="0.55" stop-color="#132C35"/><stop offset="1" stop-color="#1D4250"/></linearGradient>
    <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="#7FDBCA" stroke-opacity="0.07"/></pattern>"""


def pct(t, cycle):
    return round(t / cycle * 100, 3)


# =============================================================== terminal session
CYCLE = 17.0
CW = 10.25                      # approx. advance of one 17px monospace glyph
lines = [  # (kind, text, start-second, colour)
    ("cmd", "kubectl get pods -n secureship", 0.4, None),
    ("out", "NAME                        READY   STATUS    AGE", 1.7, "#6F8790"),
    ("out", "backend-6f9c8d7b5-x2kq9     1/1     Running   12d", 1.9, "#C9D7DC"),
    ("out", "worker-7c4b9f6d8-m8z1p      1/1     Running   12d", 2.05, "#C9D7DC"),
    ("out", "frontend-5d8f7c9b4-q7w3e    1/1     Running   12d", 2.2, "#C9D7DC"),
    ("cmd", "trivy image --severity HIGH,CRITICAL secureship-backend", 3.2, None),
    ("ok", "Total: 0 (HIGH: 0, CRITICAL: 0)", 5.0, "#3FB950"),
    ("cmd", "cosign verify ghcr.io/jav1d006/secureship-backend", 6.0, None),
    ("ok", "Verified OK: signature and transparency log entry", 7.8, "#3FB950"),
    ("cmd", "echo $NEXT_ROLE", 8.8, None),
    ("role", "DevSecOps Engineer @ your-team", 9.9, "#5EEAD4"),
]
TOP, STEP, LEFT = 92, 29, 40
H = TOP + STEP * len(lines) + 34
css, body, clips = [], [], []
for i, (kind, text, t, col) in enumerate(lines):
    y = TOP + i * STEP
    a = pct(t, CYCLE)
    css.append(f"@keyframes l{i}{{0%,{max(a - 0.01, 0)}%{{opacity:0}}{a}%,95%{{opacity:1}}100%{{opacity:0}}}}.l{i}{{animation:l{i} {CYCLE}s linear infinite}}")
    if kind == "cmd":
        w = (len(text) + 2) * CW + 6
        typ_end = pct(t + 0.035 * len(text) + 0.2, CYCLE)
        css.append(f"@keyframes w{i}{{0%,{a}%{{width:0}}{typ_end}%,95%{{width:{w:.0f}px}}100%{{width:0}}}}"
                   f".w{i}{{animation:w{i} {CYCLE}s infinite;animation-timing-function:steps({len(text) + 2},end)}}")
        clips.append(f'<clipPath id="c{i}"><rect class="w{i}" x="{LEFT}" y="{y - 20}" width="0" height="28"/></clipPath>')
        body.append(f'<g class="l{i}"><g clip-path="url(#c{i})"><text x="{LEFT}" y="{y}"><tspan fill="#5EEAD4">❯</tspan> '
                    f'<tspan fill="#E6EDF3">{escape(text)}</tspan></text></g></g>')
    elif kind == "ok":
        body.append(f'<g class="l{i}"><text x="{LEFT}" y="{y}" fill="{col}">✔ <tspan fill="#C9F5D6">{escape(text)}</tspan></text></g>')
    elif kind == "role":
        cx = LEFT + len(text) * CW + 8
        body.append(f'<g class="l{i}"><text x="{LEFT}" y="{y}" fill="{col}" font-weight="700">{escape(text)}</text>'
                    f'<rect class="blink" x="{cx:.0f}" y="{y - 16}" width="10" height="20" fill="#5EEAD4"/></g>')
    else:
        body.append(f'<g class="l{i}"><text x="{LEFT}" y="{y}" fill="{col}" xml:space="preserve">{escape(text)}</text></g>')

terminal = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{H}" viewBox="0 0 1200 {H}" role="img" aria-labelledby="tt td">
  <title id="tt">A day in production</title>
  <desc id="td">kubectl shows healthy pods, trivy finds no HIGH or CRITICAL vulnerabilities, cosign verifies the image signature, and the next role is DevSecOps Engineer at your team.</desc>
  <defs>{BG}<clipPath id="card"><rect width="1200" height="{H}" rx="14"/></clipPath>{''.join(clips)}</defs>
  <style>
    text {{ font-family: {MONO}; font-size: 17px; white-space: pre; }}
    .blink {{ animation: blink 1s step-end infinite; }} @keyframes blink {{ 50% {{ opacity: 0; }} }}
    {''.join(css)}
    @media (prefers-reduced-motion: reduce) {{ g[class^="l"], rect[class^="w"], .blink {{ animation: none !important; opacity: 1; }} rect[class^="w"] {{ width: 1200px; }} }}
  </style>
  <g clip-path="url(#card)">
    <rect width="1200" height="{H}" fill="#0A1418"/>
    <rect width="1200" height="44" fill="#122329"/>
  </g>
  <rect x="0.5" y="0.5" width="1199" height="{H - 1}" rx="14" fill="none" stroke="#7FDBCA" stroke-opacity="0.22"/>
  <circle cx="26" cy="22" r="6.5" fill="#FF5F57"/><circle cx="48" cy="22" r="6.5" fill="#FEBC2E"/><circle cx="70" cy="22" r="6.5" fill="#28C840"/>
  <text x="600" y="27" text-anchor="middle" fill="#7C949D" style="font-size:14px">javid@prod-cluster: ~</text>
  {''.join(body)}
</svg>
"""
(out / "terminal.svg").write_text(terminal)

# =============================================================== defense in depth
W, H2 = 1200, 400
mid = 190
nodes = [  # id, x, y, title, subtitle
    ("internet", 105, mid, "internet", "untrusted"),
    ("ingress", 365, mid, "ingress-nginx", "rate limits · headers"),
    ("api", 610, mid, "api", "non-root · read-only"),
    ("db", 870, 125, "postgres", "secret out of git"),
    ("job", 870, 268, "scan job", "no network · no creds"),
]
pos = {n[0]: (n[1], n[2]) for n in nodes}
good_path = f"M{pos['internet'][0] + 52} {mid} L{pos['ingress'][0] - 70} {mid} M{pos['ingress'][0] + 70} {mid} L{pos['api'][0] - 70} {mid}"
p_in = f"M157 {mid} L{pos['api'][0]} {mid} L{pos['db'][0] - 70} 125"
p_job = f"M157 {mid} L{pos['api'][0]} {mid} L{pos['job'][0] - 70} 268"
# attacks: straight at the database, and the scan job trying to phone home
atk1 = f"M157 {mid + 22} C 300 330, 560 345, 700 300"
atk2 = f"M{pos['job'][0] + 70} 268 C 1000 268, 1040 250, 1085 250"


def node(nid, x, y, title, sub):
    if nid == "internet":
        return f"""
  <g transform="translate({x} {y})">
    <circle r="50" fill="#2B1418" fill-opacity="0.6" stroke="#F85149" stroke-opacity="0.55" stroke-width="2"/>
    <path d="M-24 6 a14 14 0 0 1 4 -27 a18 18 0 0 1 33 4 a12 12 0 0 1 11 23 z" fill="none" stroke="#FF7B72" stroke-width="3" stroke-linejoin="round"/>
    <text y="82" text-anchor="middle" class="t">{title}</text><text y="102" text-anchor="middle" class="s">{sub}</text>
  </g>"""
    return f"""
  <g transform="translate({x} {y})">
    <rect x="-70" y="-30" width="140" height="60" rx="12" fill="#10252C" stroke="#5EEAD4" stroke-opacity="0.75" stroke-width="2"/>
    <text y="6" text-anchor="middle" class="t">{title}</text>
    <text y="52" text-anchor="middle" class="s">{sub}</text>
  </g>"""


def packet(path, dur, begin, color="#5EEAD4", r=6):
    return f"""<circle r="{r}" fill="{color}" opacity="0"><animateMotion dur="{dur}s" begin="{begin}s" repeatCount="indefinite" path="{path}"/>
    <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.08;0.9;1" dur="{dur}s" begin="{begin}s" repeatCount="indefinite"/></circle>"""


def attack(path, dur, begin, wall_x, wall_y, label, left=False):
    bw = len(label) * 8.4 + 16
    bx = -16 - bw if left else 16
    return f"""
  <circle r="7" fill="#F85149" opacity="0"><animateMotion dur="{dur}s" begin="{begin}s" repeatCount="indefinite" keyPoints="0;1;1" keyTimes="0;0.55;1" calcMode="linear" path="{path}"/>
    <animate attributeName="opacity" values="0;1;1;0;0" keyTimes="0;0.05;0.55;0.6;1" dur="{dur}s" begin="{begin}s" repeatCount="indefinite"/></circle>
  <g transform="translate({wall_x} {wall_y})" opacity="0">
    <animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;0.54;0.57;0.85;1" dur="{dur}s" begin="{begin}s" repeatCount="indefinite"/>
    <circle r="20" fill="#F85149" fill-opacity="0.18"><animate attributeName="r" values="8;30" dur="{dur}s" begin="{begin}s" repeatCount="indefinite" keyTimes="0;1" calcMode="spline" keySplines=".2 .8 .2 1"/></circle>
    <path d="M-8 -8 L8 8 M8 -8 L-8 8" stroke="#FF7B72" stroke-width="4" stroke-linecap="round"/>
    <rect x="{bx:.0f}" y="-60" width="{bw:.0f}" height="26" rx="6" fill="#3A1418" stroke="#F85149" stroke-opacity="0.7"/>
    <text x="{bx + 8:.0f}" y="-42" class="deny">{label}</text>
  </g>"""


defense = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H2}" viewBox="0 0 {W} {H2}" role="img" aria-labelledby="dt dd">
  <title id="dt">Defense in depth</title>
  <desc id="dd">Legitimate traffic flows from the internet through ingress to the API and database. An attacker going straight for the database and a scan job trying to reach the internet are both denied by default-deny NetworkPolicies.</desc>
  <defs>{BG}<clipPath id="card"><rect width="{W}" height="{H2}" rx="18"/></clipPath></defs>
  <style>
    .t {{ font-family: {SANS}; font-size: 17px; font-weight: 600; fill: #E6EDF3; }}
    .s {{ font-family: {MONO}; font-size: 12px; fill: #7C949D; }}
    .lbl {{ font-family: {MONO}; font-size: 13px; fill: #5EEAD4; }}
    .deny {{ font-family: {MONO}; font-size: 13px; font-weight: 700; fill: #FF7B72; }}
    .flow {{ stroke-dasharray: 6 8; animation: flow 1.2s linear infinite; }}
    @keyframes flow {{ to {{ stroke-dashoffset: -28; }} }}
    @media (prefers-reduced-motion: reduce) {{ .flow {{ animation: none; }} }}
  </style>
  <g clip-path="url(#card)"><rect width="{W}" height="{H2}" fill="url(#bg)"/><rect width="{W}" height="{H2}" fill="url(#grid)"/></g>
  <rect x="0.5" y="0.5" width="{W - 1}" height="{H2 - 1}" rx="18" fill="none" stroke="#7FDBCA" stroke-opacity="0.18"/>

  <!-- cluster boundary -->
  <rect x="240" y="58" width="930" height="300" rx="16" fill="#0B1A20" fill-opacity="0.45" stroke="#5EEAD4" stroke-opacity="0.35" stroke-dasharray="8 6"/>
  <text x="262" y="84" class="lbl">kubernetes · namespace secureship · default-deny</text>
  <text x="32" y="38" class="lbl" fill="#5EEAD4">$ kubectl get networkpolicy</text>
  <text x="{W - 32}" y="38" text-anchor="end" class="s">only what is allowed gets through</text>

  <!-- allowed routes -->
  <path d="M157 {mid} H{pos['ingress'][0] - 70}" stroke="#5EEAD4" stroke-opacity="0.45" stroke-width="2.5" class="flow" fill="none"/>
  <path d="M{pos['ingress'][0] + 70} {mid} H{pos['api'][0] - 70}" stroke="#5EEAD4" stroke-opacity="0.45" stroke-width="2.5" class="flow" fill="none"/>
  <path d="M{pos['api'][0] + 70} {mid} L{pos['db'][0] - 70} 125" stroke="#5EEAD4" stroke-opacity="0.45" stroke-width="2.5" class="flow" fill="none"/>
  <path d="M{pos['api'][0] + 70} {mid} L{pos['job'][0] - 70} 268" stroke="#5EEAD4" stroke-opacity="0.25" stroke-width="2" stroke-dasharray="3 6" fill="none"/>

  <!-- walls -->
  <line x1="700" y1="262" x2="700" y2="345" stroke="#F85149" stroke-opacity="0.8" stroke-width="3" stroke-linecap="round"/>
  <text x="712" y="342" class="s" fill="#FF7B72">netpol: deny</text>
  <line x1="1085" y1="200" x2="1085" y2="300" stroke="#F85149" stroke-opacity="0.8" stroke-width="3" stroke-linecap="round"/>
  <text x="1085" y="322" text-anchor="middle" class="s" fill="#FF7B72">egress: deny</text>

  {''.join(node(*n) for n in nodes)}

  <!-- legit packets -->
  {packet(p_in, 3.6, 0)}
  {packet(p_in, 3.6, 1.2)}
  {packet(p_in, 3.6, 2.4)}
  {packet(p_job, 4.8, 0.6, "#8FE3D7", 4.5)}

  <!-- attacks -->
  {attack(atk1, 5.0, 0.8, 700, 300, "DENIED")}
  {attack(atk2, 5.0, 3.3, 1085, 250, "BLOCKED", left=True)}
</svg>
"""
(out / "defense.svg").write_text(defense)
print("ok")
