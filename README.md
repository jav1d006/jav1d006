<p align="center">
  <img src="assets/header.svg" width="100%" alt="Javid Mamedov, DevSecOps Engineer: Kubernetes, GitOps, secure CI/CD"/>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/javid-mamedov-20061104c/"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="mailto:javidmm.006@gmail.com"><img src="https://img.shields.io/badge/Email-Get%20in%20touch-2C5364?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>
  <a href="https://github.com/jav1d006?tab=repositories"><img src="https://img.shields.io/badge/Projects-Browse-203A43?style=for-the-badge&logo=github&logoColor=white" alt="Projects"/></a>
</p>

## `$ whoami`

I build delivery platforms where security is part of the pipeline, not a step after it. I design CI/CD that tests, scans, signs and ships software on every commit, and I run what I build: hardened containers, default-deny networking, monitoring and alerting included.

<p align="center">
  <img src="assets/terminal.svg" width="100%" alt="A day in production: healthy pods, zero HIGH/CRITICAL CVEs, signature verified, next role DevSecOps Engineer at your team"/>
</p>

<details>
<summary><code>$ kubectl get engineer javid -o yaml</code></summary>

```yaml
apiVersion: people/v1
kind: Engineer
metadata:
  name: javid-mamedov
  role: DevSecOps Engineer
spec:
  focus:         [kubernetes, gitops, secure-ci-cd, supply-chain-security]
  platform:      [kubernetes, helm, argo-cd, docker, linux]
  security:      [trivy, gitleaks, semgrep, checkov, sbom, cosign]
  observability: [prometheus, grafana, alertmanager]
  learning:      [aws, policy-as-code]
  openTo:        remote and international roles
```

</details>

## `$ cat pipeline.yml`

<p align="center">
  <img src="assets/pipeline.svg" width="100%" alt="How I ship: commit, test, scan, sign, deploy, observe"/>
</p>

Every change goes through the same gates. A failing test, a leaked secret or a HIGH/CRITICAL CVE stops the release; everything that ships is signed, has an SBOM and is deployed through GitOps.

## `$ kubectl get networkpolicy`

<p align="center">
  <img src="assets/defense.svg" width="100%" alt="Defense in depth: legitimate traffic flows through ingress to the API; direct database access and scan-job egress are denied"/>
</p>

Default-deny everywhere, explicit allows only. Containers run non-root on read-only filesystems with every capability dropped, and the jobs that touch untrusted code have no network and no credentials.

## `$ ls ~/projects --featured`

<table>
<tr>
<td width="50%" valign="top">

### [SecureShip](https://github.com/jav1d006/secureship)
**Self-hosted DevSecOps scanner**

Drop in a project, get a 0–100 security score from eight scanners, with SARIF, PDF and a GitHub Action for pull requests. Built to the standard it checks for.

- Every scan runs in an isolated Kubernetes Job: no network, no credentials, read-only source
- CI blocks HIGH/CRITICAL CVEs, publishes an SBOM and signs images with cosign
- GitOps with Argo CD, Prometheus alerts unit-tested with `promtool`

<img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI"/>
<img src="https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white" alt="Next.js"/>
<img src="https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white" alt="Kubernetes"/>
<img src="https://img.shields.io/badge/Argo%20CD-EF7B4D?style=flat-square&logo=argo&logoColor=white" alt="Argo CD"/>

<details>
<summary><b>Architecture</b></summary>

```mermaid
flowchart TB
    U([Browser / GitHub Action]) --> ING[ingress-nginx]
    ING --> FE[Next.js]
    ING --> API[FastAPI]
    API --> PG[(PostgreSQL)]
    API --> R[(Redis queue)]
    R --> W[Worker]
    W -->|one Job per scan| J[[Scan Job<br/>no network · read-only]]
    J --> S{{Gitleaks · Trivy · Semgrep<br/>Bandit · Checkov · ShellCheck}}
    GH[git push] --> CI[GitHub Actions<br/>tests · scans · SBOM · cosign] --> GHCR[(GHCR)]
    GH --> ARGO[Argo CD] -->|sync| ING
```

</details>

</td>
<td width="50%" valign="top">

### [PulseBoard](https://github.com/jav1d006/PulseBoard)
**Real-time microservices on Kubernetes**

An anonymous team-health service (FastAPI, Redis, PostgreSQL, WebSockets) built as a vehicle for production-grade Kubernetes delivery.

- Helm chart with HPA (2 → 6 replicas), PodDisruptionBudget, StatefulSet and NetworkPolicies
- Every push spins up a disposable `kind` cluster in GitHub Actions, deploys the chart and runs smoke tests
- Cloud-agnostic: runs on any cluster, no cloud bill

<img src="https://img.shields.io/badge/Helm-0F1689?style=flat-square&logo=helm&logoColor=white" alt="Helm"/>
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub Actions"/>
<img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white" alt="Redis"/>
<img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL"/>

<details>
<summary><b>Architecture</b></summary>

```mermaid
flowchart TB
    C([Team member]) -->|POST /pulse| ING[Ingress nginx]
    ING --> API[FastAPI API<br/>HPA 2 → 6]
    D([Live dashboard]) -.->|WebSocket| API
    API -->|ZADD + PUBLISH| R[(Redis<br/>rolling 30-min window)]
    WK[Worker] -->|every 60s aggregate| R
    WK -->|snapshots + burnout alerts| PG[(PostgreSQL<br/>StatefulSet)]
    GH[git push] --> CI[GitHub Actions] -->|ephemeral kind cluster| HELM[helm install + smoke test]
```

</details>

</td>
</tr>
</table>

### More work

| Project | What it is |
|---|---|
| [Linux-Hardening](https://github.com/jav1d006/Linux-Hardening) | Menu-driven Bash toolkit that applies Linux hardening baselines (kernel, disk, identity and authentication) with confirmation and logging |
| [Payloads-WAF](https://github.com/jav1d006/Payloads-WAF) | Curated JSON payload sets (SQLi, SSRF, SSTI, XXE, request smuggling and more) for authorised WAF and application security testing |
| [Gitlab-Local-Kubernetes](https://github.com/jav1d006/Gitlab-Local-Kubernetes) | Containerised app deployed to a local Kubernetes cluster through GitLab CI |
| [SAST-DAST-RealProject](https://github.com/jav1d006/SAST-DAST-RealProject) | Intentionally vulnerable app scanned with Snyk (SAST) and OWASP ZAP (DAST) in CI |

## `$ which --all tools`

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

<details>
<summary><code>$ cat .secrets</code></summary>

```console
$ gitleaks detect --source . --redact
Finding:  AWS_SECRET_ACCESS_KEY=REDACTED
RuleID:   aws-secret-access-key
File:     .secrets
✖ 1 leak found. Commit blocked. Nice try.
```

</details>

<br/>

<p align="center">
  <img src="assets/footer.svg" width="100%" alt="Built, scanned, signed, shipped"/>
</p>
