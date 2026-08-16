from pages.login_page import LoginPage

VALID_EMAIL = "bim@gmail.com"
VALID_PASSWORD = "West1312!"


def test_login_success(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL)
    login_page.fill_password(VALID_PASSWORD)
    login_page.yalla_login()
