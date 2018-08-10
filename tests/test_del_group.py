from model.group import Group


def test_del_group(app):
    if app.group.group_count() == 0:
        app.group.create(Group(name="testname", header="testheader", footer="testfooter"))

    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
