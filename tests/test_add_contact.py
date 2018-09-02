
from fixture.application import Application
from model.contact import Contact

def test_add_contact(app: Application, db, json_contacts):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.add(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
