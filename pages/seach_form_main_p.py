from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as conditions
from selenium.webdriver.support.ui import WebDriverWait


class CarSearchForm:
    URL = "https://icarro-v1.netlify.app/search?page=0&size=10"
    CITY_INPUT = (By.CSS_SELECTOR, "input[data-testid='city-input']")
    CITY_OPTION = (By.CSS_SELECTOR, "[data-testid='city-option']")
    DATE_INPUT = (By.ID, "dates")
    CALENDAR_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Open calendar']")
    CALENDAR_DIALOG = (By.ID, "daterange-popover")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "form button[type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        self.wait.until(conditions.visibility_of_element_located(self.CITY_INPUT))

    @property
    def wait(self):
        return WebDriverWait(self.driver, 10)

    def fill_city(self, city):
        city_input = self.wait.until(conditions.element_to_be_clickable(self.CITY_INPUT))
        city_input.clear()
        city_input.send_keys(city)
        self.wait.until(conditions.element_to_be_clickable(self.CITY_OPTION)).click()

    def open_date_picker(self):
        self.wait.until(conditions.element_to_be_clickable(self.CALENDAR_BUTTON)).click()
        return self.wait.until(conditions.visibility_of_element_located(self.CALENDAR_DIALOG))

    def selected_city(self):
        return self.driver.find_element(*self.CITY_INPUT).get_attribute("value")

    def is_submit_enabled(self):
        return self.driver.find_element(*self.SUBMIT_BUTTON).is_enabled()

    def submit(self):
        self.wait.until(conditions.element_to_be_clickable(self.SUBMIT_BUTTON)).click()
