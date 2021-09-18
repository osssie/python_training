from model.group import Group
import random
import string
import os.path
import json


def random_string(prefix, maxLen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxLen))])


testdata = [
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string("name", 10)]
    for header in ["", random_string("header", 10)]
    for footer in ["", random_string("footer", 10)]
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/groups.json")

with open(file, "w") as f:
    f.write(json.dumps(testdata))