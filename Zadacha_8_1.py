# Создать телефонный справочник
# 1. Вывод на экран
# 2. Сохранять данные в текстовом файле
# 3. Поиск по имени и фамилии
# 4. Использование функций

# Д/З Дополнить телефонный справочник возможностью изменения данных
# Пользователь так же может ввести имя и фамилию и вы должны реализовать функционал для изменения и удаления данных


def menu():                                 # Модуль меню
    print("\t Выберите операцию, которую хотите осуществить:")
    print()
    print("1 - Просмотреть все контакты")
    print("2 - Поиск контакта")
    print("3 - Изменить контракт")
    print("4 - Добавить контакт")
    print("5 - Удалить контакт")
    print("0 - Покинуть программу")
    print()
    isCorrect = False
    while not isCorrect:
        try:
            while not isCorrect:
                option = int(input('Ваш выбор: '))
                if option < 0 or option > 5:
                    print("Число должно быть от 0 до 5")
                else:
                    isCorrect = True
        except ValueError:
            print("Это не число!")
            option = 0
    return option

def selection():            # Подпрограмма запуска модулей
    isFinish = False
    while not isFinish:
        select = menu()
        print("Ваш выбор - ", select)
        if select == 1:
            print("Запускаю модуль просмотра данных")
            screen()
        elif select == 2:
            print("Запускаю модуль поиска контакта")
        elif select == 3:
            print("Запускаю модуль изменения контакта")
        elif select == 4:
            print("Запускаю модуль добавления контакта")
        elif select == 5:
            print("Запускаю модуль удаления контакта")
        else:
            isFinish = True
    print("Работа программы закончена. Спасибо")

def read_data():                            # Модуль считывания данных из файла в список
    with open('fio.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
        data = list(map(lambda record: record[:-1].split(';'), data))
        file.close()
    return data

def screen():
    data = read_data()
    screen_result(data)

def screen_result(data):
    header_line = ('ID', 'Фамилия', 'Имя', 'Отчество', 'Телефон')
    print('___________________________________________________________________________________')
    print()
    print('\t\t'.join(map(str, header_line)))
    print('___________________________________________________________________________________')
    print()
    for i in range(len(data)):
        print('\t\t'.join(map(str, data[i])))

def search_data():
    data = read_data()
    print('Если поиск будет по Фамилии - наберите 1, если поиск будет по Имени - наберите 2')
    isCorrect = False
    while not isCorrect:
        try:
            while not isCorrect:
                option = int(input('Ваш выбор: '))
                if option < 1 or option > 2:
                    print("Число должно быть 1 или 2")
                else:
                    isCorrect = True
        except ValueError:
            print("Это не число!")
            option = 0
    search_text = input('Введите имя или фамилию для поиска: ')
    if option == 1:
        filtered_data = list(filter(lambda record: (record[1] == search_text), data))
    else:
        filtered_data = list(filter(lambda record: (record[2] == search_text), data))
    screen_result(filtered_data)

def change_data():
    data = read_data()
    screen()
    record_ID = input('Введите номер записи для изменения: ')
    change_record_index = data[0].index(record_ID)
    print(data[change_record_index])
    data[change_record_index][1] = input('Введите изменения в фамилии: ')
    data[change_record_index][2] = input('Введите изменения в имени: ')
    data[change_record_index][3] = input('Введите изменения в отчестве: ')
    data[change_record_index][4] = input('Введите изменения в номере телефона: ')
    print('Изменённая запись:')
    print(data[change_record_index])
    write_data(data)
    
def write_data(data):                            # Модуль записи данных в файл
    with open('fio.txt', 'w', encoding='utf-8') as file:
        for i in range(len(data)):
            file.writelines(';'.join(data[i]))
            file.writelines('\n')
        file.close()

def main():
    print('\n' * 100)
    print("\t\t ТЕЛЕФОННЫЙ СПРАВОЧНИК")
    print()
    # selection()
    # screen()
    # search_data()
    # change_data()

if __name__ == '__main__':
    main()