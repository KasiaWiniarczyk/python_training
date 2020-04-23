from model.group import Group

def test_add_new_group(app):
    app.group.add_new_group(Group(name="Test100", header="Test200", footer="Test300"))