# Accessibility Baseline & Repository Architecture Audit

## 1. Project Overview

This project documents an accessibility baseline audit of the National Portal of India and provides a small dashboard to display the recorded findings.

- **Website audited:** https://www.india.gov.in/
- **Audit tool:** Google Chrome Lighthouse
- **Testing approach:** Lighthouse and keyboard-only navigation
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python and Flask
- **Testing:** Python `unittest`

## 2. Repository Architecture

```text
Task-1/
├── client/
│   ├── index.html
│   ├── style.css
│   └── app.js
├── server/
│   └── app.py
├── docs/
│   ├── accessibility-audit.md
│   └── screenshots/
├── tests/
│   └── test_app.py
├── .gitignore
├── requirements.txt
└── README.md
```

## 3. Folder Responsibilities

- **client/** — Displays audit findings using HTML, CSS and JavaScript.
- **server/** — Provides a Flask API that returns structured finding data.
- **docs/** — Contains the audit report and screenshot evidence.
- **tests/** — Contains automated tests for the API.
- **requirements.txt** — Lists Python dependencies.
- **.gitignore** — Excludes virtual environments and temporary files.

## 4. Architecture Boundaries

The frontend requests audit findings from the backend through an HTTP API. The Flask server returns JSON data, and the frontend renders each finding as a dashboard card.

The audit documentation and screenshots are maintained separately from the application source code.

## 5. Local Setup

### Prerequisites

- Python 3
- Git
- Visual Studio Code
- A web browser
- VS Code Live Server extension

### Install dependencies

```bash
python -m venv .venv
```

Activate the environment in Git Bash on Windows:

```bash
source .venv/Scripts/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

### Run the backend

From the repository root:

```bash
python server/app.py
```

The API runs locally at `http://127.0.0.1:5000`.

- `GET /` — Returns an API health message.
- `GET /api/findings` — Returns the five recorded audit findings as JSON.

### Run the frontend

Open `client/index.html` using VS Code Live Server while the backend is running.

### Run automated tests

From the repository root:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

The current test suite contains three tests covering the health route, findings endpoint and required finding fields.

## 6. First Vertical Feature Slice

The accessibility findings viewer is implemented:

1. The frontend requests findings from the backend.
2. The backend returns structured JSON data.
3. The frontend renders the findings as dashboard cards.
4. Automated tests verify the API responses and required fields.

## 7. Lighthouse Results

| Category | Score |
|---|---:|
| Performance | 49 |
| Accessibility | 89 |
| Best Practices | 88 |
| SEO | 100 |

These are the scores recorded during the initial audit.

## 8. Accessibility Findings

Five findings and their recommended remediations are documented in `docs/accessibility-audit.md`. Supporting screenshots are available under `docs/screenshots/`.

The findings cover ARIA list structure, colour contrast, HTML list structure, duplicate IDs and links with identical text leading to different destinations.

## 9. Project Status

- [x] Accessibility findings documented
- [x] Screenshot evidence collected
- [x] Repository architecture established
- [x] Frontend dashboard implemented
- [x] Flask API implemented
- [x] Automated tests implemented and passing (3/3)
- [x] Changes pushed to GitHub
