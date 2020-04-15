from model.group import Group

def test_update_group(app):
    app.session.login(username="admin", password="secret")
    app.group.update_first_group(Group(name="Test10", header="Test11", footer="Test12"))
    app.session.logout()