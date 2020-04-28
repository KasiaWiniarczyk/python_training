from model.group import Group

def test_modify_group2_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test2", header="Test", footer="Test2"))
    app.group.modify_first_group(Group(name="Test3"))

def test_modify_group2_header(app):
   # if app.group.count() == 0:
       # app.group.create(Group(name="Test2", header="Test", footer="Test5"))
    app.group.modify_first_group(Group(header="Test4"))
