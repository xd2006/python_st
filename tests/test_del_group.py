from model.group import Group


def test_del_group(app):
    if app.group.group_count() == 0:
        app.group.create(Group(name="testname", header="testheader", footer="testfooter"))

    app.group.delete_first_group()
