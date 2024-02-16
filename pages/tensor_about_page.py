from .base_page import BasePage
from selenium.webdriver.common.by import By


class TensorAboutPage(BasePage):
    def tensor_about_we_work_photos(self):
        return self.browser.find_elements(By.CSS_SELECTOR, ".tensor_ru-About__block3 img.tensor_ru-About__block3-image")

    def should_be_we_work(self):
        assert self.is_element_present(By.CSS_SELECTOR, ".tensor_ru-About__block3"), '"We are working" is not available'
