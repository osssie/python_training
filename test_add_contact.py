# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import pytest
from contact import Contact
from contact_application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.tearDown)
    return fixture


def test_add_contact(app):
    app.addressbook_login(login='admin', password='secret')
    app.addressbook_fill_contact_data(Contact(name="Sofi", middlename="a", lastname="Turner", nickname="Sofi",
                                                           title="Namer", company="Test", address="none", phone_home="09897776633",
                                                           phone_mobile="09897776632", phone_work="09897776631", phone_fax="098977766",
                                                           email="sofi@a.cto", bday="9", bmonth="August", byear="1999"))
    app.addressbook_logout()
