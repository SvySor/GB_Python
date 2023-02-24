# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод: 
# пара-ра-рам рам-пам-папам па-ра-па-дам

# Вывод:
# Парам пам-пам


def Input_data():
    #poem = input('Введите текст стихотворения: ')
    poem = 'Пара-ра-рам Рам-пам-папам Па-ра-па-дам Ап-ра-Ап-ам'
    return poem

def Devide_by_phrase(my_str):
    my_list = my_str.split()
    return my_list

def Syllabe_count(string):
    counter = 0
    string = string.lower()
    letter_list = list(string)
    for i in letter_list:
        if i in vowel_list:
            counter += 1
    return counter

vowel_list = ('a', 'e', 'i', 'o', 'u', 'y', 'а', 'у', 'о', 'и', 'э', 'ы')

rythm_OK = True
poem = Input_data()
poem_list = Devide_by_phrase(poem)
count = Syllabe_count(poem_list[0])
for phrase in poem_list:
    old_count = count
    count = Syllabe_count(phrase)
    if old_count != count:
        rythm_OK = False

if rythm_OK:
    print('Парам пам-пам, ритм в порядке')
else:
    print('Пам парам, с ритмом не всё в порядке')
