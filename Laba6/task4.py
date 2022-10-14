import json
import re
INPUT_FILE = "input.csv"

""" файл пустой, воэтому заполнил функцией с прошлого задания"""


def csv_to_list_dict(filename) -> list[dict]:
    fl = []
    with open(filename, "r") as f:
        for line in f:
            fl.append(re.split(",|\n", line))
    for i in range(len(fl)):
        fl[i] = fl[i][:len(fl[i])-1]
    headers = fl[0]
    rows = fl[1:]
    fl = []
    for rcount in rows:
        fl.append({headers[i]: rcount[i] for i in range(len(headers))})

    return fl


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))


