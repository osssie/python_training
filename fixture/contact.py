from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_name("Send e-Mail")) > 0):
            wd.find_element_by_link_text("home").click()

    def add_new(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def edit_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def edit_contact_by_id(self, id):
        wd = self.app.wd
        element = wd.find_element_by_css_selector("input[id='%s']" % id)
        row = element.find_element_by_xpath(".//ancestor::tr")
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

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
        self.change_field_value("phone2", contact.phone_secondary)
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

    def modify_contact_by_index(self, index, contact):
        self.open()
        self.edit_contact_by_index(index)
        self.fill_contact_form(contact)
        self.update()
        self.open()
        self.contact_cache = None

    def modify_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.edit_contact_by_id(id)
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.app.open_homepage()
        self.contact_cache = None

    def submit(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def update(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def delete_first(self):
        self.delete_contact_by_index(0)

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_contact_by_index(self,index):
        wd = self.app.wd
        self.open()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_homepage()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.open_homepage()
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
                cells = element.find_elements_by_tag_name("td")
                lastname = cells[1].text
                name = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                self.contact_cache.append(Contact(name=name, lastname=lastname, address=address, id=id,
                                                  all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails))

        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name('a').click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name('a').click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        name = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        phone_home = wd.find_element_by_name("home").get_attribute("value")
        phone_mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone_work = wd.find_element_by_name("work").get_attribute("value")
        phone_secondary = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        # print("name " + name)
        # print("lastname " + lastname)
        # print("id " + id)
        # print("phone_home " + phone_home)
        # print("phone_mobile " + phone_mobile)
        # print("phone_work " + phone_work)
        # print("phone_secondary " + phone_secondary)
        # print("address " + address)
        # print("email "+ email)
        # print("email2 " + email2)
        # print("email3 " + email3)
        return Contact(name=name, lastname=lastname, id=id,
                       phone_home=phone_home, phone_mobile=phone_mobile, phone_work=phone_work,
                       phone_secondary=phone_secondary,
                       address=address, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        split = re.split("\n", text, maxsplit=15)
        fullname = split[0]
        split1 = re.split((" "), fullname, maxsplit=2)
        name = split1[0]
        lastname = split1[2]
        phone_home = re.search("H: (.*)", text).group(1)
        phone_mobile = re.search("M: (.*)", text).group(1)
        phone_work = re.search("W: (.*)", text).group(1)
        phone_secondary = re.search("P: (.*)", text).group(1)
        address = split[4]
        email = split[11]
        email2 = split[12]
        email3 = split[13]
        # print(split)
        # print(fullname)
        # print(split1)
        # print("name " + name)
        # print("lastname " + lastname)
        # print("phone_home " + phone_home)
        # print("phone_mobile " + phone_mobile)
        # print("phone_work " + phone_work)
        # print("address " + address)
        # print("email " + email)
        # print("email2 " + email2)
        # print("email3 " + email3)
        return Contact(name=name, lastname=lastname,
                       phone_home=phone_home, phone_mobile=phone_mobile, phone_work=phone_work,
                       phone_secondary=phone_secondary,
                       address=address, email=email, email2=email2, email3=email3)




