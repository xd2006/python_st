from random import randrange

from model.group import Group


def test_edit_group(app):
    if app.group.group_count() == 0:
        app.group.create(Group(name="testname", header="testheader", footer="testfooter"))
    old_groups = app.group.get_group_list()
    group = Group(name="testname_edited", header="testheader_edited", footer="testfooter_edited")
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.edit_group_by_index(group, index)
    assert len(old_groups) == app.group.group_count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_group_name(app):
    if app.group.group_count() == 0:
        app.group.create(Group(name="testname", header="testheader", footer="testfooter"))
    old_groups = app.group.get_group_list()
    group = Group(name="testname_edited_only")
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.edit_group_by_index(group, index)
    assert len(old_groups) == app.group.group_count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
