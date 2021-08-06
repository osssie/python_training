class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def add_new_group(self):
        wd = self.app.wd
        self.open()
        wd.find_element_by_name("new").click()

    def create(self, group):
        wd = self.app.wd
        self.open()
        self.add_new_group()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        self.submit()
        self.open()

    def submit(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()
