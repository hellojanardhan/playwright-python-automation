import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.products_page import ProductsPage


STANDARD_USER = "standard_user"
PASSWORD = "secret_sauce"


def test_login_with_valid_credentials(
    page: Page,
    saucedemo_base_url: str,
) -> None:
    login_page = LoginPage(page, saucedemo_base_url)
    login_page.open()
    login_page.login(STANDARD_USER, PASSWORD)

    expect(page).to_have_url(f"{saucedemo_base_url}/inventory.html")
    products_page = ProductsPage(page)
    expect(products_page.heading).to_be_visible()
    expect(products_page.product_title("Sauce Labs Backpack")).to_be_visible()


@pytest.mark.parametrize(
    ("username", "password", "expected_error"),
    [
        pytest.param(
            "invalid_user",
            PASSWORD,
            "Username and password do not match any user in this service",
            id="invalid-username",
        ),
        pytest.param(
            STANDARD_USER,
            "invalid_password",
            "Username and password do not match any user in this service",
            id="invalid-password",
        ),
        pytest.param("", "", "Username is required", id="empty-credentials"),
        pytest.param(
            STANDARD_USER,
            "",
            "Password is required",
            id="empty-password",
        ),
        pytest.param("", PASSWORD, "Username is required", id="empty-username"),
    ],
)
def test_login_rejects_invalid_credentials(
    page: Page,
    saucedemo_base_url: str,
    username: str,
    password: str,
    expected_error: str,
) -> None:
    login_page = LoginPage(page, saucedemo_base_url)
    login_page.open()
    login_page.login(username, password)

    expect(login_page.error_message).to_have_text(f"Epic sadface: {expected_error}")
    expect(page).to_have_url(f"{saucedemo_base_url}/")
