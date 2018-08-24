import json
import os
import random
import re
import string
import getopt
import sys

from model.group import Group

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    str = prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    return clear(str.strip())


def clear(s):
    return re.sub("\s+", " ", s)


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("testname", 10), header=random_string("testheader", 20),
          footer=random_string("testfooter", 20))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
