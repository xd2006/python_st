import pytest

from model.group import Group

testdata = [
    Group(name="testname", header="testheader", footer="testfooter"),
    Group(name="", header="", footer="")
]


@pytest.mark.parametrize("group", testdata)
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    group = Group(name="testname", header="testheader", footer="testfooter")
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.group_count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
