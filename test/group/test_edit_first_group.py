# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="modify"))
    old_groups = app.group.get_group_list()
    app.group.edit(Group(name="Rename", header="header", footer="footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
