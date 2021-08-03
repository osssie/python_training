# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.tearDown)
    return fixture


def test_add_group(app):
    app.addressbook_login(username="admin", password="secret")
    app.addressbook_fill_group_creation_form(Group(name="new test group", header="aaa", footer="eee"))
    app.addressbook_logout()


def test_add_empty_group(app):
    app.addressbook_login(username="admin", password="secret")
    app.addressbook_fill_group_creation_form(Group(name="", header="", footer=""))
    app.addressbook_logout()

