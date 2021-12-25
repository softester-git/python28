import getopt
import os.path
import random
import sys
import jsonpickle
from fixture.contact import ContactHelper
from model.contact import Contact

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)
n = 5
f = "data/contacts.json"
for a, o in opts:
    if a == "-n":
        n = int(o)
    elif a == "-f":
        f = o
testdata = [Contact(firstname="", middlename="", lastname="")] + [
    Contact(firstname=ContactHelper.random_string("firstname", 10),
            middlename=ContactHelper.random_string("middlename", 10),
            lastname=ContactHelper.random_string("lastname", 10),
            nickname=ContactHelper.random_string("nickname", 10),
            address=ContactHelper.random_string("address", 20),
            title=ContactHelper.random_string("title", 10),
            phone_home=ContactHelper.random_digit(10),
            phone_work=ContactHelper.random_digit(10),
            phone_mobile=ContactHelper.random_digit(10),
            phone2=ContactHelper.random_digit(10),
            fax=ContactHelper.random_digit(10),
            email=ContactHelper.random_string("email", 10),
            email2=ContactHelper.random_string("email2", 10),
            email3=ContactHelper.random_string("email3", 10),
            photo="title.gif",
            company=ContactHelper.random_string("company", 10),
            homepage=ContactHelper.random_string("homepage", 10),
            bday=str(random.randrange(1, 28)),
            bmonth=ContactHelper.random_month(),
            byear=random.randrange(1970, 2021),
            aday=str(random.randrange(1, 28)),
            amonth=ContactHelper.random_month(),
            ayear=random.randrange(1970, 2021),
            address2=ContactHelper.random_string("address2", 10),
            notes=ContactHelper.random_string("notes", 10))
    for i in range(n)]
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as fd:
    jsonpickle.set_encoder_options("json", indent=2)
    fd.write(jsonpickle.encode(testdata))
