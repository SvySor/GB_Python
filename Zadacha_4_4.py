# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def Random_A():
    A = round(random.uniform(-100, 100), 2)
    return A

k = 7
List_A = []
String_A = ""
for i in range(k+1):
    List_A.insert(0, Random_A())
List_A[3] = 0                           # Пример пропуска 0
print("Коэффициенты: ", List_A)

for i in range(k+1):
    if List_A[k-i] == 0:
        String_A += ''
    else:
        String_A += str(List_A[k - i]) + "*x^" + str(k - i) + " + "
String_A = String_A + "= 0"
String_Finish = String_A.replace('+ -', "- ").replace('+ =', "=").replace('^1', '').replace('*x^0', '').replace("*", ' * ')
print('Выражение:', String_Finish)
