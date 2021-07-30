# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from contact import Contact



class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_add_contact(self):
        driver = self.driver
        self.addressbook_open_homepage(driver)
        self.addressbook_login(driver, login='admin', password='secret')
        self.addressbook_add_new_contact(driver)
        self.addressbook_fill_contact_data(driver, Contact(name="Sofi", middlename="a", lastname="Turner", nickname="Sofi",
                                                           title="Namer", company="Test", address="none", phone_home="09897776633",
                                                           phone_mobile="09897776632", phone_work="09897776631", phone_fax="098977766",
                                                           email="sofi@a.cto", bday="9", bmonth="August", byear="1999"))
        self.addressbook_contact_create(driver)
        self.addressbook_logout(driver)

    def addressbook_logout(self, driver):
        driver.find_element_by_link_text("Logout").click()

    def addressbook_contact_create(self, driver):
        driver.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def addressbook_fill_contact_data(self, driver, contact):
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").send_keys(contact.name)
        driver.find_element_by_name("middlename").click()
        driver.find_element_by_name("middlename").send_keys(contact.middlename)
        driver.find_element_by_name("lastname").send_keys(contact.lastname)
        driver.find_element_by_name("nickname").send_keys(contact.nickname)
        driver.find_element_by_name("title").send_keys(contact.title)
        driver.find_element_by_name("company").send_keys(contact.company)
        driver.find_element_by_name("address").send_keys(contact.address)
        driver.find_element_by_name("home").send_keys(contact.phone_home)
        driver.find_element_by_name("mobile").click()
        driver.find_element_by_name("mobile").send_keys(contact.phone_mobile)
        driver.find_element_by_name("work").send_keys(contact.phone_work)
        driver.find_element_by_name("fax").send_keys(contact.phone_fax)
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").send_keys(contact.email)
        driver.find_element_by_name("email2").click()
        driver.find_element_by_name("bday").click()
        Select(driver.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        driver.find_element_by_name("bmonth").click()
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        driver.find_element_by_name("byear").click()
        driver.find_element_by_name("byear").send_keys(contact.byear)
        driver.find_element_by_name("theform").click()


    def addressbook_add_new_contact(self, driver):
        driver.find_element_by_link_text("add new").click()

    def addressbook_login(self, driver, login="admin", password="secret"):
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").send_keys(login)
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_id("LoginForm").submit()

    def addressbook_open_homepage(self, driver):
        driver.get("http://localhost/addressbook/index.php")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
