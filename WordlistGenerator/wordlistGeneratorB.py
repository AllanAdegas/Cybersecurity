import itertools
import string

string = itertools.permutations(string.ascii_letters + string.digits + "!@#$%¨&*()'-=_+?<>,.;/", 8)

for i in string:
    print(''.join(i))