
from model.group import Group


def test_edit_group(app):
    app.group.edit_first_group(Group(name="testname_edited", header="testheader_edited", footer="testfooter_edited"))

def test_edit_group_name(app):
    app.group.edit_first_group(
            Group(name="testname_edited_only"))
