from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(prefix, maxlen):
    numbers = string.digits
    return prefix + "".join([random.choice(numbers) for i in range(random.randrange(maxlen))])


def random_mail(maxlen):
    mail = ''.join(random.choice(string.ascii_letters) for _ in range(maxlen))
    return (mail + "@mail.com")


testdata = [Contact(name="", middlename="", lastname="", nickname="", title="", company="", address="",
                    phone_home="", phone_mobile="", phone_work="", phone_secondary="", email="", email2="", email3="")] \
    + [
    Contact(name=random_string("name", 10), middlename=random_string("middlename", 6),
            lastname=random_string("lastname", 10), nickname=random_string("nickname", 5),
            title=random_string("title", 5), company=random_string("company", 10),
            address=random_string("address", 20), phone_home=random_phone("phone_home", 8),
            phone_mobile=random_phone("phone_mobile", 8),
            phone_work=random_phone("phone_work", 8), phone_secondary=random_phone("phone_secondary", 8),
            email=random_mail(5), email2=random_mail(8), email3=random_mail(8),
            bday="9", bmonth="August", byear="1999")
    for i in range(3)
    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as cont:
    jsonpickle.set_encoder_options("json", indent=2)
    cont.write(jsonpickle.encode(testdata))
