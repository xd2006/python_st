
from model.group import Group


def test_edit_group(app):
    if app.group.group_count() == 0:
        app.group.create(Group(name="testname", header="testheader", footer="testfooter"))
    old_groups = app.group.get_group_list()
    group = Group(name="testname_edited", header="testheader_edited", footer="testfooter_edited")
    group.id = old_groups[0].id
    app.group.edit_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max)==sorted(new_groups, key=Group.id_or_max)




def test_edit_group_name(app):
    if app.group.group_count() == 0:
        app.group.create(Group(name="testname", header="testheader", footer="testfooter"))
    old_groups = app.group.get_group_list()
    group = Group(name="testname_edited_only")
    group.id = old_groups[0].id
    app.group.edit_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max)==sorted(new_groups, key=Group.id_or_max)

