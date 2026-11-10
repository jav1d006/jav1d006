"""Generate the self-hosted SVG assets for the profile README."""
import sys
from pathlib import Path

out = Path(sys.argv[1])
out.mkdir(parents=True, exist_ok=True)

SANS = "'Segoe UI', Ubuntu, 'Helvetica Neue', Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'JetBrains Mono', Menlo, Consolas, monospace"
BG = """
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0B1A20"/>
      <stop offset="0.55" stop-color="#132C35"/>
      <stop offset="1" stop-color="#1D4250"/>
    </linearGradient>
    <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M32 0H0V32" fill="none" stroke="#7FDBCA" stroke-opacity="0.07"/>
    </pattern>"""

# ------------------------------------------------------------------ header
header = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="340" viewBox="0 0 1200 340" role="img" aria-labelledby="t d">
  <title id="t">Javid Mamedov</title>
  <desc id="d">DevSecOps Engineer: Kubernetes, GitOps and secure CI/CD</desc>
  <defs>{BG}
    <radialGradient id="glow" cx="0.82" cy="0.45" r="0.45">
      <stop offset="0" stop-color="#2DD4BF" stop-opacity="0.28"/>
      <stop offset="1" stop-color="#2DD4BF" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="scan" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#2DD4BF" stop-opacity="0"/>
      <stop offset="1" stop-color="#2DD4BF" stop-opacity="0.16"/>
    </linearGradient>
    <linearGradient id="name" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#FFFFFF"/>
      <stop offset="1" stop-color="#B9F3EA"/>
    </linearGradient>
    <clipPath id="card"><rect width="1200" height="340" rx="18"/></clipPath>
    <clipPath id="type"><rect class="typing" x="72" y="62" width="0" height="30"/></clipPath>
  </defs>
  <style>
    .typing {{ animation: type 2.4s steps(26, end) 0.3s forwards; }}
    .cursor {{ animation: follow 2.4s steps(26, end) 0.3s forwards, blink 1s step-end 2.7s infinite; }}
    .scanline {{ animation: scan 5s ease-in-out infinite; }}
    .ring {{ transform-origin: 985px 168px; animation: pulse 3s ease-out infinite; opacity: 0; }}
    .ring2 {{ animation-delay: 1.5s; }}
    .fade {{ opacity: 0; animation: fade 0.9s ease-out forwards; }}
    .f1 {{ animation-delay: 0.2s; }} .f2 {{ animation-delay: 0.6s; }} .f3 {{ animation-delay: 1s; }} .f4 {{ animation-delay: 1.4s; }}
    @keyframes type {{ to {{ width: 352px; }} }}
    @keyframes blink {{ 50% {{ opacity: 0; }} }}
    @keyframes follow {{ from {{ transform: translateX(0); }} to {{ transform: translateX(348px); }} }}
    @keyframes scan {{ 0% {{ transform: translateY(-140px); }} 100% {{ transform: translateY(380px); }} }}
    @keyframes pulse {{ 0% {{ transform: scale(0.85); opacity: 0.55; }} 100% {{ transform: scale(1.6); opacity: 0; }} }}
    @keyframes fade {{ from {{ opacity: 0; transform: translateY(8px); }} to {{ opacity: 1; transform: none; }} }}
    @media (prefers-reduced-motion: reduce) {{
      .typing {{ animation: none; width: 352px; }}
      .scanline, .ring {{ animation: none; }} .cursor {{ animation: none; transform: translateX(348px); }}
      .fade {{ animation: none; opacity: 1; }}
    }}
  </style>
  <g clip-path="url(#card)">
    <rect width="1200" height="340" fill="url(#bg)"/>
    <rect width="1200" height="340" fill="url(#grid)"/>
    <rect width="1200" height="340" fill="url(#glow)"/>
    <rect class="scanline" y="0" width="1200" height="120" fill="url(#scan)"/>
  </g>
  <rect x="0.5" y="0.5" width="1199" height="339" rx="18" fill="none" stroke="#7FDBCA" stroke-opacity="0.18"/>

  <!-- terminal prompt -->
  <g font-family="{MONO}" font-size="19">
    <g clip-path="url(#type)">
      <text x="72" y="84" fill="#5EEAD4">~/javid</text>
      <text x="158" y="84" fill="#8B9DA5">$</text>
      <text x="178" y="84" fill="#E6EDF3">./ship --secure --all</text>
    </g>
    <rect class="cursor" x="72" y="68" width="10" height="21" fill="#5EEAD4"/>
  </g>

  <g font-family="{SANS}">
    <text class="fade f1" x="70" y="170" font-size="66" font-weight="700" fill="url(#name)" letter-spacing="-1">Javid Mamedov</text>
    <text class="fade f2" x="72" y="214" font-size="25" font-weight="600" fill="#5EEAD4" letter-spacing="0.5">DevSecOps Engineer</text>
    <text class="fade f3" x="72" y="252" font-size="18" fill="#A9BCC4">Kubernetes  ·  GitOps  ·  Secure CI/CD  ·  Supply-chain security</text>
  </g>
  <g class="fade f4" font-family="{MONO}" font-size="14">
    <rect x="72" y="276" width="186" height="30" rx="15" fill="#2DD4BF" fill-opacity="0.12" stroke="#2DD4BF" stroke-opacity="0.45"/>
    <circle cx="92" cy="291" r="5" fill="#3FB950"/>
    <text x="104" y="296" fill="#C9F5EE">all checks passed</text>
    <rect x="270" y="276" width="196" height="30" rx="15" fill="#FFFFFF" fill-opacity="0.04" stroke="#7FDBCA" stroke-opacity="0.25"/>
    <text x="290" y="296" fill="#A9BCC4">open to remote roles</text>
  </g>

  <!-- shield -->
  <circle class="ring" cx="985" cy="168" r="92" fill="none" stroke="#2DD4BF" stroke-width="2"/>
  <circle class="ring ring2" cx="985" cy="168" r="92" fill="none" stroke="#2DD4BF" stroke-width="2"/>
  <g transform="translate(985 168)">
    <circle r="92" fill="#0B1A20" fill-opacity="0.55" stroke="#2DD4BF" stroke-opacity="0.35"/>
    <path d="M0 -62 L50 -42 V2 C50 34 28 55 0 66 C-28 55 -50 34 -50 2 V-42 Z" fill="#2DD4BF" fill-opacity="0.10" stroke="#5EEAD4" stroke-width="3" stroke-linejoin="round"/>
    <path d="M-22 2 L-6 18 L24 -14" fill="none" stroke="#5EEAD4" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
  <g font-family="{MONO}" font-size="12" fill="#6F8790">
    <text x="868" y="300">sbom ✓   signed ✓   deployed ✓</text>
  </g>
