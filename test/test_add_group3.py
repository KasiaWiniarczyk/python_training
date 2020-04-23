# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group2(app):
        app.group.create(Group(name="Test2", header="Test", footer="Test2"))

def test_add_empty_group2(app):
        app.group.create(Group(name="", header="", footer=""))


