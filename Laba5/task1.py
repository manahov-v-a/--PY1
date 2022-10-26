from pprint import pprint

a = ["bin", "dec", "hex", "oct"]


def gre(name, value):
    if name == a[0]:
        return bin(value)
    if name == a[1]:
        return value
    if name == a[2]:
        return hex(value)
    if name == a[3]:
        return oct(value)


res = []
for i in range(16):
    res.append({x: gre(x, i) for x in a})
pprint(res)
