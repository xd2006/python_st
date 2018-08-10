from random import randrange

from model.contact import Contact


def test_edit_contact(app):
    if app.contact.contact_count() == 0:
        app.contact.add(
            Contact(first_name="TestName", middle_name="testMiddle", last_name="LastTest", nickname="NickTest",
                    title="Title", company="Company", address="Some Address",
                    phone="+37529000000", email="somemail@mail.com", homepage="testhomepage.com",
                    day_of_birth="10", month_of_birth="September", year_of_birth="1980"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="TestName_ed", middle_name="testMiddle_ed", last_name="LastTest_ed", nickname="NickTest_ed",
                title="Title_ed", company="Company_ed", address="Some Address edited",
                phone="+37529000111", email="somemail-ed@mail.com", homepage="testhomepage_ed.com",
                day_of_birth="11", month_of_birth="October", year_of_birth="1985")
    index = randrange(len(old_contacts))
    app.contact.edit_contact_by_index(contact, index)
    contact.id = old_contacts[index].id
    assert len(old_contacts) == app.contact.contact_count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

