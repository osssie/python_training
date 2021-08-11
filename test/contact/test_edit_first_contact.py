# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="Editable", middlename="E", lastname="Contact"))
    app.contact.modify_first_contact(Contact(name="Mary", middlename="M", lastname="Marvel", nickname="Mary",
                                            title="Lead", company="Test", address="none", phone_home="09893333333",
                                            phone_mobile="09897776632", phone_work="09897776631", phone_fax="098933333",
                                            email="mary@a.cto", bday="4", bmonth="August", byear="1995"))
