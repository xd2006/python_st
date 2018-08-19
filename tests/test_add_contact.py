from model.contact import Contact


def test_test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="TestName", middle_name="testMiddle", last_name="LastTest", nickname="NickTest",
                      title="Title", company="Company", address="Some Address",
                      homephone="+37529000000", email="somemail@mail.com", homepage="testhomepage.com",
                      day_of_birth="10", month_of_birth="September", year_of_birth="1980")
    app.contact.add(contact)
    assert len(old_contacts) + 1 == app.contact.contact_count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
