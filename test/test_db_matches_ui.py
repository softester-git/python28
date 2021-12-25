from model.group import Group


def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    def clear(group):
        return(Group(id=group.id, name=group.name))
    db_list = map(clear, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
