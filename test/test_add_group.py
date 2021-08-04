# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.tearDown)
    return fixture


def test_add_group(app):
    app.session.addressbook_login(username="admin", password="secret")
    app.addressbook_fill_group_creation_form(Group(name="new test group", header="aaa", footer="eee"))
    app.session.addressbook_logout()


def test_add_empty_group(app):
    app.session.addressbook_login(username="admin", password="secret")
    app.addressbook_fill_group_creation_form(Group(name="", header="", footer=""))
    app.session.addressbook_logout()

