from selenium import webdriver

from fixture.contact import ContactHelper
from fixture.general import GeneralHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:
    wd: webdriver
    general: GeneralHelper
    group: GroupHelper
    contact: ContactHelper

    def __init__(self, browser, base_url):
        if (browser=="firefox"):
            self.wd = webdriver.Firefox(capabilities={"marionette": False},
                            firefox_binary="C:/Program Files (x86)/Mozilla Firefox ESR/firefox.exe")
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser &s" % browser)
        self.wd.implicitly_wait(2)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.general = GeneralHelper(self)
        self.base_url = base_url

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
