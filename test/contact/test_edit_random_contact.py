# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange
import allure


def test_edit_random_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact)
    with allure.step('Given a non-empty contact list'):
        old_contacts = db.get_contact_list()
    with allure.step('Given a random contact from the list'):
        index = randrange(len(old_contacts))
        contact = Contact(name="Mary", middlename="KEE", lastname="Marvel", nickname="Mary",
                      title="Lead", company="Test", address="none", phone_home="09893333333",
                      phone_mobile="09897776632", phone_work="09897776631", phone_secondary="098933333",
                      email="mary@a.cto", bday="4", bmonth="August", byear="1995")
        contact.id = old_contacts[index].id
    with allure.step('When I modify the contact from the list'):
        app.contact.modify_contact_by_id(contact.id, contact)
    with allure.step('Then the new contact list is equal to the old list with modified contact'):
        new_contacts = db.get_contact_list()
        assert len(old_contacts) == app.contact.count()
        old_contacts[index] = contact
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_contact_list(), key=Contact.id_or_max)
