
from model.contact import Contact
import re


def test_compare_db_homepage_contact(app, db):
    db_count = len(db.get_contact_list())
    homepage_list = sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)
    db_contact_list = db.get_contact_list()
    for i in range(db_count):
        contacts_from_homepage = homepage_list[i]
        contacts_from_db = db_contact_list[i]
        assert contacts_from_homepage.name == contacts_from_db.name
        assert contacts_from_homepage.lastname == contacts_from_db.lastname
        assert contacts_from_homepage.address == contacts_from_db.address
        assert contacts_from_homepage.all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_db)
        assert contacts_from_homepage.all_emails_from_home_page == merge_emails_like_on_home_page(contacts_from_db)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [contact.phone_home, contact.phone_mobile,
                                                            contact.phone_work, contact.phone_secondary]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))
