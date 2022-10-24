import string
from collections import Counter

def get_count_char(str_):
    str_ = str_.lower()
    str_ = "".join([i for i in "".join(str_.split()) if i.isalpha() == True])
    # str_ = "".join(list_).translate(str_.maketrans('', '', string.punctuation))
    return dict(Counter(list(str_)))

def procent_dict(dict_):
    sum_value = sum(dict_.values())
    for i in dict_:
        dict_['%s' % i] = dict_.get('%s' % i)/sum_value * 100
    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
