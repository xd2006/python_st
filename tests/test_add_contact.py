import random
import re
import string

import pytest

from fixture.application import Application
from model.contact import Contact


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    str = prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    return clear(str.strip())


def random_mail(maxlen):
    symbols = string.ascii_letters + string.digits
    str = "".join([random.choice(symbols) for i in range(random.randrange(maxlen // 2))]) + "@"
    str += "".join([random.choice(symbols) for i in range(random.randrange(maxlen // 2))]) + "."
    str += "".join([random.choice(symbols) for i in range(3)])
    return str


def random_month():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    return random.choice(months)


def random_day(maxday):
    return random.choice(range(maxday))


def random_year(minyear, maxyear):
    return random.choice(range(minyear, maxyear))


def random_phone(prefix, maxlen):
    symbols = string.digits + " " * 10 + "(" + ")" + "-"
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def clear(s):
    return re.sub("\s+", " ", s)


testdata = [
    Contact(first_name=random_string("TestName", 15), middle_name=random_string("TestMiddle", 15),
            last_name=random_string("TestLat", 15),
            nickname=random_string("NickTest", 10), title=random_string("TestTitle", 10),
            company=random_string("Test Co", 15),
            address=random_string("Address", 40), homephone=random_phone("+", 15), workphone=random_phone("+3(75)", 11),
            mobilephone=random_phone("8(029)", 12),
            email=random_mail(16), email2=random_mail(10), email3=random_mail(20),
            homepage=random_string("somepage", 5), day_of_birth=str(random_day(28)),
            month_of_birth=random_month(), year_of_birth=str(random_year(1900, 2018)))
    for i in range(3)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app: Application, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add(contact)
    assert len(old_contacts) + 1 == app.contact.contact_count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
