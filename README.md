<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F2027,50:203A43,100:2C5364&height=200&section=header&text=Javid%20Mamedov&fontSize=44&fontColor=ffffff&fontAlignY=36&desc=DevSecOps%20Engineer%20%C2%B7%20Kubernetes%20%C2%B7%20CI%2FCD%20Security&descAlignY=58&descSize=17&animation=fadeIn" width="100%" alt="Javid Mamedov, DevSecOps Engineer"/>

**I build delivery platforms where security is part of the pipeline, not a step after it.**

<a href="https://www.linkedin.com/in/javid-mamedov-20061104c/"><img src="https://img.shields.io/badge/LinkedIn-Javid%20Mamedov-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
<a href="mailto:javidmm.006@gmail.com"><img src="https://img.shields.io/badge/Email-javidmm.006%40gmail.com-2C5364?style=flat-square&logo=gmail&logoColor=white" alt="Email"/></a>
<img src="https://img.shields.io/badge/Open%20to-remote%20%26%20international%20roles-203A43?style=flat-square" alt="Open to remote and international roles"/>

</div>

<br/>

## About

DevSecOps engineer focused on Kubernetes, GitOps and secure CI/CD. I design pipelines that test, scan, sign and ship software automatically, and I run what I build: hardened containers, default-deny networking, monitoring and alerting included.

- **Platform:** Kubernetes (kubeadm, kind), Helm, Argo CD, Docker, Linux
- **Security:** SAST, SCA, secret and IaC scanning wired into CI as blocking gates; SBOMs and image signing
- **Operations:** Prometheus, Grafana, Alertmanager, PostgreSQL backups, runbooks
- **Currently:** going deeper into cloud infrastructure design on AWS and policy-as-code for Kubernetes

<br/>

## Featured projects

### [SecureShip](https://github.com/jav1d006/secureship)&nbsp;&nbsp;<sub>Self-hosted DevSecOps scanner · Python · Next.js · Kubernetes</sub>

<a href="https://github.com/jav1d006/secureship"><img src="https://raw.githubusercontent.com/jav1d006/secureship/main/docs/screenshots/home.png" width="100%" alt="SecureShip web interface"/></a>

Upload a project and get a 0–100 security score from eight scanners (Gitleaks, Trivy, Bandit, Semgrep, Checkov, ShellCheck), with SARIF, CSV, JSON and PDF export and a GitHub Action for pull requests. The platform is built to the same standard it checks for:

