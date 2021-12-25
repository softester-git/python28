from model.group import Group
from timeit import timeit


def test_group_list(app, db):
    print(timeit(lambda: app.group.get_group_list()))
    def clear(group):
        return(Group(id=group.id, name=group.name.strip()))
    print(timeit(lambda: map(clear, db.get_group_list()), number=1000))
