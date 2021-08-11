# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="Editable", middlename="E", lastname="Contact"))
    app.contact.delete_first()
