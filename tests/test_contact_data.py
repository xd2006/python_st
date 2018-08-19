from random import randrange

from fixture.application import Application
from model.contact import Contact
import re


def test_contact_data_on_home_and_edit_page(app: Application):
    if app.contact.contact_count() == 0:
        app.contact.add(
            Contact(first_name="TestName", middle_name="testMiddle", last_name="LastTest", nickname="NickTest",
                    title="Title", company="Company", address="Some Address",
                    homephone="+37529000000", mobilephone="+375(29)000001", workphone="+375(29)100-002",
                    email="somemail@mail.com",
                    email2="somemail2@mail.com", email3="somemail3@mail.com", homepage="testhomepage.com",
                    day_of_birth="10", month_of_birth="September", year_of_birth="1980"))
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page: Contact = contacts[index]
    contact_from_edit_page: Contact = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.last_name == contact_from_edit_page.last_name
    assert contact_from_home_page.first_name == contact_from_edit_page.first_name
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(
        contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(
        contact_from_edit_page)


def test_phones_on_home_page(app: Application):
    contact_from_home_page: Contact = app.contact.get_contact_list()[2]
    contact_from_edit_page: Contact = app.contact.get_contact_info_from_edit_page(2)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(
        contact_from_edit_page)


def test_phones_on_contact_view_page(app: Application):
    contact_from_view_page: Contact = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page: Contact = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone


def clear(s):
    return re.sub("([^\w^+])", "", s)


def merge_phones_like_on_home_page(contact: Contact):
    return "\n".join(filter(lambda x: x != "" and x is not None,
                            (map(lambda x: clear(x), [contact.homephone, contact.mobilephone, contact.workphone]))))


def merge_emails_like_on_home_page(contact: Contact):
    return "\n".join(filter(lambda x: x != "" and x is not None,
                            [contact.email, contact.email2, contact.email3]))
