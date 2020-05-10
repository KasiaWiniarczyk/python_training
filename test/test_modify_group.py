from model.group import Group
from random import randrange

def test_modify_group2_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test2", header="Test", footer="Test2"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="Test3")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_modify_group2_header(app):
   # if app.group.count() == 0:
       # app.group.create(Group(name="Test2", header="Test", footer="Test5"))
    #old_groups = app.group.get_group_list()
    #app.group.modify_first_group(Group(header="Test4"))
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)
