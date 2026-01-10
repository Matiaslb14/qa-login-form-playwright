🌍 Language: [English](README.md) | [Español](README.es.md)

[![CI](https://github.com/Matiaslb14/qa-login-form-playwright/actions/workflows/ci.yml/badge.svg)](https://github.com/Matiaslb14/qa-login-form-playwright/actions)

# QA Login Automation – Playwright + Pytest

## 📌 Description
QA Automation project focused on validating the **authentication flow** of a web application using **Playwright** and **Pytest**.

The goal of this project is to automate a **critical business flow**, applying industry best practices such as **Page Object Model (POM)**, **reusable fixtures**, **negative scenarios**, **marker-based execution**, and **automatic evidence capture on failures**, ensuring stability in both **local execution** and **CI/CD pipelines**.

A public test application is used to simulate a real-world environment without external dependencies.

---

## ⭐ Key Features
- UI automation using **Playwright**
- Architecture based on **Page Object Model (POM)**
- Use of **fixtures** for setup and teardown
- Test suite separation:
  - **Smoke tests** (fast, critical checks)
  - **Regression tests** (negative scenarios and extended validations)
- **Headless** execution
- Automatic **screenshot capture on test failures**
- **Continuous Integration with GitHub Actions**
- Strong focus on **quality, maintainability, and stability**

---

## 🧪 What Is Tested
- Successful authentication (happy path)
- Negative scenarios:
  - Invalid username
  - Invalid password
  - Empty fields
- Behavior under anomalous inputs (security-aware checks)
- Controlled and consistent error messages

---

## 🔐 Security-Aware Checks (QA Perspective)
From a QA (non-pentesting) perspective, the following are validated:
- Safe handling of unexpected or oversized inputs
- No application crashes when receiving anomalous data
- Controlled error messages without sensitive information leakage
- Stable behavior of the authentication flow

---

## 🛠 Tech Stack
- **Python**
- **Pytest**
- **Playwright**
- **Chromium**
- **GitHub Actions**

---

## 📂 Project Structure
```text
qa-login-form-playwright/
├── pages/
│   └── login_page.py
├── tests/
│   ├── conftest.py
│   ├── test_login_positive.py
│   └── test_login_negative.py
├── utils/
│   └── config.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── pytest.ini
├── requirements.txt
└── README.md
```
## ▶️ How to Run the Project
### Local Execution
```bash
git clone https://github.com/Matiaslb14/qa-login-form-playwright.git
cd qa-login-form-playwright

python -m venv .venv
.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt
python -m playwright install chromium

pytest
```
### Run Tests by Type
```bash
# Smoke tests (fast, critical)
pytest -m smoke

# Regression tests
pytest -m regression
```
## 🤖 CI – GitHub Actions
- Tests run automatically on every **push** and **pull request**
- Executed in **headless mode**
- **Automatic screenshots** are generated on failures
- The pipeline acts as continuous integration validation

## 🧠 Technical Decisions
- **Playwright** is used for its speed, stability, and modern UI testing support
- **POM** is implemented to improve maintainability and scalability
- Marker-based execution optimizes test runtime
- Test design prioritizes **quality over quantity**
- No unnecessary frameworks are used to keep the focus on QA Automation

## 📌 Project Scope
**Included**
- UI automation
- Positive and negative scenarios
- Automatic execution evidence
- CI/CD integration

**Not Included**
- Custom backend
- Load testing
- Pentesting

## 📈 Next Steps
- Automatic HTML reports in CI
- Parallel test execution
- Extension of the flow to logout and session recovery