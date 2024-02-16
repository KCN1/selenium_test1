from .pages.sbis_page import SbisPage
# from .pages.sbis_contacts import SbisContactsPage

def test_can_open_sbis_contacts_page(browser):
    link = "https://sbis.ru/"
    page = SbisPage(browser, link)
    browser.implicitly_wait(5)
    page.open()
    page.go_to_sbis_contacts_page()
    assert 'sbis.ru/contacts' in browser.current_url
