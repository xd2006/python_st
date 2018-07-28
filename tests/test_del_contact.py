
def test_del_contact(app):
    app.session.logon(username="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()