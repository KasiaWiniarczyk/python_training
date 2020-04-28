from model.contact import Contact

def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="John", middlename="Malcolm", lastname="Grey", nickname="John", title="QA",
                                   company="XCaliber", address="Compton Street", home="120745896",
                                   mobile="120632020", work="101862202", fax="170012580", email="john.grey@gmail.com",
                                   email2="john.grey1@gmail.com",
                                   email3="john.grey2@gmail.com", homepage="none", bday="16", bmonth="November",
                                   byear="1981", aday="13", amonth="October", address2="Artist Street",
                                   phone2="none", notes="none"))
    app.contact.modify_first_contact(Contact(firstname="Greg", bday="16", bmonth="November", byear="1981", aday="13", amonth="October"))


def test_modify_contact_lastname(app):
    app.contact.modify_first_contact(Contact(lastname="Blue", bday="16", bmonth="November", byear="1981", aday="13", amonth="October"))