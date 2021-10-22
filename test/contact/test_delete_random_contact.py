# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import allure


def test_delete_random_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact)
    with allure.step('Given a non-empty contact list'):
        old_contacts = db.get_contact_list()
    with allure.step('Given a random contact from the list'):
        contact = random.choice(old_contacts)
    with allure.step('When I delete the contact from the list'):
        app.contact.delete_contact_by_id(contact.id)
    with allure.step('Then the new contact list is equal to the old list without deleted contact'):
        new_contacts = db.get_contact_list()
        assert len(old_contacts) - 1 == len(new_contacts)
        old_contacts.remove(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_contact_list(), key=Contact.id_or_max)
