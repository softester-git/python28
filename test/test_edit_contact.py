from model.contact import Contact
from random import randrange


def test_edit_contact_by_index(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Contact for edit"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="NewFirstname",
                      middlename="NewMiddlename",
                      lastname="NewLastname",
                      nickname="NewNickname",
                      title="NewTitle",
                      company="NewCompany",
                      address="NewAddress",
                      phone_home="110",
                      phone_mobile="111",
                      phone_work="112",
                      fax="113",
                      email="Newemail@test.test",
                      email2="Newemail2@test.test",
                      email3="Newemail3@test.test",
                      homepage="http://newhomepage.test",
                      bday="11",
                      bmonth="July",
                      byear="2010",
                      aday="15",
                      amonth="June",
                      ayear="2011",
                      address2="NewAddress2",
                      phone2="114",
                      notes="NewNotes")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_id(contact.id, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(app.contact.get_contact_list(), key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
