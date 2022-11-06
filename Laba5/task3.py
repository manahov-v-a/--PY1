import random


def get_unique_list_numbers() -> list[int]:
    a = []
    for i in range(15):
        while True:
            b = random.randint(-10, 10)
            if b not in a:
                a.append(b)
                break
    return a


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