</svg>
"""
(out / "header.svg").write_text(header)

# ------------------------------------------------------------------ pipeline
stages = [("commit", "git push"), ("test", "pytest · ruff"), ("scan", "trivy · gitleaks · semgrep"),
          ("sign", "sbom · cosign"), ("deploy", "argo cd · gitops"), ("observe", "prometheus · grafana")]
W, H, CYCLE = 1200, 210, 7.0
x0, x1, cy = 110, 1090, 92
xs = [x0 + i * (x1 - x0) / (len(stages) - 1) for i in range(len(stages))]
travel = 0.80                                    # fraction of the cycle the dot spends travelling
css, nodes = [], []
for i, ((name, tools), x) in enumerate(zip(stages, xs)):
    on = round(travel * (x - x0) / (x1 - x0) * 100, 2)
    css.append(f"@keyframes n{i} {{ 0%, {max(on - 0.01, 0)}% {{ fill: #10252C; stroke: #2E5361; }} "
               f"{on}%, 94% {{ fill: #134E4A; stroke: #5EEAD4; }} 100% {{ fill: #10252C; stroke: #2E5361; }} }}")
    css.append(f"@keyframes c{i} {{ 0%, {max(on - 0.01, 0)}% {{ opacity: 0; }} {on}%, 94% {{ opacity: 1; }} 100% {{ opacity: 0; }} }}")
    css.append(f".n{i} {{ animation: n{i} {CYCLE}s linear infinite; }} .c{i} {{ animation: c{i} {CYCLE}s linear infinite; }}")
    nodes.append(f"""
  <circle class="node n{i}" cx="{x:.1f}" cy="{cy}" r="26" stroke-width="2.5"/>
  <path class="check c{i}" d="M{x - 10:.1f} {cy} l7 7 l13 -14" fill="none" stroke="#5EEAD4" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="{x:.1f}" y="{cy + 58}" text-anchor="middle" font-family="{SANS}" font-size="18" font-weight="600" fill="#E6EDF3">{name}</text>
  <text x="{x:.1f}" y="{cy + 82}" text-anchor="middle" font-family="{MONO}" font-size="12.5" fill="#7C949D">{tools}</text>""")

pipeline = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="pt pd">
  <title id="pt">How I ship software</title>
  <desc id="pd">commit, test, scan, sign, deploy, observe</desc>
  <defs>{BG}
    <linearGradient id="line" gradientUnits="userSpaceOnUse" x1="{x0}" y1="0" x2="{x1}" y2="0">
      <stop offset="0" stop-color="#2DD4BF" stop-opacity="0.35"/>
      <stop offset="0.5" stop-color="#2DD4BF" stop-opacity="0.7"/>
      <stop offset="1" stop-color="#2DD4BF" stop-opacity="0.35"/>
    </linearGradient>
    <radialGradient id="dot"><stop offset="0" stop-color="#E6FFFB"/><stop offset="0.4" stop-color="#5EEAD4"/><stop offset="1" stop-color="#2DD4BF" stop-opacity="0"/></radialGradient>
    <clipPath id="card"><rect width="{W}" height="{H}" rx="18"/></clipPath>
  </defs>
  <style>
    .node {{ fill: #10252C; stroke: #2E5361; }}
    .check {{ opacity: 0; }}
    .runner {{ animation: run {CYCLE}s linear infinite; }}
    @keyframes run {{ 0% {{ transform: translateX(0); opacity: 1; }} {travel * 100:.0f}% {{ transform: translateX({x1 - x0}px); opacity: 1; }}
                     94% {{ transform: translateX({x1 - x0}px); opacity: 0; }} 100% {{ transform: translateX(0); opacity: 0; }} }}
    {chr(10).join('    ' + c for c in css)}
    @media (prefers-reduced-motion: reduce) {{
      .node, .check, .runner {{ animation: none !important; }}
      .node {{ fill: #134E4A; stroke: #5EEAD4; }} .check {{ opacity: 1; }} .runner {{ opacity: 0; }}
    }}
  </style>
  <g clip-path="url(#card)">
    <rect width="{W}" height="{H}" fill="url(#bg)"/>
    <rect width="{W}" height="{H}" fill="url(#grid)"/>
  </g>
  <rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="18" fill="none" stroke="#7FDBCA" stroke-opacity="0.18"/>
  <text x="32" y="36" font-family="{MONO}" font-size="13" fill="#5EEAD4">$ git push origin main</text>
  <text x="{W - 32}" y="36" text-anchor="end" font-family="{MONO}" font-size="13" fill="#6F8790">every commit · every time</text>
  <line x1="{x0}" y1="{cy}" x2="{x1}" y2="{cy}" stroke="url(#line)" stroke-width="3" stroke-dasharray="6 7" stroke-linecap="round"/>
  <g class="runner"><circle cx="{x0}" cy="{cy}" r="20" fill="#2DD4BF" fill-opacity="0.18"/><circle cx="{x0}" cy="{cy}" r="8" fill="#E6FFFB" stroke="#5EEAD4" stroke-width="3"/></g>{''.join(nodes)}
</svg>
"""
(out / "pipeline.svg").write_text(pipeline)

