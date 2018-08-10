
from model.group import Group


def test_edit_group(app):
    if app.group.group_count() == 0:
        app.group.create(Group(name="testname", header="testheader", footer="testfooter"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="testname_edited", header="testheader_edited", footer="testfooter_edited"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)



def test_edit_group_name(app):
    if app.group.group_count() == 0:
        app.group.create(Group(name="testname", header="testheader", footer="testfooter"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(
        Group(name="testname_edited_only"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


