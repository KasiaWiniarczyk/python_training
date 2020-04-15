from model.contact import Contact

def test_add_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_new_contact(Contact(firstname="Thomas", middlename="Malcolm", lastname="Grey", nickname="John", title="QA", company="XCaliber", address="Compton Street", home="120745896",
                                   mobile="120632020", work="101862202", fax="170012580", email="john.grey@gmail.com", email2="john.grey1@gmail.com",
                                   email3="john.grey2@gmail.com", homepage="none", bday="16", bmonth="November", byear="1981", aday="13", amonth="October", ayear="2005", address2="Artist Street",
                                   phone2="none", notes="none"))
    app.session.logout()