import random

from fixture.application import Application
from model.contact import Contact
from model.group import Group


def test_add_contact_to_group(app: Application, db, orm):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="testname", header="testheader", footer="testfooter"))

    groups = db.get_group_list()
    group = random.choice(groups)
    contacts = orm.get_contacts_not_in_group(group)
    if len(contacts) == 0:
        app.contact.add(
            Contact(first_name="TestName", middle_name="testMiddle", last_name="LastTest", nickname="NickTest",
                    title="Title", company="Company", address="Some Address",
                    homephone="+37529000000", email="somemail@mail.com", homepage="testhomepage.com",
                    day_of_birth="10", month_of_birth="September", year_of_birth="1980"))
        contacts = orm.get_contacts_not_in_group(group)
    contact = random.choice(contacts)
    app.contact.add_contact_to_group(contact, group)
    contacts_in_group = orm.get_contacts_in_group(group)
    assert contact in contacts_in_group, "Contact id=%s wasn't added to group id=%s" % (contact.id, group.id)


