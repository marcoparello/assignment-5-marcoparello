# CYSE 411 Assignment — Engineering a DevSecOps Assurance Pipeline

## Scenario

You have inherited an existing software repository that may contain insecure code, vulnerable dependencies, and software supply chain risk.

Your task is **not** to manually fix vulnerabilities.

Your task is to engineer **automated security controls** using CI/CD.

You will design GitHub Actions workflows that implement:

1. Static Application Security Testing (SAST)
2. Software Composition Analysis (SCA)
3. Software Bill of Materials (SBOM) generation
4. Security quality gates that can block unsafe code from being merged

This assignment focuses on secure software engineering through automation, assurance, and policy enforcement.

---

# Learning Objectives

After completing this assignment, you should be able to:

* Engineer security controls in CI pipelines
* Configure modern DevSecOps tooling
* Apply supply chain security practices
* Use policy-as-code to enforce software assurance requirements
* Implement security checks as merge-enforced controls

---

# Assignment Requirements

You must implement **three GitHub Actions workflows** and integrate additional security controls.

Repository structure must include:

```text
.github/workflows/
   sast.yml
   sca.yml
   sbom.yml
```
[!IMPORTANT]
**Project Root Note:** The target application is located in the /vulnerable-app directory. You must configure your workflow actions to point to this subdirectory (e.g., using defaults: run: working-directory or tool-specific path arguments) to ensure the scanners find the source code and package.json.

## Engineering Decision Requirement

This assignment is not only about configuring tools.

For each task, you must make at least one justified engineering decision, such as:

- vulnerability severity threshold
- supply-chain policy choice
- SBOM analysis policy
- merge gate enforcement rule

Briefly document these decisions in your Pull Request description.

---

# Task 1 — SAST Pipeline

Create:

`.github/workflows/sast.yml`

Use one approved SAST tool:

* CodeQL
* SonarQube (optional alternative)

Requirements:

Your pipeline must:

* Trigger on **pull requests**
* Run automated static analysis
* Upload scan results (SARIF)
* Enforce a Quality Gate: By default, some SAST tools upload results without failing the workflow. You must configure a mechanism (such as a **SARIF threshold script (sarif-threshold)** or tool-specific exit-code flags) to ensure the workflow **fails if High or Critical vulnerabilities are detected**.

* Implement one customized security enhancement:

  * Secret Scanning Integration: (Hint: Check src/routes/admin.js for hardcoded credentials that should be caught).
  * Custom CodeQL query.
  * Modified rule configuration.

A Pull Request template is provided to help document these decisions.

**GitHub Actions Reference:** https://docs.github.com/en/actions

## Why Pull Requests?  
This assignment uses pull requests because modern DevSecOps pipelines enforce security controls before code is merged. Pull requests trigger automated security checks, support required reviews, and model how security gates are applied in real software engineering practice.

**Reference**: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request

## What is SARIF and why does it matter?  
SARIF (Static Analysis Results Interchange Format) is a standardized machine-readable format for representing static analysis findings. It allows tools such as CodeQL to export vulnerabilities, warnings, and metadata in a common structure that can be consumed by platforms like GitHub Security.

In this assignment, SARIF is important because it:
- enables automated reporting of findings in GitHub Code Scanning
- supports traceability and evidence of security analysis
- allows security results to be integrated into CI/CD decision gates
- reflects how modern DevSecOps pipelines operationalize automated security findings

**Reference:** https://docs.github.com/en/code-security/how-tos/find-and-fix-code-vulnerabilities/integrate-with-existing-tools/uploading-a-sarif-file-to-github

## What is a CodeQL query and why does it matter?  
A CodeQL query is a rule written in the CodeQL query language that analyzes source code as a database to detect security weaknesses, unsafe patterns, or coding errors. Unlike using only default scanners, custom queries allow engineers to tailor analysis to specific threats, coding practices, or organizational policies.

In this assignment, using or modifying a CodeQL query is important because it:
- demonstrates understanding beyond default tool configuration  
- shows how security analysis can be customized for specific risks  
- supports detection of domain-specific or project-specific vulnerabilities  
- reflects how advanced secure engineering teams extend automated analysis in practice

**References:**
- https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli

- GitHub CodeQL Action:
https://docs.github.com/en/code-security/code-scanning

- Custom CodeQL Queries:
https://codeql.github.com/docs/writing-codeql-queries/

- https://medium.com/@waeel.nono3719876/hunting-vulnerabilities-with-codeql-a-hands-on-introduction-17fd686dfb72

---

# Task 2 — SCA Pipeline

Create:

`.github/workflows/sca.yml`

Use one approved tool:

* Grype
* Trivy

Requirements:

Pipeline must:

