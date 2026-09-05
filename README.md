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

All 10 UI scenarios target the [SauceDemo](https://www.saucedemo.com) demo e-commerce site.

**API Tests (`test_api.py`)** — 7 scenarios against a public REST API ([reqres.in](https://reqres.in)):
- GET a single user (200, correct data)
- GET a nonexistent user (404)
- GET a paginated user list
- POST to create a user (201, echoes submitted data)
- PUT to update a user (200, updated fields)
- DELETE a user (204)
- POST registration with missing required field (400, error message)

## CI

GitHub Actions runs two separate jobs on every push:
- **`api-tests`** — runs the API suite once (no browser needed)
- **`ui-tests`** — runs the UI suite across Chromium, Firefox, and WebKit

## Tech stack

- [pytest](https://docs.pytest.org/)
- [Playwright for Python](https://playwright.dev/python/) (UI tests)
- [requests](https://requests.readthedocs.io/) (API tests)

## Running locally

```bash
python -m pip install pytest playwright pytest-playwright requests
python -m playwright install
python -m pytest --browser chromium --ignore=test_api.py
python -m pytest test_api.py
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
