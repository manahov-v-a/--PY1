# TODO продолжить заполнение словаря
dict_hex = {}
for i in range(16):
    a = ((hex(i))[::-1].capitalize())[::-1]
    dict_hex.update({a: i})

print(dict_hex)

