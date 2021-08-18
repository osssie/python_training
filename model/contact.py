from sys import maxsize


class Contact:

    def __init__(self, name=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None,
                 phone_home=None, phone_mobile=None, phone_work=None, phone_fax=None, email=None, bday=None,
                 bmonth=None, byear=None, id=None):
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
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.id  = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
