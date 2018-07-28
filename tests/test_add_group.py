import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):

    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.logon(username="admin", password="secret")
    app.create_group(Group(name="testname", header="testheader", footer="testfooter"))
    app.logout()


def test_add_empty_group(app):
    app.logon(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
