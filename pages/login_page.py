from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as conditions
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    URL = "https://icarro-v1.netlify.app/login"
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    Yalla_BTN = (By.XPATH, "//button[contains(text(),'Y’alla!')]")
    LOGIN_NAV_LINK = (By.CSS_SELECTOR, "a[href='/login']")
    ERROR_MESSAGES = (
        By.CSS_SELECTOR,
        "[role='alert'], .alert, .error, .errors, .invalid-feedback, .text-danger, [data-testid*='error']",
    )

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        self.wait.until(conditions.visibility_of_element_located(self.EMAIL_INPUT))

    @property
    def wait(self):
        return WebDriverWait(self.driver, 10)

    def open_login_form(self):
        self.driver.find_element(*self.LOGIN_NAV_LINK).click()

    def fill_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def fill_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def yalla_login(self):
        self.wait.until(conditions.element_to_be_clickable(self.Yalla_BTN)).click()

    def is_login_page_open(self):
        return "/login" in self.driver.current_url

    def has_validation_error(self):
        return any(
            error.is_displayed()
            for error in self.driver.find_elements(*self.ERROR_MESSAGES)
        ) or any(
            field.get_attribute("aria-invalid") == "true"
            or field.get_property("validationMessage")
            for field in (
                self.driver.find_element(*self.EMAIL_INPUT),
                self.driver.find_element(*self.PASSWORD_INPUT),
            )
        ) or self.has_browser_alert()

    def has_browser_alert(self):
        try:
            return bool(self.driver.switch_to.alert.text)
        except NoAlertPresentException:
            return False

    def dismiss_browser_alert(self):
        try:
            self.driver.switch_to.alert.accept()
        except NoAlertPresentException:
            pass

    def wait_for_rejected_login(self):
        self.wait.until(lambda _: self.has_validation_error())



