class ContactHelper:

    def __init__(self, app):
        self.app = app

    def addressbook_add_new(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def addressbook_create(self, contact):
        wd = self.app.wd
        self.addressbook_add_new()
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
        self.addressbook_submit()

    def addressbook_submit(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()