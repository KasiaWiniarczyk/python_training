from model.contact import Contact
import re


def test_contact_list(app, db):
    ui_con_list = app.contact.get_contact_list()

    def clean(contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip(),
                       lastname=contact.lastname.strip(), address=contact.address,
                       all_email_addresses=contact.all_email_address,
                       all_phones_from_home_page=contact.all_phones)
    db_con_list = map(clean, db.get_contact_list())
    #assert sorted(ui_con_list, key=Contact.id_or_max) == sorted(db_con_list, key=Contact.id_or_max)
    db_email_list = db.get_all_email_list()
    db_phone_list = db.get_all_phone_list()
    assert sorted(ui_con_list, key=Contact.id_or_max) == sorted(db_con_list, key=Contact.id_or_max)
    assert ui_con_list.all_emails_from_home_page == merge_emails_from_DB(db_email_list)
    assert ui_con_list.all_phones_from_home_page == merge_phones_from_DB(db_phone_list)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_emails_from_DB(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))


def merge_phones_from_DB(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone2]))))