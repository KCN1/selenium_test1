from .pages.sbis_contacts_page import SbisContactsPage

def test_should_see_tensor_banner(browser):
    link = "https://sbis.ru/contacts/"
    page = SbisContactsPage(browser, link)
    browser.implicitly_wait(5)
    page.open()
    page.should_be_tensor_banner()

def test_can_open_tensor_page(browser):
    link = "https://sbis.ru/contacts/"
    page = SbisContactsPage(browser, link)
    browser.implicitly_wait(5)
    page.open()
    page.go_to_tensor_page()
    assert 'tensor.ru' in browser.current_url
