from selenium.webdriver.support.select import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def add(self, contact):
        wd = self.app.wd
        # Init creation process
        wd.find_element_by_link_text("add new").click()
        self.populate_contact_data(contact)
        #Submit creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[@name='submit']").click()
        # Return to home page
        self.return_to_homepage()

    def populate_contact_data(self, contact):
        wd = self.app.wd
        self.populate_by_name("firstname", contact.first_name)
        self.populate_by_name("middlename", contact.middle_name)
        self.populate_by_name("lastname", contact.last_name)
        self.populate_by_name("nickname", contact.nickname)
        self.populate_by_name("title", contact.title)
        self.populate_by_name("company", contact.company)
        self.populate_by_name("address", contact.address)
        self.populate_by_name("home", contact.phone)
        self.populate_by_name("email", contact.email)
        self.populate_by_name("homepage", contact.homepage)

        self.select_by_xpath("//div[@id='content']/form/select[@name='bday']", contact.day_of_birth)
        self.select_by_xpath("//div[@id='content']/form/select[@name='bmonth']", contact.month_of_birth)

        self.populate_by_name("byear", contact.year_of_birth)


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

    def edit_first_contact(self, contact):
        wd = self.app.wd
        # Init edit process contact
        wd.find_element_by_xpath("//a[./img[@title='Edit']]").click()
        self.populate_contact_data(contact)
        # Submit creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[@value='Update']").click()
        # Return to home page
        self.return_to_homepage()


    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_css_selector("input[value='Delete']").click()
        # submit deletion
        wd.switch_to_alert().accept()
        self.return_to_homepage()

    def return_to_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()