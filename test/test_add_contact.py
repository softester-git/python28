# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="FirstName",
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
                               ayear="1955"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname=""))
    app.session.logout()
