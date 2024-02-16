from .pages.sbis_contacts_page import SbisContactsPage


def test_can_open_tensor_page(browser):
    link = "https://sbis.ru/contacts/"
    page = SbisContactsPage(browser, link)
    browser.implicitly_wait(5)
    page.open()
    page.should_be_tensor_banner()
    page.go_to_tensor_page()
    assert 'tensor.ru' in browser.current_url
