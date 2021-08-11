# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="Editable", middlename="E", lastname="Contact"))
    app.contact.create(Contact(name="Sofi", middlename="a", lastname="Turner", nickname="Sofi",
                                                title="Namer", company="Test", address="none", phone_home="09897776633",
                                                phone_mobile="09897776632", phone_work="09897776631", phone_fax="098977766",
                                                email="sofi@a.cto", bday="9", bmonth="August", byear="1999"))
