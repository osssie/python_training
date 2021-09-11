# -*- coding: utf-8 -*-
from model.contact import Contact



def test_add_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(name="Sofi", middlename="a", lastname="Turner", nickname="Sofi",
                                                title="Namer", company="Test", address="none", phone_home="09897776633",
                                                phone_mobile="09897776632", phone_work="09897776631", phone_secondary="0989777606",
                                                email="sofi@a.cto", bday="9", bmonth="August", byear="1999")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

