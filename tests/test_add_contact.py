from model.contact import Contact

def test_test_add_contact(app):
    app.contact.add(
        Contact(first_name="TestName", middle_name="testMiddle", last_name="LastTest", nickname="NickTest",
                title="Title", company="Company", address="Some Address",
                phone="+37529000000", email="somemail@mail.com", homepage="testhomepage.com",
                day_of_birth="10", month_of_birth="September", year_of_birth="1980"))
