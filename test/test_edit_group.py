from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(name="new_group_name", header="new_group_header", footer="new_group_footer"))
    app.session.logout()


def test_edit_first_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(name="", header="", footer=""))
    app.session.logout()