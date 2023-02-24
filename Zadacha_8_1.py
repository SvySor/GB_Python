# Создать телефонный справочник
# 1. Вывод на экран
# 2. Сохранять данные в текстовом файле
# 3. Поиск по имени и фамилии
# 4. Использование функций

# Д/З Дополнить телефонный справочник возможностью изменения данных
# Пользователь так же может ввести имя и фамилию и вы должны реализовать функционал для изменения и удаления данных


def menu():
    pass

def write_data():
    pass

def read_data():
    with open('fio.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
        file.close()
    return data

def change_data():
    pass

def screen(data):
    for elem in data:
        print(elem)

def main():
    data = read_data()
    screen(data)
    pass

if __name__ == '__main__':
    main()