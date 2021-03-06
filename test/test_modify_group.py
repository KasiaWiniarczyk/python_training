from model.group import Group
import random

def test_modify_group2_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Test2", header="Test", footer="Test2"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group = Group(name="Test3")
    app.group.modify_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

#def test_modify_group2_header(app):
   # if app.group.count() == 0:
       # app.group.create(Group(name="Test2", header="Test", footer="Test5"))
    #old_groups = app.group.get_group_list()
    #app.group.modify_first_group(Group(header="Test4"))
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)
