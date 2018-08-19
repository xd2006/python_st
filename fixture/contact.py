from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def add(self, contact):
        wd = self.app.wd
        self.navigate_to_homepage()
        # Init creation process
        wd.find_element_by_link_text("add new").click()
        self.populate_contact_data(contact)
        #Submit creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[@name='submit']").click()
        # Return to home page
        self.navigate_to_homepage()
        self.contact_cache = None


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


    def edit_contact_by_index(self, contact, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        self.populate_contact_data(contact)
        # Submit creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[@value='Update']").click()
        # Return to home page
        self.navigate_to_homepage()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.navigate_to_homepage()
        wd.find_elements_by_xpath("//a[./img[@title='Edit']]")[index].click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.navigate_to_homepage()
        wd.find_elements_by_xpath("//a[./img[@title='Details']]")[index].click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.navigate_to_homepage()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_css_selector("input[value='Delete']").click()
        # submit deletion
        wd.switch_to_alert().accept()
        self.navigate_to_homepage()
        self.contact_cache = None

    def navigate_to_homepage(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()

    def contact_count(self):
        wd = self.app.wd
        self.navigate_to_homepage()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name='entry']"):
                cells = element.find_elements_by_css_selector("td")
                id = cells[0].find_element_by_name("selected[]").get_attribute("id")
                first_name = cells[2].text
                last_name = cells[1].text
                all_phones = cells[5].text.splitlines()
                homephone = all_phones[0] if len(all_phones)>=1 else None
                mobilephone = all_phones[1] if len(all_phones)>=2 else None
                workphone = all_phones[2] if len(all_phones)>=3 else None
                self.contact_cache.append(Contact(first_name=first_name, last_name=last_name, id=id, homephone=homephone, mobilephone=mobilephone,
                                                  workphone=workphone))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index) -> Contact:
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(first_name=firstname, last_name=lastname, id=id, homephone=homephone, mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone   )

