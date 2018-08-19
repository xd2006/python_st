from selenium.webdriver.firefox.webdriver import WebDriver

from fixture.contact import ContactHelper
from fixture.general import GeneralHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:
    wd: WebDriver
    general: GeneralHelper
    group: GroupHelper
    contact: ContactHelper

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False},
                            firefox_binary="C:/Program Files (x86)/Mozilla Firefox ESR/firefox.exe")
        self.wd.implicitly_wait(2)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.general = GeneralHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url()
            return True
        except:
            return False
