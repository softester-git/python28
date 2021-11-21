# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from contact import Contact
from application import Application


class UntitledTestCase(unittest.TestCase):

    def setUp(self):
        self.app = Application()

    def test_add_contact(self):
        self.app.login(username="admin", password="secret")
        self.app.create_contact(Contact(firstname="FirstName",
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
        self.app.logout()

    def test_add_empty_contact(self):
        self.app.login(username="admin", password="secret")
        self.app.create_contact(Contact(firstname=""))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()
