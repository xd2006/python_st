from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import Select

from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": True},
                            firefox_binary="C:/Program Files (x86)/Mozilla Firefox/firefox.exe")
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def return_to_homepage(self):
        wd = self.wd
        wd.find_element_by_link_text("home").click()





    def destroy(self):
        self.wd.quit()
