# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group(app):
    app.group.edit(Group(name="Rename", header="header", footer="footer"))
