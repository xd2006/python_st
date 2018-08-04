from selenium.webdriver.support.select import Select


class GeneralHelper:

    def __init__(self, app):
        self.app = app

    def populate_by_name(self, name, text):
        if text is not None:
            wd = self.app.wd
            wd.find_element_by_name(name).click()
            wd.find_element_by_name(name).clear()
            wd.find_element_by_name(name).send_keys(text)

    def select_by_xpath(self, xpath, text):
        if text is not None:
            wd = self.app.wd
            selectBday = Select(wd.find_element_by_xpath(xpath))
            selectBday.select_by_value(text)