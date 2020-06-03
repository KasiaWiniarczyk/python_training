import random
from model.contact import Contact
from model.group import Group


def test_add_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="Tom", notes="test"))
    if len(db.get_group_list()) == 0:
        app.group.create_group(Group(name="test"))
    old_contacts_in_groups = db.get_contacts_in_group_list()
    contacts = db.get_contact_list()
    groups = db.get_group_list()
    contact_for_group = random.choice(contacts)
    group_for_contact = random.choice(groups)
    app.contact.add_contact_for_group(contact_for_group.contact_id, group_for_contact.group_id)
    new_contacts_in_groups = db.get_contacts_in_group_list()
    assert len(old_contacts_in_groups) + 1 == len(new_contacts_in_groups)