# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_group(self):
        wd = self.wd
        self.addressbook_open_homepage(wd)
        self.addressbook_login(wd, username="admin", password="secret")
        self.addressbook_opn_group_pge(wd)
        self.addressbook_new_group(wd)
        self.addressbook_fill_group_creation_form(wd, group_name="new test group", group_header="aaa", group_footer="eee")
        self.addressbook_submit_group_creation(wd)
        self.addressbook_click_home(wd)
        self.addressbook_opn_group_pge(wd)
        self.addressbook_logout(wd)

    def addressbook_logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def addressbook_click_home(self, wd):
        wd.find_element_by_link_text("home").click()

    def addressbook_submit_group_creation(self, wd):
        wd.find_element_by_name("submit").click()

    def addressbook_fill_group_creation_form(self, wd, group_name, group_header, group_footer):
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group_name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group_header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group_footer)

    def addressbook_new_group(self, wd):
        wd.find_element_by_name("new").click()

    def addressbook_opn_group_pge(self, wd):
        wd.find_element_by_link_text("groups").click()

    def addressbook_login(self, wd, username, password):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def addressbook_open_homepage(self, wd):
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
