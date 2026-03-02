import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from base.base_class import Base


class MainPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.number = application_number

    # URL
    url = 'https://info.midpass.ru/'

    # LOCATORS
    select_county = "//select[@id='countries']"
    select_city = "//select[@id='cities']"
    application_number = "//input[@id='applicationCode']"
    button = "//input[@id='search']"
    date = "//span[@class='data-block-day']"
    id = "//span[@class='data-block-id']"
    pass_status = "//span[@class='data-block-stat']"

    # GETTERS
    def wait_for_element(self, xpath, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath)))

    def wait_for_element_visible(self, xpath, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, xpath)))

    @staticmethod
    def select_dropdown_value(element, value):
        select = Select(element)
        select.select_by_value(str(value))

    def get_county(self):
        return self.wait_for_element(self.select_county)

    def get_city(self):
        return self.wait_for_element(self.select_city)

    def get_number(self):
        return self.wait_for_element(self.application_number)

    def get_button(self):
        return self.wait_for_element(self.button)

    def get_status(self):
        return self.wait_for_element(self.pass_status)

    def get_date(self):
        return self.wait_for_element(self.date)

    def get_id(self):
        return self.wait_for_element(self.id)

    # ACTIONS
    def open_page(self):
        self.driver.get(self.url)

    def select_country(self, value):
        element = self.get_county()
        self.select_dropdown_value(element, value)

    def select_city_value(self, value):
        element = self.get_city()
        self.select_dropdown_value(element, value)

    def input_number(self, application_number):
        self.get_number().send_keys(application_number)

    def button_click(self):
        self.get_button().click()

    def status_text(self):
        return self.get_status().text

    def date_text(self):
        return self.get_date().text

    def id_text(self):
        return self.get_id().text

    # MAIN METHODS
    def check_pass_status(self):
        self.open_page()
        self.select_country("29: ГЕРМАНИЯ")
        self.select_city_value("5: БОНН")
        self.input_number(2000493022026011300194396)
        self.button_click()
        time.sleep(3)
        return self.status_text(), self.date_text(), self.id_text()
