from model.contact import Contact
from random import randrange

def test_modify_contact_firstname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="John", middlename="Malcolm", lastname="Grey", nickname="John", title="QA",
                                   company="XCaliber", address="Compton Street", home="120745896",
                                   mobile="120632020", work="101862202", fax="170012580", email="john.grey@gmail.com",
                                   email2="john.grey1@gmail.com",
                                   email3="john.grey2@gmail.com", homepage="none", bday="16", bmonth="November",
                                   byear="1981", aday="13", amonth="October", address2="Artist Street",
                                   phone2="none", notes="none"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact = Contact(firstname="Greg", lastname="Peter", bday="16", bmonth="November", byear="1981", aday="13", amonth="October")
    app.contact.modify_contact_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


#def test_modify_contact_lastname(app):
    #old_contacts = app.contact.get_contact_list()
    #app.contact.modify_first_contact(Contact(lastname="Blue", bday="16", bmonth="November", byear="1981", aday="13", amonth="October"))
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) == len(new_contacts)