# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange
import re


def test_compare_contact_on_homepage(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="Mary", middlename="M", lastname="Marvel", nickname="Mary",
                                            title="Lead", company="Test", address="none", phone_home="09893333333",
                                            phone_mobile="09897776632", phone_work="09897776631", phone_fax="098933333",
                                            email="mary@a.cto", bday="4", bmonth="August", byear="1995"))
        contact_from_home_page = app.contact.get_contacts_list()[0]
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)

        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(
            contact_from_edit_page)
        assert contact_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(contact_from_edit_page)


def test_compare_contact_on_viewpage(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="Mary", middlename="M", lastname="Marvel", nickname="Mary",
                                            title="Lead", company="Test", address="none", phone_home="09893333333",
                                            phone_mobile="09897776632", phone_work="09897776631", phone_fax="098933333",
                                            email="mary@a.cto", bday="4", bmonth="August", byear="1995"))
        old_contacts = app.contact.get_contacts_list()
        index = randrange(len(old_contacts))
        contact = Contact()
        contact.id = old_contacts[index].id
        contact_from_view_page = app.contact.get_contact_from_view_page(index)
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
        assert contact_from_view_page.name == contact_from_edit_page.name
        assert contact_from_view_page.lastname == contact_from_edit_page.lastname
        assert contact_from_view_page.address == contact_from_edit_page.address
        assert contact_from_view_page.phone_home == contact_from_edit_page.phone_home
        assert contact_from_view_page.phone_mobile == contact_from_edit_page.phone_mobile
        assert contact_from_view_page.phone_work == contact_from_edit_page.phone_work
        assert contact_from_view_page.phone_fax == contact_from_edit_page.phone_fax
        assert contact_from_view_page.email == contact_from_edit_page.email
        assert contact_from_view_page.email2 == contact_from_edit_page.email2
        assert contact_from_view_page.email3 == contact_from_edit_page.email3


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [contact.phone_home, contact.phone_mobile,
                                                            contact.phone_work, contact.phone_fax]))))


def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [contact.email, contact.email2, contact.email3]))))


