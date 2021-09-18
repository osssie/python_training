# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_delete_random_contact(app, data_contacts):
    contact = data_contacts
    if app.contact.count() == 0:
        app.contact.create(contact)
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index:index+1] = []
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
