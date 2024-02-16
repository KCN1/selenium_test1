from .base_page import BasePage
from selenium.webdriver.common.by import By


class SbisPage(BasePage):
    def go_to_sbis_contacts_page(self):
        sbis_contacts_link = self.browser.find_element(By.CSS_SELECTOR, ".sbisru-Header a[href='/contacts']")
        sbis_contacts_link.click()

    # def should_be_contacts_link(self):
    #     assert self.is_element_present(By.CSS_SELECTOR, ".sbisru-Header a[href='/contacts']"), "Contacts link is not available"
