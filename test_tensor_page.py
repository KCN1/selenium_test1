from .pages.tensor_page import TensorPage


def test_can_open_tensor_about_page(browser):
    link = "https://tensor.ru/"
    page = TensorPage(browser, link)
    browser.implicitly_wait(5)
    page.open()
    page.should_be_power_in_people()
    page.go_to_tensor_about_page()
    assert 'tensor.ru/about' in browser.current_url
