from random import randrange

from model.contact import Contact


def test_del_contact(app):
    if app.contact.contact_count() == 0:
        app.contact.add(
            Contact(first_name="TestName", middle_name="testMiddle", last_name="LastTest", nickname="NickTest",
                    title="Title", company="Company", address="Some Address",
                    homephone="+37529000000", email="somemail@mail.com", homepage="testhomepage.com",
                    day_of_birth="10", month_of_birth="September", year_of_birth="1980"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.contact_count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts

