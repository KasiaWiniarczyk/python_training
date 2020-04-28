from model.contact import Contact

def test_update_contact(app):
    app.contact.update_contact(Contact(firstname="Peter", middlename="George", lastname="Pink", nickname="John", title="QA", company="XCaliber", address="Compton Street", home="120745896",
                                   mobile="120632020", work="101862202", fax="170012580", email="john.grey@gmail.com", email2="john.grey1@gmail.com",
                                   email3="john.grey2@gmail.com", homepage="none", bday="16", bmonth="November", byear="1981", aday="13", ayear="2005", amonth="October", address2="Artist Street",
                                   phone2="none", notes="none"))