def select(f, col):
        print(f)
        print(col)
        return [f(x) for x in col]

def where(f, col):
    print(f)
    print(col)
    return [x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23, 38]
print(data)
res = select(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = select(lambda x: (x, x**2), res)
print(res)



# Функция map(). Добавление 10 ко всем членам списка data
res1 = list(map(lambda x: x + 10, data))
print(res1)

# Функция map(). Преобразование типов из списка с цифрами в строку и обратно.
data_str = [str(i) for i in data] # Преобразование каждого члена в срочный тип и интеджер
data_str = ' '.join(data_str) # Объединение писка в строку
print(data_str)
res2 = list(map(int, data_str.split())) # Обратное преобразование.  Разделение строки и применение функции int к строчному типу
print(res2)

# Функция filter() Фильтрация чётных значений
res3 = list(filter(lambda x: x % 2 == 0, data))
print(res3)

# Функция zip() Создаёт кортежи из списков (Пробегает по минимальному набору)

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [11, 12, 13, 14, 15]
salary = [120, 170, 180]
res4 = list(zip(users, ids, salary))
print(res4)

# Функция enumerate() Применяется к итерируемому объекту и создаёт список с кортежами из индекса и элемента
cities = ['Москва', 'Смоленск', 'Рим', 'Лондон', 'Киев']
print(list(enumerate(cities)))


# Работа с файлами
# a - добавление данных (не удаляются старые данные)
# r - чтение данных
# w - перезапись данных (удаляются старые)
# w+ - открыть файл для записи и читать из него. Если файла нет, то он будет создан
# r+ - открыть файл для чтения и дописывать него. Если файла нет, то будет ошибка

data = open('city_list.txt', 'a')
data.writelines(cities)
data.close()

