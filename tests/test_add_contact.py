import pytest

from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_add_contact(app):
    app.session.logon(username="admin", password="secret")
    app.contact.add_contact(
        Contact(first_name="TestName", middle_name="testMiddle", last_name="LastTest", nickname="NickTest",
                title="Title", company="Company", address="Some Address",
                phone="+37529000000", email="somemail@mail.com", homepage="testhomepage.com",
                day_of_birth="10", month_of_birth="September", year_of_birth="1980"))
    app.session.logout()
