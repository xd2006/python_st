import re

import pytest
import random
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


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.group_count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
