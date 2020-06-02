from model.contact import Contact

testdata = [
    Contact(firstname="firstname", middlename="middlename", lastname="lastname",
            nickname="nickname", title="title", company="company",
            address="address", home="home",
            mobile="mobile", work="work", fax="fax", email="email",
            email2="email2", email3="emial3", homepage="homepage", bday="16", bmonth="November",
            byear="1981", aday="13", amonth="October", ayear="2000", address2="address2"),
            phone2="phone2", notes="notes")],
    Contact(firstname="firstname1", middlename="middlename1", lastname="lastname1",
            nickname="nickname1", title="title1", company="company1",
            address="address1", home="home1",
            mobile="mobile1", work="work1", fax="fax1", email="email",
            email2="email2", email3="emial3", homepage="homepage1", bday="16", bmonth="November",
            byear="1981", aday="13", amonth="October", ayear="2000", address2="address2"),
            phone2="phone2", notes="notes1")
]


#def random_string(prefix, maxlen):
#    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
#    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


#def random_phone_number():
#    symbols = string.digits
#    return "".join([random.choice(symbols) for i in range(9)])


#def random_emails(maxlen):
#    symbols = string.ascii_letters + string.digits
#    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@gmail.com"


#testdata = [
#        Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10), lastname=random_string("lastname", 10),
#                nickname=random_string("nickname", 10), title=random_string("title", 15), company=random_string("company", 15),
#                 address=random_string("address", 15), home=random_phone_number(),
#               mobile=random_phone_number(), work=random_phone_number(), fax=random_phone_number(), email=random_emails(20),
#                   email2=random_emails(20), email3=random_emails(20), homepage="none", bday="16", bmonth="November",
#                   byear="1981", aday="13", amonth="October", ayear="2000", address2=random_string("address2", 20),
#                  phone2=random_phone_number(), notes=random_string("notes", 10))] + [
#        Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
#                address="", home="", mobile="", work="", fax="", email="", email2="", email3="",
#                homepage="", bday="-", bmonth="-", byear="", aday="-", amonth="-", address2="",
#                phone2="", notes="")
#        for i in range(5)
#]