# ------------------------------------------------------------------ footer
footer = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="90" viewBox="0 0 1200 90" role="img" aria-label="Built, scanned, signed, shipped">
  <defs>{BG}<clipPath id="card"><rect width="1200" height="90" rx="18"/></clipPath></defs>
  <style>.cursor {{ animation: blink 1s step-end infinite; }} @keyframes blink {{ 50% {{ opacity: 0; }} }}
  @media (prefers-reduced-motion: reduce) {{ .cursor {{ animation: none; }} }}</style>
  <g clip-path="url(#card)"><rect width="1200" height="90" fill="url(#bg)"/><rect width="1200" height="90" fill="url(#grid)"/></g>
  <rect x="0.5" y="0.5" width="1199" height="89" rx="18" fill="none" stroke="#7FDBCA" stroke-opacity="0.18"/>
  <text x="600" y="52" text-anchor="middle" font-family="{MONO}" font-size="17" fill="#A9BCC4"><tspan fill="#5EEAD4">built</tspan> · <tspan fill="#5EEAD4">scanned</tspan> · <tspan fill="#5EEAD4">signed</tspan> · <tspan fill="#5EEAD4">shipped</tspan>   <tspan fill="#6F8790">exit 0</tspan></text>
  <rect class="cursor" x="828" y="37" width="9" height="19" fill="#5EEAD4"/>
</svg>
"""
(out / "footer.svg").write_text(footer)
print("ok", [p.name for p in out.iterdir()])
