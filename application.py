from selenium import webdriver

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def addressbook_open_homepage(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def addressbook_login(self, username, password):
        wd = self.wd
        self.addressbook_open_homepage()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

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

    def addressbook_logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()


    def tearDown(self):
        self.wd.quit()