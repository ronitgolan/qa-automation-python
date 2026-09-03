# test_login.py
# Automated tests for the SauceDemo login flow (https://www.saucedemo.com)
# Python version of the original JavaScript/Playwright project — same logic, new language.

import pytest
from playwright.sync_api import Page, expect

URL = "https://www.saucedemo.com"


@pytest.fixture
def go_to_login(page: Page):
    page.goto(URL)
    return page


def test_successful_login_with_valid_credentials(go_to_login: Page):
    page = go_to_login
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    expect(page).to_have_url(f"{URL}/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")


def test_login_fails_with_incorrect_password(go_to_login: Page):
    page = go_to_login
    page.fill("#user-name", "standard_user")
    page.fill("#password", "wrong_password")
    page.click("#login-button")

    expect(page).to_have_url(f"{URL}/")
    expect(page.locator('[data-test="error"]')).to_contain_text(
        "Username and password do not match"
    )


def test_login_fails_with_empty_username(go_to_login: Page):
    page = go_to_login
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    expect(page.locator('[data-test="error"]')).to_contain_text(
        "Username is required"
    )


def test_login_fails_with_empty_password(go_to_login: Page):
    page = go_to_login
    page.fill("#user-name", "standard_user")
    page.click("#login-button")

    expect(page.locator('[data-test="error"]')).to_contain_text(
        "Password is required"
    )


def test_locked_out_user_cannot_login(go_to_login: Page):
    page = go_to_login
    page.fill("#user-name", "locked_out_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    expect(page.locator('[data-test="error"]')).to_contain_text(
        "Sorry, this user has been locked out"
    )
