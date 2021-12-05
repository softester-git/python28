# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="FirstName",
                               middlename="MiddleName",
                               lastname="LastName",
                               nickname="NickName",
                               company="Company",
                               title="Ttile",
                               address="Address",
                               phone_home="1001",
                               phone_mobile="1002",
                               phone_work="1003",
                               fax="1004",
                               email="email@email.email",
                               email2="email2@email2.email2",
                               email3="email3@email3.email3",
                               homepage="Homepage",
                               address2="Address2",
                               phone2="1005",
                               notes="Notes",
                               bday="5",
                               bmonth="May",
                               byear="1950",
                               aday="15",
                               amonth="March",
                               ayear="1955")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="", middlename="", lastname="", nickname="")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
