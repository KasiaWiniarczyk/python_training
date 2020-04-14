# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group2(app):
        app.session.login(username="admin", password="secret")
        app.group.create(Group(name="Test2", header="Test", footer="Test2"))
        app.session.logout()


def test_add_empty_group2(app):
        app.session.login(username="admin", password="secret")
        app.group.create(Group(name="", header="", footer=""))
        app.session.logout()


