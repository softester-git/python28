# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.contact import ContactHelper
import random
import pytest


testdata = [Contact(firstname="", address="", lastname="")] + [Contact(firstname=ContactHelper.random_string("firstname", 10),
                                                                          address=ContactHelper.random_string("address", 20),
                                                                          lastname=ContactHelper.random_string("lastname", 10),
                                                                          nickname=ContactHelper.random_string("nickname", 10),
                                                                        middlename=ContactHelper.random_string("title", 10),
                                                                       title=ContactHelper.random_string("title", 10),
                                                                       phone_home=random.randrange(10),
                                                                       fax=random.randrange(10),
                                                                       phone_work=ContactHelper.random_digit(10),
                                                                       phone_mobile=ContactHelper.random_digit(10),
                                                                       phone2=ContactHelper.random_digit(10),
                                                                       email=ContactHelper.random_string("email", 10),
                                                                       email2=ContactHelper.random_string("email2", 10),
                                                                       email3=ContactHelper.random_string("email3", 10),
                                                                       photo="title.gif",
                                                                       company=ContactHelper.random_string("company", 10),
                                                                       homepage=ContactHelper.random_string("homepage", 10),
                                                                       bday=str(random.randrange(1,28)),
                                                                       bmonth=ContactHelper.random_month(),
                                                                       byear=random.randrange(1970,2021),
                                                                       aday=str(random.randrange(1,28)),
                                                                       amonth=ContactHelper.random_month(),
                                                                       ayear=random.randrange(1970,2021),
                                                                       address2=ContactHelper.random_string("address2", 10),
                                                                       notes=ContactHelper.random_string("notes", 10),
                                                                       )
                                                     for i in range(5)]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(Contact(firstname=' '.join(contact.firstname.split()), lastname=' '.join(contact.lastname.split())))
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
