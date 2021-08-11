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
        self.open()
        self.add_new_group()
        self.fill_group_form(group)
        self.submit()
        self.open()

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def submit(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def update(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open()
        self.select_first_group()
        wd.find_element_by_name("delete").click()
        self.open()

    def edit_first_group(self):
        wd = self.app.wd
        self.open()
        self.select_first_group()
        wd.find_element_by_name("edit").click()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open()
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        self.update()
        self.open()

    def edit(self, group):
        self.open()
        self.edit_first_group()
        self.fill_group_form(group)
        self.update()
        self.open()

