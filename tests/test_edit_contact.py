from model.contact import Contact


def test_edit_contact(app):
    if app.contact.contact_count() == 0:
        app.contact.add(
            Contact(first_name="TestName", middle_name="testMiddle", last_name="LastTest", nickname="NickTest",
                    title="Title", company="Company", address="Some Address",
                    phone="+37529000000", email="somemail@mail.com", homepage="testhomepage.com",
                    day_of_birth="10", month_of_birth="September", year_of_birth="1980"))
    app.contact.edit_first_contact(
        Contact(first_name="TestName_ed", middle_name="testMiddle_ed", last_name="LastTest_ed", nickname="NickTest_ed",
                title="Title_ed", company="Company_ed", address="Some Address edited",
                phone="+37529000111", email="somemail-ed@mail.com", homepage="testhomepage_ed.com",
                day_of_birth="11", month_of_birth="October", year_of_birth="1985"))
