import pytest

from pages.login_page import LoginPage

VALID_EMAIL = "bim@gmail.com"
VALID_PASSWORD = "West1312!"


def test_login_success(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.fill_email(VALID_EMAIL)
    login_page.fill_password(VALID_PASSWORD)
    login_page.yalla_login()


@pytest.mark.parametrize(
    ("email", "password"),
    [
        ("", ""),
        ("", VALID_PASSWORD),
        (VALID_EMAIL, ""),
        ("not-an-email", VALID_PASSWORD),
        ("nonexistent-ilcarro-user@example.com", VALID_PASSWORD),
        (VALID_EMAIL, "wrong-password"),
    ],
    ids=[
        "empty_credentials",
        "empty_email",
        "empty_password",
        "invalid_email_format",
        "unknown_email",
        "wrong_password",
    ],
)
def test_login_rejects_invalid_credentials(driver, email, password):
    login_page = LoginPage(driver)
    login_page.open()

    login_page.fill_email(email)
    login_page.fill_password(password)
    login_page.yalla_login()
    login_page.wait_for_rejected_login()

    assert login_page.is_login_page_open(), "Invalid login must not authenticate a user"
    assert login_page.has_validation_error(), "The rejected login must show an error"
    login_page.dismiss_browser_alert()
