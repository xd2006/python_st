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
        self.app.general.populate_by_name("firstname", contact.first_name)
        self.app.general.populate_by_name("middlename", contact.middle_name)
        self.app.general.populate_by_name("lastname", contact.last_name)
        self.app.general.populate_by_name("nickname", contact.nickname)
        self.app.general.populate_by_name("title", contact.title)
        self.app.general.populate_by_name("company", contact.company)
        self.app.general.populate_by_name("address", contact.address)
        self.app.general.populate_by_name("home", contact.phone)
        self.app.general.populate_by_name("email", contact.email)
        self.app.general.populate_by_name("homepage", contact.homepage)

        self.app.general.select_by_xpath("//div[@id='content']/form/select[@name='bday']", contact.day_of_birth)
        self.app.general.select_by_xpath("//div[@id='content']/form/select[@name='bmonth']", contact.month_of_birth)

        self.app.general.populate_by_name("byear", contact.year_of_birth)




    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.return_to_homepage()
        # Init edit process contact
        wd.find_element_by_xpath("//a[./img[@title='Edit']]").click()
        self.populate_contact_data(contact)
        # Submit creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[@value='Update']").click()
        # Return to home page
        self.return_to_homepage()


    def delete_first_contact(self):
        wd = self.app.wd
        self.return_to_homepage()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_css_selector("input[value='Delete']").click()
        # submit deletion
        wd.switch_to_alert().accept()
        self.return_to_homepage()

    def return_to_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()