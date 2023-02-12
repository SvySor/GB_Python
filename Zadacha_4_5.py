# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


def StringClean(string_1):
    cleanString = string_1.replace(" ", "")
    return cleanString


String_A = '56.22 * x^7 - 34.49 * x^6 + 74.71 * x^5 - 71.16 * x^4 - 35.02 * x^2 - 10.04 * x - 1.52 = 0'
String_B = '- 8.65 * x^6 - 52.0 * x^4 - 1.49 * x^2 - 33.35 * x + 3.3 = 0'

String_A = String_A.replace("-", "+ -").replace("= 0", "").replace(" ","")
splitted_text = String_A.split("+")
print(splitted_text)
for i in range(len(splitted_text)):
    splitted_text[i] = splitted_text[i].replace("*","").replace("^","")
    stepen_1 = splitted_text[i].partition("x")
    print(stepen_1)
print()