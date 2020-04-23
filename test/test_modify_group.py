from model.group import Group

def test_modify_group2_name(app):
    app.group.modify_first_group(Group(name="Test3"))

def test_modify_group2_header(app):
    app.group.modify_first_group(Group(header="Test4"))
