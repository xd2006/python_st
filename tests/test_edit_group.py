import random
from random import randrange

from model.group import Group


def test_edit_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="testname", header="testheader", footer="testfooter"))
    old_groups = db.get_group_list()
    group = Group(name="testname_edited", header="testheader_edited", footer="testfooter_edited")
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.edit_group_by_id(group, group.id)
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        new_groups = map(clean, new_groups)
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_edit_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="testname", header="testheader", footer="testfooter"))
    old_groups = db.get_group_list()
    group = Group(name="testname_edited_only")
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.edit_group_by_id(group, group.id)
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        new_groups = map(clean, new_groups)
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def clean(group):
    return Group(id=group.id, name=group.name.strip())