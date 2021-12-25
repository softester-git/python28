import mysql.connector
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                group_list.append(Group(id=str(id), name=name.strip(), header=header, footer=footer))
        finally:
            cursor.close()
        return(group_list)

    def get_contact_list(self):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, work, mobile, phone2, email, email2, email3 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, home, work, mobile, phone2, email, email2, email3) = row
                contact_list.append(Contact(id=str(id),
                                            firstname=" ".join(firstname.split()),
                                            lastname=" ".join(lastname.split()),
                                            address=" ".join(address.split()),
                                            phone_home=" ".join(home.split()),
                                            phone_work=" ".join(work.split()),
                                            phone_mobile=" ".join(mobile.split()),
                                            phone2=" ".join(phone2.split()),
                                            email=" ".join(email.split()),
                                            email2=" ".join(email2.split()),
                                            email3=" ".join(email3.split())))
        finally:
            cursor.close()
        return(contact_list)

    def destroy(self):
        self.connection.close()