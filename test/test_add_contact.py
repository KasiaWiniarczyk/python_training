# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application
from sys import maxsize

def test_add_contact(app):
        old_contacts = app.contact.get_contact_list()
        contact = Contact(firstname="John", middlename="Malcolm", lastname="Grey", nickname="John", title="QA", company="XCaliber", address="Compton Street", home="120745896",
                                   mobile="120632020", work="101862202", fax="170012580", email="john.grey@gmail.com", email2="john.grey1@gmail.com",
                                   email3="john.grey2@gmail.com", homepage="none", bday="16", bmonth="November", byear="1981", aday="13", amonth="October", address2="Artist Street",
                                   phone2="none", notes="none")
        app.contact.create(contact)
        new_contacts = app.contact.get_contact_list()
        assert len(old_contacts) + 1 == app.contact.count()
        new_contacts = app.contact.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_add_empty_contact(app):
        # old_contacts = app.contact.get_contact_list()
        # contact = Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                                # address="", home="", mobile="", work="", fax="", email="", email2="", email3="",
                                # homepage="", bday="-", bmonth="-", byear="", aday="-", amonth="-", address2="",
                                # phone2="", notes="")
        # app.contact.create(contact)
        # new_contacts = app.contact.get_contact_list()
        # assert len(old_contacts) + 1 == len(new_contacts)
        # old_contacts.append(contact)
        # assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
