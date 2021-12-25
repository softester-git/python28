#import mysql.connector
#import pymysql.cursors
#from fixture.db import DbFixture
from fixture.orm import ORMFixture
from model.group import Group

#connection = mysql.connector.connect(host="localhost", database="addressbook", user="root", password="")
#connection = pymysql.connect(host="localhost", database="addressbook", user="root", password="")
#db = DbFixture(host="localhost", name="addressbook", user="root", password="")
db = ORMFixture(host="localhost", name="addressbook", user="root", password="")


try:
    l = db.get_contacts_not_in_group(Group(id="130"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass #db.destroy()
