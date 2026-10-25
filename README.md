# Accessibility Baseline & Repository Architecture Audit

## 1. Project Overview

This project documents an accessibility and architecture audit of the National Portal of India.

- **Website:** https://www.india.gov.in/
- **Audit Tool:** Google Chrome Lighthouse
- **Audit Areas:** Accessibility, Performance, Best Practices, and SEO

The project records accessibility findings, supporting screenshots, and a proposed repository architecture for future development.

## 2. Architecture Overview

This repository follows a monorepo-style structure. Frontend code, backend code, documentation, and tests are organized in separate directories.

```text
task-1/
├── client/
├── server/
├── docs/
│   ├── accessibility-audit.md
│   └── screenshots/
│       ├── lighthouse-overview/
│       └── individual-issues/
├── tests/
└── README.md
```

## 3. Folder Responsibilities

- **client/** — Contains frontend code, user interface components, and client-side assets.
- **server/** — Contains backend application logic and API-related code.
- **docs/** — Stores the accessibility audit report and supporting screenshots.
- **tests/** — Stores automated tests and test-related documentation.
- **README.md** — Explains the project, repository structure, and setup instructions.

## 4. Architecture Boundaries

The client is responsible for presenting information and collecting user interactions. The server is responsible for processing requests and handling application logic. The client and server communicate through defined API endpoints when implemented.

Documentation and tests remain separate from application source code to improve maintainability and organization.

## 5. Local Setup

### Prerequisites

- Git
- Visual Studio Code
- A web browser
- The relevant runtime and dependencies when application code is added

### Setup Steps

1. Clone the repository from GitHub.
2. Open the project folder in Visual Studio Code.
3. Review the documentation in `docs/`.
4. Install the dependencies required by the client and server once their technology stacks are configured.
5. Run the relevant tests after test commands have been added.

**Current status:** This repository is an initial architecture skeleton and audit documentation project. Client and server implementations, dependency installation commands, and test commands will be added when the technology stack is defined.

## 6. First Vertical Feature Slice

A proposed first feature is an accessibility findings viewer.

1. The client displays the list of audit findings.
2. The client requests findings from a backend API.
3. The server returns structured finding data, including the issue title, description, priority, and remediation.
4. The client renders the findings for the user.
5. Tests verify the API response and the displayed information.

This feature is a proposed implementation and has not yet been developed.

## 7. Audit Results

The initial Lighthouse scores recorded during the audit were:

| Category | Score |
|---|---:|
| Performance | 49 |
| Accessibility | 89 |
| Best Practices | 88 |
| SEO | 100 |

Detailed findings and screenshot evidence are available in `docs/accessibility-audit.md` and `docs/screenshots/`.

## 8. Project Status

- [x] Initial accessibility findings documented
- [x] Screenshot evidence collected
- [x] Initial repository architecture planned
- [ ] Repository structure verified
- [ ] Architecture documentation reviewed
- [ ] Client and server implementation
- [ ] Tests configured
