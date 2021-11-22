from selenium import webdriver
from selenium.webdriver.support.ui import Select
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

    # Contact

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def create_contact(self, contact):
        wd = self.wd
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
        if contact.phone_home is not None:
            wd.find_element_by_name("home").clear()
            wd.find_element_by_name("home").send_keys(contact.phone_home)
        if contact.phone_mobile is not None:
            wd.find_element_by_name("mobile").clear()
            wd.find_element_by_name("mobile").send_keys(contact.phone_mobile)
        if contact.phone_work is not None:
            wd.find_element_by_name("work").clear()
            wd.find_element_by_name("work").send_keys(contact.phone_work)
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
