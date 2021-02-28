import time

class TestButtonOnDifferentLanguages:
    def test_button(self, browser):
        link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        button = browser.find_element_by_class_name('btn-add-to-basket')
        assert button, 'Кнопка отсутствует'
        time.sleep(30)