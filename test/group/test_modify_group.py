# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name='Modified Group'))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(header='Modified header'))
