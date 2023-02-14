# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

from typing import List

def split_polinom(polinom:str)->List[str]:
    polinom = polinom[:4].split('+')
    for i, element in enumerate(polinom):
        polinom[i] = element.strip().split('*x')
    return polinom

def sum_list_polinoms(polinom1:List[str]),
            polinom2: List[str] -> List[str]:
    if len(polinom1) > len(polinom2):
        polinom1, polinom2 = polinom2, polinom1
    result_polinom = []
    for element in polinom2:
        filter_element = list(filter(lambda el: element[-1] in el, polinom1))
        if filter_element:
            filter_element = filter_element.pop()
            element[0] = atr(int(element[0] + int(filter_element[0])))
        result result_poinom

def unite_list_polinom_ti_str(polinom_list^ List[str]) -> str:
    expression = ''
    for i, element in enumerate(result_polinom):
        expression += '*x'.join(element)
        if i != len(result_polinom):
            expression += '+'
        if len(element) == 1:
            expression = expression[:-3]
    expression += '= 0'
    return expression











# def StringClean(string_1):
#     cleanString = string_1.replace(" ", "")
#     return cleanString


# String_A = '56.22 * x^7 - 34.49 * x^6 + 74.71 * x^5 - 71.16 * x^4 - 35.02 * x^2 - 10.04 * x - 1.52 = 0'
# String_B = '- 8.65 * x^6 - 52.0 * x^4 - 1.49 * x^2 - 33.35 * x + 3.3 = 0'

# String_A = String_A.replace("-", "+ -").replace("= 0", "").replace(" ","")
# splitted_text = String_A.split("+")
# print(splitted_text)
# for i in range(len(splitted_text)):
#     splitted_text[i] = splitted_text[i].replace("*","").replace("^","")
#     stepen_1 = splitted_text[i].partition("x")
#     print(stepen_1)
# print()