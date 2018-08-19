from fixture.application import Application
from model.contact import Contact


def test_phones_on_home_page(app: Application):
    contact_from_home_page: Contact = app.contact.get_contact_list()[0]
    contact_from_edit_page: Contact = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.homephone == contact_from_edit_page.homephone
    assert contact_from_home_page.workphone == contact_from_edit_page.workphone
    assert contact_from_home_page.mobilephone == contact_from_edit_page.mobilephone



