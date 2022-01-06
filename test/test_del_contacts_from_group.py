import random
from model.contact import Contact
from model.group import Group


def test_del_contact_from_group(db, app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Contact for add to group"))
    if app.group.count() == 0:
        app.group.create(Group(name="group for contact"))

    contacts = db.get_contact_list()
    groups = db.get_group_list()
    random_contact = random.choice(contacts)
    random_group = random.choice(groups)

    pair = db.get_linked_pair()
    if pair is False:
        app.contact.add_relation(random_group, random_contact)
        pair = db.get_linked_pair()
    random_group = Group(id=str(pair[1]))
    random_contact = Contact(id=str(pair[0]))
    if db.check_relation(group=random_group, contact=random_contact):
        app.contact.del_relation(group=random_group, contact=random_contact)
        check = db.check_relation(group=random_group, contact=random_contact)
        assert check is False
