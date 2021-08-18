from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_name("Send e-Mail")) > 0):
            wd.get("http://localhost/addressbook/index.php")

    def add_new(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def edit_first(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.name)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.phone_home)
        self.change_field_value("mobile", contact.phone_mobile)
        self.change_field_value("work", contact.phone_work)
        self.change_field_value("fax", contact.phone_fax)
        self.change_field_value("email", contact.email)
        wd.find_element_by_name("bday").click()
        wd.find_element_by_name("bmonth").click()
        self.change_field_value("byear", contact.byear)

    def create(self, contact):
        self.open()
        self.add_new()
        self.fill_contact_form(contact)
        self.submit()
        self.open()
        self.contact_cache = None

    def modify_first_contact(self, contact):
        self.open()
        self.edit_first()
        self.fill_contact_form(contact)
        self.update()
        self.open()
        self.contact_cache = None

    def submit(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def update(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def delete_first(self):
        wd = self.app.wd
        self.open()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cell = element.find_elements_by_tag_name("td")
                name = cell[2]
                lastname = cell[1]
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(name=name.text, lastname=lastname.text, id=id))

        return list(self.contact_cache)
