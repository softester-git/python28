# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from contact import Contact


class UntitledTestCase(unittest.TestCase):

    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        self.login(username="admin", password="secret")
        self.create_contact(Contact(firstname="FirstName",
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
        self.logout()

    def test_add_empty_contact(self):
        self.login(username="admin", password="secret")
        self.create_contact(Contact(firstname=""))
        self.logout()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def create_contact(self, contact):
        wd = self.wd
        self.open_home_page()
        # Open form
        wd.find_element_by_link_text("add new").click()
        # Fill form
        if contact.firstname is not None:
            wd.find_element_by_name("firstname").clear()
            wd.find_element_by_name("firstname").send_keys(contact.firstname)
        if contact.middlename is not None:
            wd.find_element_by_name("middlename").clear()
            wd.find_element_by_name("middlename").send_keys(contact.middlename)
        if contact.lastname is not None:
            wd.find_element_by_name("lastname").clear()
            wd.find_element_by_name("lastname").send_keys(contact.lastname)
        if contact.nickname is not None:
            wd.find_element_by_name("nickname").clear()
            wd.find_element_by_name("nickname").send_keys(contact.nickname)
        if contact.title is not None:
            wd.find_element_by_name("title").clear()
            wd.find_element_by_name("title").send_keys(contact.title)
        if contact.company is not None:
            wd.find_element_by_name("company").clear()
            wd.find_element_by_name("company").send_keys(contact.company)
        if contact.address is not None:
            wd.find_element_by_name("address").clear()
            wd.find_element_by_name("address").send_keys(contact.address)
        if contact.home is not None:
            wd.find_element_by_name("home").clear()
            wd.find_element_by_name("home").send_keys(contact.home)
        if contact.mobile is not None:
            wd.find_element_by_name("mobile").clear()
            wd.find_element_by_name("mobile").send_keys(contact.mobile)
        if contact.work is not None:
            wd.find_element_by_name("work").clear()
            wd.find_element_by_name("work").send_keys(contact.work)
        if contact.fax is not None:
            wd.find_element_by_name("fax").clear()
            wd.find_element_by_name("fax").send_keys(contact.fax)
        if contact.email is not None:
            wd.find_element_by_name("email").clear()
            wd.find_element_by_name("email").send_keys(contact.email)
        if contact.email2 is not None:
            wd.find_element_by_name("email2").clear()
            wd.find_element_by_name("email2").send_keys(contact.email2)
        if contact.email3 is not None:
            wd.find_element_by_name("email3").clear()
            wd.find_element_by_name("email3").send_keys(contact.email3)
        if contact.homepage is not None:
            wd.find_element_by_name("homepage").clear()
            wd.find_element_by_name("homepage").send_keys(contact.homepage)
        if contact.address2 is not None:
            wd.find_element_by_name("address2").clear()
            wd.find_element_by_name("address2").send_keys(contact.address2)
        if contact.phone2 is not None:
            wd.find_element_by_name("phone2").clear()
            wd.find_element_by_name("phone2").send_keys(contact.phone2)
        if contact.notes is not None:
            wd.find_element_by_name("notes").clear()
            wd.find_element_by_name("notes").send_keys(contact.notes)
        if contact.bday is not None:
            wd.find_element_by_name("bday").click()
            Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        if contact.bmonth is not None:
            wd.find_element_by_name("bmonth").click()
            Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        if contact.byear is not None:
            wd.find_element_by_name("byear").clear()
            wd.find_element_by_name("byear").send_keys(contact.byear)
        if contact.aday is not None:
            wd.find_element_by_name("aday").click()
            Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        if contact.amonth is not None:
            wd.find_element_by_name("amonth").click()
            Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        if contact.ayear is not None:
            wd.find_element_by_name("ayear").clear()
            wd.find_element_by_name("ayear").send_keys(contact.ayear)
        # Submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()

    def open_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home").click()

    def open_main_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def login(self, username, password):
        wd = self.wd
        self.open_main_page()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
