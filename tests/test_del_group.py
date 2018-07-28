
def test_del_group(app):
    app.session.logon(username="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()