* Scan dependencies
* Detect transitive dependency risk
* Enforce severity threshold
* Fail build when threshold is violated
* Implement one supply-chain control:

  * license risk policy, OR
  * dependency policy gate, OR
  * version/provenance check

**Reference about Supply Chain Security (GitHub):** https://docs.github.com/en/code-security/supply-chain-security

A Pull Request template is provided to help document these decisions.


## What is Grype and why does it matter? 
Grype is an open-source Software Composition Analysis (SCA) tool that scans software dependencies, containers, and SBOMs for known vulnerabilities (CVEs). It helps identify security risks introduced through third-party and transitive dependencies rather than flaws in code written by developers.

In this assignment, Grype is important because it:
- detects vulnerable open-source components in the software supply chain  
- helps identify transitive dependency risk that may not be visible to developers  
- supports automated dependency security checks in CI/CD pipelines  
- enables security gates that can block unsafe software from being merged

**References:**
- Grype: https://github.com/anchore/grype
- GitHub Actions with Trivy:https://github.com/aquasecurity/trivy-action

## What is Trivy and why does it matter?  
Trivy is an open-source security scanner used for Software Composition Analysis (SCA) and broader supply chain security. It can detect known vulnerabilities (CVEs) in software dependencies, container images, infrastructure-as-code configurations, and secrets.

In this assignment, Trivy is important because it:
- detects vulnerable dependencies and transitive supply-chain risks  
- supports automated security checks within CI/CD pipelines  
- can enforce security gates based on vulnerability severity  
- provides broader coverage beyond dependency scanning, including misconfigurations and secrets

**References:**
- Trivy: https://aquasecurity.github.io/trivy/


---

# Task 3 — SBOM Pipeline

Create:

`.github/workflows/sbom.yml`

Use one:

* Syft
* CycloneDX tooling

Requirements:

Must:

* Generate an SBOM
* Export artifact
* Upload artifact through GitHub Actions
* Include one policy or analysis step using the SBOM:

  * component inventory validation, OR
  * vulnerable component identification, OR
  * dependency review policy

**Reference of SBOM Basics:** https://www.cisa.gov/sbom

A Pull Request template is provided to help document these decisions.

## What is Syft and why does it matter?  
Syft is an open-source tool used to generate a Software Bill of Materials (SBOM), a machine-readable inventory of the software components, libraries, and dependencies used in an application. It helps make software composition visible and supports vulnerability management, incident response, and supply chain security.

In this assignment, Syft is important because it:
- creates visibility into direct and transitive software dependencies  
- supports generation of SBOM artifacts for software assurance  
- enables vulnerability analysis when used with tools such as Grype  
- helps operationalize supply-chain transparency in DevSecOps pipelines

**References: 
- Syft: https://github.com/anchore/syft

## What is CycloneDX and why does it matter?  
CycloneDX is an open standard for representing a Software Bill of Materials (SBOM). It provides a machine-readable format for describing software components, dependencies, and related metadata in support of vulnerability management and supply chain security.

In this assignment, CycloneDX is important because it:
- provides a standardized format for documenting software components  
- supports visibility into direct and transitive dependencies  
- enables interoperability with vulnerability analysis and supply-chain tools  
- helps operationalize software transparency and assurance in DevSecOps pipelines

**Reference CycloneDX:** https://cyclonedx.org/tool-center/

---

# Task 4 — Security Gate Enforcement

At least one workflow must act as a merge gate.

**Unsafe builds must fail**. To achieve this, you must ensure the shell returns a non-zero exit code when security violations are found. This is what allows GitHub to block a Pull Request.

Branch protection must treat the workflow as a required check.

  [!TIP]
  Branch Protection Setup: To fully operationalize the "Gate," you must manually configure Branch Protection in your repository settings to require these status checks to pass before merging into main.

Your security gate must enforce at least one:

* vulnerability threshold policy
* dependency policy
* secret detection policy

---

## What is Security Gate Enforcement and why does it matter?  
Security gate enforcement is the use of automated policy checks in a CI/CD pipeline to prevent unsafe code or vulnerable software from being merged until defined security conditions are satisfied. Rather than treating security findings as advisory only, security gates turn security requirements into enforceable controls.

In this assignment, security gate enforcement is important because it:
- blocks merges when security thresholds are violated  
- turns security analysis into actionable policy decisions  
- helps enforce risk-based controls automatically in CI/CD  
- reflects how modern DevSecOps pipelines operationalize “secure by default” practices

**References**

- GitHub Branch Protection Rules: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches

- Required Status Checks Tutorial: https://oneuptime.com/blog/post/2026-01-28-github-actions-branch-protection/view

- Concept: Gated Commits / Merge Gates: https://en.wikipedia.org/wiki/Gated_commit


# Deliverables

The students must submit a Pull-Request of the repository containing:

