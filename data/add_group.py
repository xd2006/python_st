import random
import re
import string

from model.group import Group


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    str = prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    return clear(str.strip())


def clear(s):
    return re.sub("\s+", " ", s)


testdata = [
               Group(name=name, header=header, footer=footer)
               for name in ["", random_string("testname", 10)]
               for header in ["", random_string("testheader", 20)]
               for footer in ["", random_string("testfooter", 20)]
           ]