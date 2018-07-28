
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import Select


class Application:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False},
                             firefox_binary="C:/Program Files (x86)/Mozilla Firefox ESR/firefox.exe")
        self.wd.implicitly_wait(60)

    def open_home_page(self):
            wd = self.wd
            wd.get("http://localhost/addressbook/")

    def logon(self, username, password):
            wd = self.wd
            self.open_home_page()
            wd.find_element_by_name("user").click()
            wd.find_element_by_name("user").clear()
            wd.find_element_by_name("user").send_keys(username)
            wd.find_element_by_name("pass").click()
            wd.find_element_by_name("pass").clear()
            wd.find_element_by_name("pass").send_keys(password)
            wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def logout(self):
            wd = self.wd
            wd.find_element_by_link_text("Logout").click()

    def return_to_homepage(self):
            wd = self.wd
            wd.find_element_by_link_text("home").click()

    def add_contact(self, contact):
            wd = self.wd
            wd.find_element_by_link_text("add new").click()
            wd.find_element_by_name("firstname").click()
            wd.find_element_by_name("firstname").clear()
            wd.find_element_by_name("firstname").send_keys(contact.first_name)
            wd.find_element_by_name("middlename").click()
            wd.find_element_by_name("middlename").clear()
            wd.find_element_by_name("middlename").send_keys(contact.middle_name)
            wd.find_element_by_name("lastname").click()
            wd.find_element_by_name("lastname").clear()
            wd.find_element_by_name("lastname").send_keys(contact.last_name)
            wd.find_element_by_name("nickname").click()
            wd.find_element_by_name("nickname").clear()
            wd.find_element_by_name("nickname").send_keys(contact.nickname)
            wd.find_element_by_name("title").click()
            wd.find_element_by_name("title").clear()
            wd.find_element_by_name("title").send_keys(contact.title)
            wd.find_element_by_name("company").click()
            wd.find_element_by_name("company").clear()
            wd.find_element_by_name("company").send_keys(contact.company)
            wd.find_element_by_name("address").click()
            wd.find_element_by_name("address").clear()
            wd.find_element_by_name("address").send_keys(contact.address)
            wd.find_element_by_name("home").click()
            wd.find_element_by_name("home").clear()
            wd.find_element_by_name("home").send_keys(contact.phone)
            wd.find_element_by_name("email").click()
            wd.find_element_by_name("email").clear()
            wd.find_element_by_name("email").send_keys(contact.email)
            wd.find_element_by_name("homepage").click()
            wd.find_element_by_name("homepage").clear()
            wd.find_element_by_name("homepage").send_keys(contact.homepage)
            selectBday = Select(wd.find_element_by_xpath("//div[@id='content']/form/select[@name='bday']"))
            selectBday.select_by_value(contact.day_of_birth)
            selectBMonth = Select(wd.find_element_by_xpath("//div[@id='content']/form/select[@name='bmonth']"))
            selectBMonth.select_by_value(contact.month_of_birth)
            wd.find_element_by_name("byear").click()
            wd.find_element_by_name("byear").clear()
            wd.find_element_by_name("byear").send_keys(contact.year_of_birth)
            wd.find_element_by_xpath("//div[@id='content']/form/input[@name='submit']").click()

            self.return_to_homepage()

    def return_to_groups_page(self):
                wd = self.wd
                wd.find_element_by_link_text("group page").click()

    def create_group(self, group):
                wd = self.wd

                self.open_groups_page()
                # init group creation
                wd.find_element_by_name("new").click()
                # fill grops form
                wd.find_element_by_name("group_name").click()
                wd.find_element_by_name("group_name").clear()
                wd.find_element_by_name("group_name").send_keys(group.name)
                wd.find_element_by_name("group_header").click()
                wd.find_element_by_name("group_header").clear()
                wd.find_element_by_name("group_header").send_keys(group.header)
                wd.find_element_by_name("group_footer").click()
                wd.find_element_by_name("group_footer").clear()
                wd.find_element_by_name("group_footer").send_keys(group.footer)
                # submit group creation
                wd.find_element_by_name("submit").click()

                self.return_to_groups_page()

    def open_groups_page(self):
                wd = self.wd
                wd.find_element_by_link_text("groups").click()

    def destroy(self):
                self.wd.quit()