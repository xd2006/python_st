import random
from random import randrange

from model.contact import Contact


def test_edit_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add(
            Contact(first_name="TestName", middle_name="testMiddle", last_name="LastTest", nickname="NickTest",
                    title="Title", company="Company", address="Some Address",
                    homephone="+37529000000", email="somemail@mail.com", homepage="testhomepage.com",
                    day_of_birth="10", month_of_birth="September", year_of_birth="1980"))
    old_contacts = db.get_contact_list()
    contact = Contact(first_name="TestName_ed", middle_name="testMiddle_ed", last_name="LastTest_ed", nickname="NickTest_ed",
                      title="Title_ed", company="Company_ed", address="Some Address edited",
                      homephone="+37529000111", email="somemail-ed@mail.com", homepage="testhomepage_ed.com",
                      day_of_birth="11", month_of_birth="October", year_of_birth="1985")
    contact_to_edit = random.choice(old_contacts)
    app.contact.edit_contact_by_id(contact, contact_to_edit.id)
    contact.id = contact_to_edit.id
    assert len(old_contacts) == app.contact.contact_count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact_to_edit)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)

