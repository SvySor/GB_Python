# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


string = 'Названия с включенными символами абв абв центр лабораторных технологий абвгдейка гворящая зооазбука абв академия белой воды абв телеканал абв-тв интернет провайде абв-интернет в тюмени'
print(string)
words = string.split(' ')
fragment = 'абв'
new_words = []
for word in words:
    if fragment not in word:
        new_words.append(word)
print()
print(' '.join(new_words))
print()
