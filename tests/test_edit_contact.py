from model.contact import Contact


def test_edit_contact(app):
    app.session.logon(username="admin", password="secret")
    app.contact.edit_first_contact(
        Contact(first_name="TestName_ed", middle_name="testMiddle_ed", last_name="LastTest_ed", nickname="NickTest_ed",
                title="Title_ed", company="Company_ed", address="Some Address edited",
                phone="+37529000111", email="somemail-ed@mail.com", homepage="testhomepage_ed.com",
                day_of_birth="11", month_of_birth="October", year_of_birth="1985"))
    app.session.logout()