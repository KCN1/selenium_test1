from .base_page import BasePage
from selenium.webdriver.common.by import By


class TensorPage(BasePage):
    def go_to_tensor_about_page(self):
        tensor_about_link = self.browser.find_element(By.CSS_SELECTOR, "a.tensor_ru-Index__link[href='/about']")
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", tensor_about_link)
        tensor_about_link.click()

    def should_be_power_in_people(self):
        assert self.is_element_present(By.CSS_SELECTOR, ".tensor_ru-Index__block4-content.tensor_ru-Index__card"), '"Power in people" is not available'
