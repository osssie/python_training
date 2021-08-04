from selenium import webdriver
from fixture.session import SessionHelper

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)

    def addressbook_open_homepage(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def addressbook_opn_group_pge(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def addressbook_new_group(self):
        wd = self.wd
        self.addressbook_opn_group_pge()
        wd.find_element_by_name("new").click()

    def addressbook_fill_group_creation_form(self, group):
        wd = self.wd
        self.addressbook_new_group()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        self.addressbook_submit_group_creation()
        self.addressbook_click_home()
        self.addressbook_opn_group_pge()

    def addressbook_submit_group_creation(self):
        wd = self.wd
        wd.find_element_by_name("submit").click()

    def addressbook_click_home(self):
        wd = self.wd
        wd.find_element_by_link_text("home").click()

    def addressbook_add_new_contact(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

    def addressbook_fill_contact_data(self, contact):
        wd = self.wd
        self.addressbook_add_new_contact()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").send_keys(contact.name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").send_keys(contact.phone_home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").send_keys(contact.phone_mobile)
        wd.find_element_by_name("work").send_keys(contact.phone_work)
        wd.find_element_by_name("fax").send_keys(contact.phone_fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("bday").click()
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        wd.find_element_by_name("theform").click()
        self.addressbook_contact_create()

    def addressbook_contact_create(self):
        wd = self.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def tearDown(self):
        self.wd.quit()