# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="modify"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name='Modified Group'))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="modify"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header='Modified header'))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
