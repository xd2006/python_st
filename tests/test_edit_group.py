
from model.group import Group


def test_edit_group(app):
    app.session.logon(username="admin", password="secret")
    app.group.edit_first_group(Group(name="testname_edited", header="testheader_edited", footer="testfooter_edited"))
    app.session.logout()

def test_edit_group_name(app):
    app.session.logon(username="admin", password="secret")
    app.group.edit_first_group(
            Group(name="testname_edited_only"))
    app.session.logout()