- **Isolation:** every scan runs in its own Kubernetes Job with no network, no credentials and a read-only source mount; hardened ZIP extraction blocks zip-slip, symlinks and zip bombs
- **Supply chain:** CI runs tests, secret scanning and a self-scan, blocks on HIGH/CRITICAL CVEs, then publishes a CycloneDX SBOM and a keyless cosign signature
- **Runtime:** non-root, read-only containers, all capabilities dropped, default-deny NetworkPolicies
- **Operations:** GitOps with Argo CD, Prometheus and Grafana, 8 alert rules unit-tested with `promtool`, Alertmanager e-mail, daily PostgreSQL backups

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)
![Argo CD](https://img.shields.io/badge/Argo%20CD-EF7B4D?style=flat-square&logo=argo&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white)

<br/>

### [PulseBoard](https://github.com/jav1d006/PulseBoard)&nbsp;&nbsp;<sub>Real-time microservices on Kubernetes · Helm · GitHub Actions</sub>

An anonymous, real-time team-health service (FastAPI, Redis, PostgreSQL, WebSockets), built as a vehicle for production-grade Kubernetes delivery:

- **Packaging:** a configurable Helm chart with HPA (2 → 6 replicas), PodDisruptionBudget, StatefulSet storage and NetworkPolicies
- **CI/CD:** every push spins up a disposable `kind` cluster inside GitHub Actions, installs the chart and runs smoke tests, so nothing to clean up and nothing to pay for

![Helm](https://img.shields.io/badge/Helm-0F1689?style=flat-square&logo=helm&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)

<br/>

### More work

| Project | What it is |
|---|---|
| [Linux-Hardening](https://github.com/jav1d006/Linux-Hardening) | Menu-driven Bash toolkit that applies Linux hardening baselines (kernel, disk, identity and authentication) with confirmation and logging |
| [Payloads-WAF](https://github.com/jav1d006/Payloads-WAF) | Curated JSON payload sets (SQLi, SSRF, SSTI, XXE, request smuggling and more) for authorised WAF and application security testing |
| [Gitlab-Local-Kubernetes](https://github.com/jav1d006/Gitlab-Local-Kubernetes) | Containerised app deployed to a local Kubernetes cluster through GitLab CI |
| [SAST-DAST-RealProject](https://github.com/jav1d006/SAST-DAST-RealProject) | Intentionally vulnerable app scanned with Snyk (SAST) and OWASP ZAP (DAST) in CI |

<br/>

## Toolbox

<table>
<tr>
<td width="160"><b>Cloud & platform</b></td>
<td>
<img src="https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white" alt="Kubernetes"/>
<img src="https://img.shields.io/badge/Helm-0F1689?style=flat-square&logo=helm&logoColor=white" alt="Helm"/>
<img src="https://img.shields.io/badge/Argo%20CD-EF7B4D?style=flat-square&logo=argo&logoColor=white" alt="Argo CD"/>
<img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker"/>
<img src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=white" alt="AWS"/>
<img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black" alt="Linux"/>
<img src="https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=nginx&logoColor=white" alt="Nginx"/>
</td>
</tr>
<tr>
<td><b>CI/CD & IaC</b></td>
<td>
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub Actions"/>
<img src="https://img.shields.io/badge/GitLab%20CI-FC6D26?style=flat-square&logo=gitlab&logoColor=white" alt="GitLab CI"/>
<img src="https://img.shields.io/badge/Jenkins-D24939?style=flat-square&logo=jenkins&logoColor=white" alt="Jenkins"/>
<img src="https://img.shields.io/badge/Terraform-844FBA?style=flat-square&logo=terraform&logoColor=white" alt="Terraform"/>
<img src="https://img.shields.io/badge/Ansible-EE0000?style=flat-square&logo=ansible&logoColor=white" alt="Ansible"/>
<img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white" alt="Git"/>
</td>
</tr>
<tr>
<td><b>Security</b></td>
<td>
<img src="https://img.shields.io/badge/Trivy-1904DA?style=flat-square&logo=aqua&logoColor=white" alt="Trivy"/>
<img src="https://img.shields.io/badge/Gitleaks-2C5364?style=flat-square" alt="Gitleaks"/>
<img src="https://img.shields.io/badge/Semgrep-1D3557?style=flat-square&logo=semgrep&logoColor=white" alt="Semgrep"/>
<img src="https://img.shields.io/badge/Checkov-6F42C1?style=flat-square" alt="Checkov"/>
<img src="https://img.shields.io/badge/Bandit-3776AB?style=flat-square" alt="Bandit"/>
<img src="https://img.shields.io/badge/OWASP%20ZAP-00549E?style=flat-square&logo=zap&logoColor=white" alt="OWASP ZAP"/>
<img src="https://img.shields.io/badge/Snyk-4C4A73?style=flat-square&logo=snyk&logoColor=white" alt="Snyk"/>
<img src="https://img.shields.io/badge/cosign-203A43?style=flat-square&logo=sigstore&logoColor=white" alt="cosign"/>
</td>
</tr>
<tr>
<td><b>Observability</b></td>
<td>
<img src="https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white" alt="Prometheus"/>
<img src="https://img.shields.io/badge/Grafana-F46800?style=flat-square&logo=grafana&logoColor=white" alt="Grafana"/>
<img src="https://img.shields.io/badge/Alertmanager-E6522C?style=flat-square&logo=prometheus&logoColor=white" alt="Alertmanager"/>
</td>
</tr>
<tr>
<td><b>Languages & data</b></td>
<td>
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/>
<img src="https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white" alt="Bash"/>
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" alt="JavaScript"/>
<img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI"/>
<img src="https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white" alt="Next.js"/>
<img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL"/>
<img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white" alt="Redis"/>
</td>
</tr>
</table>

<br/>

<div align="center">
<sub>Interested in working together? The fastest way to reach me is <a href="https://www.linkedin.com/in/javid-mamedov-20061104c/">LinkedIn</a> or <a href="mailto:javidmm.006@gmail.com">e-mail</a>.</sub>
</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2C5364,100:0F2027&height=90&section=footer" width="100%" alt=""/>
