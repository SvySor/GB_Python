# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

My_List = [1, 45, 'валенок', 1, 45, 'башмак', 'dog', 'собака', 'cat', 'кот', 45, 1]
print(My_List)
print(type(My_List))
My_set = set( My_List)
My_unique_list = list(My_set)
print( My_unique_list)
