import mysql.connector
from model.group import Group
from contact.group import Contact


class Dbfixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(name=name, header=header, footer=footer, id=str(id)))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, email, email2, email3, home, mobile, homepage, notes, address2 work from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, email, email2, email3, home, mobile, homepage, notes, address2) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address,
                                    email=emial, email2=email2, email3=email3, home=home, mobile=mobile, homepage=homepage, notes=notes, address2=address2))
        finally:
            cursor.close()
        return list

    def get_all_email_list(self):
        list_all_emails = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, email, email2, email3 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, email, email2, email3) = row
                list_all_emails.append(Contact(id=str(id), email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list_all_emails

    def get_all_phone_list(self):
        list_all_phones = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, home, mobile, work, phone2 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, home, mobile, work, phone2) = row
                list_all_phones.append(Contact(id=str(id), home=home, mobile=mobile, work=work, phone2=phone2))
        finally:
            cursor.close()
        return list_all_phones

    def get_contacts_in_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, group_id from address_in_groups")
            for row in cursor:
                (id, group_id) = row
                list.append((Contact(id=id), Group(id=id)))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()