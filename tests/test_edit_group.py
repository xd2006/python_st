
from model.group import Group


def test_edit_group(app):
    if app.group.group_count() == 0:
        app.group.create(Group(name="testname", header="testheader", footer="testfooter"))
    app.group.edit_first_group(Group(name="testname_edited", header="testheader_edited", footer="testfooter_edited"))

def test_edit_group_name(app):
    if app.group.group_count() == 0:
        app.group.create(Group(name="testname", header="testheader", footer="testfooter"))
    app.group.edit_first_group(
            Group(name="testname_edited_only"))
