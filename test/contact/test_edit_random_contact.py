# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_edit_random_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="Editable", middlename="E", lastname="Contact"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    contact = Contact(name="Mary", middlename="M", lastname="Marvel", nickname="Mary",
                                            title="Lead", company="Test", address="none", phone_home="09893333333",
                                            phone_mobile="09897776632", phone_work="09897776631", phone_secondary="098933333",
                                            email="mary@a.cto", bday="4", bmonth="August", byear="1995")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
