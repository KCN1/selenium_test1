from .pages.tensor_about_page import TensorAboutPage

def test_should_see_we_work(browser):
    link = "https://tensor.ru/about/"
    page = TensorAboutPage(browser, link)
    browser.implicitly_wait(5)
    page.open()
    page.should_be_we_work()

def test_photos_equal_size(browser):
    link = "https://tensor.ru/about/"
    page = TensorAboutPage(browser, link)
    browser.implicitly_wait(5)
    page.open()
    photos = page.tensor_about_we_work_photos()
    widths, heights = set(), set()
    for photo in photos:
        widths.add(int(photo.get_attribute("width")))
        heights.add(int(photo.get_attribute("height")))
    assert len(widths) == len(heights) == 1, "Sizes not equal or no photos found"

