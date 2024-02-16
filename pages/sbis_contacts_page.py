from .base_page import BasePage
from selenium.webdriver.common.by import By


class SbisContactsPage(BasePage):
    def go_to_tensor_page(self):
        tensor_banner = self.browser.find_element(By.CSS_SELECTOR, "#contacts_clients a.sbisru-Contacts__logo-tensor[title='tensor.ru']")
        tensor_banner.click()
        window_name = self.browser.window_handles[-1]
        self.browser.switch_to.window(window_name)

    def should_be_tensor_banner(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#contacts_clients .sbisru-Contacts__logo-tensor[title='tensor.ru']"), "Tensor banner is not available"
