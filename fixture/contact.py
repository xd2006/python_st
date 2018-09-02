from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        from fixture.application import Application
        self.app: Application = app

    def add(self, contact):
        wd = self.app.wd
        self.navigate_to_homepage()
        # Init creation process
        wd.find_element_by_link_text("add new").click()
        self.populate_contact_data(contact)
        # Submit creation
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
        self.app.general.populate_by_name("home", contact.homephone)
        self.app.general.populate_by_name("mobile", contact.mobilephone)
        self.app.general.populate_by_name("work", contact.workphone)
        self.app.general.populate_by_name("email", contact.email)
        self.app.general.populate_by_name("email2", contact.email2)
        self.app.general.populate_by_name("email3", contact.email3)
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
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_name("add")) > 0):
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
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(first_name=first_name, last_name=last_name, id=id,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails,
                                                  address=address))
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
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        return Contact(first_name=firstname, last_name=lastname, id=id, homephone=homephone,
                       mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone, email=email,
                       email2=email2, email3=email3, address=address)

    def get_contact_from_view_page(self, index) -> Contact:
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        secondaryphone = re.search("F: (.*)", text).group(1)
        return Contact(homephone=homephone,
                       mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone)
