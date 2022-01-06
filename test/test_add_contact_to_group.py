import random
from model.contact import Contact
from model.group import Group


def test_add_contact_to_group(db, app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Contact for add to group"))
    if app.group.count() == 0:
        app.group.create(Group(name="group for contact"))

    groups = db.get_group_list()
    random_group = random.choice(groups)
    random_contact = db.get_clear_contact()
    if random_contact is False:
        app.contact.create(Contact(firstname="Contact"))
        random_contact = db.get_clear_contact()

    if not db.check_relation(group=random_group, contact=random_contact):
        print(random_group.id)
        print(random_contact.id)
        app.contact.add_relation(group=random_group, contact=random_contact)
        check = db.check_relation(group=random_group, contact=random_contact)
        assert check is True
