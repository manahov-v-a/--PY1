list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

#list_numbers[len(list_numbers)-1], list_numbers[list_numbers.index(max(list_numbers))]  = list_numbers[list_numbers.index(max(list_numbers))], list_numbers[len(list_numbers)-1]

max_index = 0
max_value = list_numbers[0]
for index, value in enumerate(list_numbers):
    if value > max_value:
        max_value = value
        max_index = index

list_numbers[max_index], list_numbers[-1] = list_numbers[-1], list_numbers[max_index]

print(list_numbers)
