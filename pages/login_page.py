from selenium.webdriver.common.by import By


class LoginPage:
    URL = "https://icarro-v1.netlify.app/login"
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    Yalla_BTN = (By.XPATH, "//button[contains(text(),'Y’alla!')]")
    LOGIN_NAV_LINK = (By.CSS_SELECTOR, "a[href='/login']")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def open_login_form(self):
        self.driver.find_element(*self.LOGIN_NAV_LINK).click()

    def fill_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def fill_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def yalla_login(self):
        self.driver.find_element(*self.Yalla_BTN).click()



