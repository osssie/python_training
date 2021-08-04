class GroupHelper:

    def __init__(self, app):
        self.app = app

    def addressbook_open(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def addressbook_new_group(self):
        wd = self.app.wd
        self.addressbook_open()
        wd.find_element_by_name("new").click()

    def addressbook_create(self, group):
        wd = self.app.wd
        self.addressbook_open()
        self.addressbook_new_group()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        self.addressbook_submit()
        self.addressbook_open()

    def addressbook_submit(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()