* The three functioning workflows
* Working security gates
* Generated artifacts
* Pull Request description documenting major security decisions

- Submission is the pull request itself.

- Direct pushes to main are not permitted.

---

# Constraints

* Do not copy prior course examples verbatim.
* You may consult official documentation.
* You must configure at least one tool not used in prior labs.
* Pipelines must run successfully in GitHub Actions.
* All configuration must be reproducible from your repository.

---

# Submission Process

1. Create a feature branch.
2. Implement required workflows.
3. Push your branch.
4. Open a pull request into main.
5. Ensure required checks pass.
6. Submit by leaving the pull request open for grading.

## 🛠️ Pre-Submission Validation

Before submitting your Pull Request, you can run a local "Pre-Flight Check" to ensure your file structure and YAML syntax are correct.

### Running the Check
From the root of your repository, run:
```bash
python3 tests/preflight_check.py
```
## Assessment Note
This assignment does not provide students access to hidden grading checks.

Evaluation will include instructor review of workflow correctness, security logic, and configuration quality.

---

# Grading (100 pts)

SAST pipeline correctness ............. 25

SCA pipeline correctness .............. 25

SBOM generation + policy use .......... 25

Security gate enforcement ............. 25

Total ................................ 100

# Assignment Rubric: DevSecOps Assurance Pipeline

This rubric defines the technical and engineering requirements to achieve full credit.  
Grading evaluates not only whether the pipelines function correctly, but also the quality of the security decisions you make when configuring controls, thresholds, and merge gates.

| Criteria | Points | Full Marks Requirements (To achieve 100%) |
| :--- | :---: | :--- |
| **1. SAST Pipeline Correctness** | **25** | • **Automation:** Workflow (`sast.yml`) triggers automatically on Pull Requests.<br>• **Path Accuracy:** Tool is correctly configured to analyze the `./vulnerable-app` directory.<br>• **Enhancement:** Includes a verified security enhancement such as a custom CodeQL query, modified rule configuration, or secret scanning integration.<br>• **Standardization:** Results are exported/uploaded in SARIF (or supported equivalent).<br>• **Engineering Decision:** A justified security threshold, rule customization, or policy decision is reflected in the workflow and documented in the Pull Request. |
| **2. SCA Pipeline Correctness** | **25** | • **Tooling:** Successful implementation of Grype or Trivy targeting the application sub-folder.<br>• **Risk Detection:** Pipeline identifies direct and transitive dependency vulnerabilities.<br>• **Supply Chain Control:** At least one verifiable policy check is implemented (license, dependency, provenance, etc.).<br>• **Enforcement:** Workflow fails when defined severity thresholds are violated.<br>• **Engineering Decision:** Severity threshold and supply-chain policy choices are justified and appropriate for the repository. |
| **3. SBOM Generation and Policy Use** | **25** | • **Artifact Generation:** Workflow (`sbom.yml`) generates a valid machine-readable SBOM (Syft or CycloneDX).<br>• **Persistence:** SBOM is uploaded as a GitHub Actions artifact.<br>• **Policy Step:** Includes at least one automated analysis or policy check performed using the SBOM.<br>• **Integration:** Demonstrates how SBOM output supports assurance or vulnerability visibility.<br>• **Engineering Decision:** The selected SBOM analysis or policy step is justified in the Pull Request. |
| **4. Security Gate Enforcement** | **25** | • **Logic Enforcement:** At least one workflow returns a non-zero exit code (`exit 1`) when defined security violations occur.<br>• **Merge Blocking:** Security gate operates as an actual merge-blocking control through required checks.<br>• **Policy Rigor:** Gate enforcement is based on a defined threshold (for example, fail on High/Critical).<br>• **Operational Correctness:** The gate acts as an enforceable control rather than advisory logging only.<br>• **Engineering Decision:** Gate threshold and enforcement strategy are justified and appropriate for repository risk. |
| **Total Score** | **100** | **Manual Review Required:** Scores reflect both technical correctness and soundness of engineering decisions. |

## Grading Notes for Students

* **Sub-folder Context Matters:**  
Scanners must target the `/vulnerable-app` directory. Workflows that scan only the repository root and miss the target application may receive zero credit for correctness.

* **A Scanner Is Not a Gate:**  
A tool that detects vulnerabilities but still allows the workflow to pass does not satisfy Task 4. You must engineer the pipeline to fail when policy conditions are violated.

* **Engineering Decisions Are Graded:**  
Choosing and justifying thresholds, supply-chain policies, and merge gate logic is part of the assignment, not an optional add-on.

* **Manual Review Applies:**  
The instructor may inspect workflow logic to detect bypasses, dummy results, or superficial implementations that satisfy syntax but do not implement meaningful controls.