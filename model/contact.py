from sys import maxsize


class Contact:

    def __init__(self, id=None,
                 firstname=None,
                 middlename=None,
                 lastname=None,
                 nickname=None,
                 photo=None,
                 title=None,
                 company=None,
                 address=None,
                 phone_home=None,
                 phone_mobile=None,
                 phone_work=None,
                 fax=None,
                 email=None,
                 email2=None,
                 email3=None,
                 homepage=None,
                 bday=None,
                 bmonth=None,
                 byear=None,
                 aday=None,
                 amonth=None,
                 ayear=None,
                 new_group=None,
                 address2=None,
                 phone2=None,
                 notes=None):
        self.id = id
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.photo = photo
        self.title = title
        self.company = company
        self.address = address
        self.phone_home = phone_home
        self.phone_mobile = phone_mobile
        self.phone_work = phone_work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.new_group = new_group
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes

    def __repr__(self):
        return("%s:%s:%s" % (self.id, self.lastname, self.firstname))

    def __eq__(self, other):
        return((self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and self.firstname == other.firstname)

    def id_or_max(cn):
        if cn.id:
            return(int(cn.id))
        else:
            return(maxsize)