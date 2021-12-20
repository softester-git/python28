# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from selenium.webdriver.support.select import Select
import re


class Application:

    def __init__(self, browser, baseUrl):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            options = Options()
            options.binary_location = "/usr/bin/google-chrome-stable"
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            self.wd = webdriver.Chrome(chrome_options=options, executable_path=r'/usr/local/bin/chromedriver')
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.baseUrl = baseUrl

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.get(self.baseUrl)

    def change_field(self, field_name, text):
        wd = self.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_field_select(self, field_name, text):
        wd = self.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def merge_phones_like_on_home_page(self, cont):
        merged_phones = "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear(x),
                                    filter(lambda x: x is not None,
                                           [cont.phone_home, cont.phone_mobile, cont.phone_work, cont.phone2]))))
        return(merged_phones)

    def merge_emails_like_on_home_page(self, cont):
        merged_emails = "\n".join(filter(lambda x: x != "",
                                       filter(lambda x: x is not None,
                                              [cont.email, cont.email2, cont.email3])))
        return(merged_emails)

    def clear(self, s):
        return (re.sub("[() -]", "", s))
