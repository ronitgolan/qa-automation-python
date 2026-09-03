# QA Automation Project (Python / pytest + Playwright)

Python version of my [JavaScript Playwright automation project](https://github.com/ronitgolan/qa-automation-project) — same test coverage, written using **pytest** and **Playwright for Python**, built to demonstrate automation skills in Python specifically.

## What's covered

**Login (`test_login.py`)** — 5 scenarios:
- Successful login with valid credentials
- Login failure with an incorrect password
- Login failure with an empty username
- Login failure with an empty password
- Locked-out user cannot log in

**Cart & Checkout (`test_cart_checkout.py`)** — 5 scenarios:
- Add a single item to the cart
- Add multiple items and verify them in the cart
- Remove an item from the cart
- Complete a full checkout flow end-to-end
- Checkout fails when required customer info is missing

All 10 scenarios target the [SauceDemo](https://www.saucedemo.com) demo e-commerce site, and run across Chromium, Firefox, and WebKit — 30 total test runs.

## Tech stack

- [pytest](https://docs.pytest.org/)
- [Playwright for Python](https://playwright.dev/python/)

## Running locally

```bash
python -m pip install pytest playwright pytest-playwright
python -m playwright install
python -m pytest --browser chromium
```

To watch the tests run in a real browser:

```bash
python -m pytest --browser chromium --headed
```

To generate an HTML report:

```bash
python -m pip install pytest-html
python -m pytest --browser chromium --html=report.html --self-contained-html
```
