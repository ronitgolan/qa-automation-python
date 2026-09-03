# test_cart_checkout.py
# Automated tests for the SauceDemo cart & checkout flow (https://www.saucedemo.com)
# Python version of the original JavaScript/Playwright project — same logic, new language.

import pytest
from playwright.sync_api import Page, expect

URL = "https://www.saucedemo.com"


@pytest.fixture
def logged_in_page(page: Page):
    page.goto(URL)
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    expect(page).to_have_url(f"{URL}/inventory.html")
    return page


def test_add_single_item_to_cart(logged_in_page: Page):
    page = logged_in_page
    page.click(".inventory_item:first-child .btn_inventory")
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")


def test_add_multiple_items_to_cart(logged_in_page: Page):
    page = logged_in_page
    page.click("#add-to-cart-sauce-labs-backpack")
    page.click("#add-to-cart-sauce-labs-bike-light")

    expect(page.locator(".shopping_cart_badge")).to_have_text("2")

    page.click(".shopping_cart_link")
    expect(page).to_have_url(f"{URL}/cart.html")

    names = page.locator(".inventory_item_name")
    expect(names).to_contain_text(["Sauce Labs Backpack", "Sauce Labs Bike Light"])


def test_remove_item_from_cart(logged_in_page: Page):
    page = logged_in_page
    page.click("#add-to-cart-sauce-labs-backpack")
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")

    page.click(".shopping_cart_link")
    page.click("#remove-sauce-labs-backpack")

    expect(page.locator(".shopping_cart_badge")).to_have_count(0)


def test_complete_checkout_with_valid_details(logged_in_page: Page):
    page = logged_in_page
    page.click("#add-to-cart-sauce-labs-backpack")
    page.click(".shopping_cart_link")
    page.click('[data-test="checkout"]')

    page.fill('[data-test="firstName"]', "Ronit")
    page.fill('[data-test="lastName"]', "Golan")
    page.fill('[data-test="postalCode"]', "12345")
    page.click('[data-test="continue"]')

    expect(page).to_have_url(f"{URL}/checkout-step-two.html")
    expect(page.locator(".summary_info")).to_be_visible()

    page.click('[data-test="finish"]')
    expect(page.locator(".complete-header")).to_have_text("Thank you for your order!")


def test_checkout_fails_with_missing_info(logged_in_page: Page):
    page = logged_in_page
    page.click("#add-to-cart-sauce-labs-backpack")
    page.click(".shopping_cart_link")
    page.click('[data-test="checkout"]')

    page.click('[data-test="continue"]')

    expect(page.locator('[data-test="error"]')).to_contain_text(
        "First Name is required"
    )
