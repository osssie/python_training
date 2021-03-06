from sys import maxsize


class Contact:

    def __init__(self, name=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None,
                 phone_home=None, phone_mobile=None, phone_work=None, phone_fax=None, email=None, email2=None,
                 email3=None, bday=None, bmonth=None, byear=None, id=None, all_phones_from_home_page=None,
                 address2=None, phone_secondary=None, notes=None, all_emails_from_home_page=None):
        self.name = name
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.phone_home = phone_home
        self.phone_mobile = phone_mobile
        self.phone_work = phone_work
        self.phone_fax = phone_fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.address2 = address2
        self.phone_secondary = phone_secondary
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
