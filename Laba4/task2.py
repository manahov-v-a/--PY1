import string


def get_count_char(str_):
    str_ = str_.lower()
    list_ = str_.split()
    str_ = "".join(list_).translate(str_.maketrans('', '', string.punctuation))
    dict_ = {}
    for i in str_:
        if i not in dict_:
            dict_.setdefault(i, 1)
        else:
            dict_[i] += 1

    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
