# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="FirstName",
                                    middlename="MiddleName",
                                    lastname="LastName",
                                    nickname="NickName",
                                    company="Company",
                                    title="Ttile",
                                    address="Address",
                                    home="1001",
                                    mobile="1002",
                                    work="1003",
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
    app.logout()


def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname=""))
    app.logout()
