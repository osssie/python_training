
from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(name="Ivan", lastname="Ivanov", phone_home="1199989", phone_mobile="2211345",
                                   phone_work="443453", phone_secondary="000123", address="citystreethome",
                                   email="ivan@mail.com", email2="ivan@mail.com", email3="ivan@mail.com"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Test"))
    groups = db.get_group_list()
    group = random.choice(groups)
    contacts = db.get_contacts_not_in_group(Group(id=group.id))
    if not contacts:
        app.contact.create(Contact(name="Ivan", lastname="Ivanov", phone_home="1199989", phone_mobile="2211345",
                                   phone_work="443453", phone_secondary="000123", address="citystreethome",
                                   email="ivan@mail.com", email2="ivan@mail.com", email3="ivan@mail.com"))
        contacts = db.get_contacts_not_in_group(Group(id=group.id))
    contact = random.choice(contacts)
    old_contacts_in_group = list(db.get_contacts_in_group(Group(id=group.id)))
    app.contact.add_to_group_by_id(contact.id, group.name)
    new_contacts_in_group = list(db.get_contacts_in_group(Group(id=group.id)))
    assert len(old_contacts_in_group) + 1 == len(new_contacts_in_group)
    assert contact in new_contacts_in_group


def test_delete_contact_of_group(app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="name1", header="header1", footer="footer1"))
    if len(db.get_contact_list()) == 0:
        if len(db.get_contact_list()) == 0:
            app.contact.create(Contact(name="Ivan", lastname="Ivanov", phone_home="1199989", phone_mobile="2211345",
                                       phone_work="443453", phone_secondary="000123", address="citystreethome",
                                       email="ivan@mail.com", email2="ivan@mail.com", email3="ivan@mail.com"))
    groups_with_contacts = db.get_not_empty_group()
    if len(groups_with_contacts) == 0:
        rand_group = random.choice(db.get_group_list())
        rand_contact = random.choice(db.get_contact_list())
        app.contact.add_to_group_by_id(rand_contact.id, rand_group.name)
        groups_with_contacts = db.get_not_empty_group()
    group = random.choice(groups_with_contacts)
    contacts = db.get_contacts_in_group(group)
    contact = random.choice(contacts)
    app.contact.delete_from_group_by_id(contact.id, group.name)
    contact_in_group = list(db.get_contacts_in_group(Group(id=group.id)))
    assert contact not in contact_in_group