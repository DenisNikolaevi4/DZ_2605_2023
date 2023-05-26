# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в
# текстовом файле
# Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# Использование функций. Ваша программа
# не должна быть линейной

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных
from pprint import pprint
def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Изменение данных\n"
          "7. Удаление данных\n"
          "Нажмите любую другую цифру, чтобы закончить работу")
    choice = int(input("Введите номер действия: "))
    return choice

def show_menu_2() -> int:
    print("\nЧто хотите изменить:\n"
          "1. Фамилию\n"
          "2. Телефон\n"
          "3. Назад\n")
    choice_2 = int(input("Введите номер действия: "))
    return choice_2

def show_menu_3() -> int:
    print("\nЧто хотите удалить:\n"
          "1. Фамилию\n"
          "2. Телефон\n"
          "3. Назад\n")
    choice_3 = int(input("Введите номер действия: "))
    return choice_3

def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

def write_txt(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:

        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')

def find_by_name(data: list, last_name: str) -> str:
    for el in data:
        if el.get("Фамилия") == last_name:
            return f"Телефон: {el.get('Телефон')} \nОписание: {el.get('Описание')}"
    return "Такой абонент отсутвует"

def find_by_name_delete(data: list, last_name: str) -> str:
    for el in data:
        if el.get("Фамилия") == last_name:
            el['Фамилия'] = ""
            return "Удалено"
    return "Такой абонент отсутвует"

def find_by_name_change(data: list, last_name: str) -> str:
    for el in data:
        if el.get("Фамилия") == last_name:
            el['Фамилия'] = input("Введите новую фамилию: ")
            return "Изменено"
    return "Такой абонент отсутвует"

def find_by_tel_delete(data: list, tel: str) -> str:
    for el in data:
        if el.get("Телефон") == tel:
            print(el['Телефон'])
            el['Телефон'] = ""
            return "Удалено"
    return "Такой телефон отсутвует"

def find_by_tel_change(data: list, tel: str) -> str:
    for el in data:
        if el.get("Телефон") == tel:
            el['Телефон'] = input("Введите новый телефон: ")
            return "Изменено"
    return "Такой телефон отсутвует"

def find_by_tel(data: list, tel: str) -> str:
    for el in data:
        if el.get("Телефон") == tel:
            return f"Фамилия: {el.get('Фамилия')} \nОписание: {el.get('Описание')}"
    return "Такой абонент отсутвует"

def add_user(data: list, user_data: str):
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    record = dict(zip(fields, user_data.split(',')))
    data.append(record)

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('D:\PYTHON\phon.txt')
    while 0 < choice < 8:
        if choice == 1:
            pprint(phone_book)
            work_with_phonebook()
            break
        elif choice == 2:
            print(find_by_name(phone_book,input("Введите фамилию: ")))
            work_with_phonebook()
            break
        elif choice == 3:
            print(find_by_tel(phone_book,input("Введите телефон: ")))
            work_with_phonebook()
            break
        elif choice == 4:
            add_user(phone_book, input())
            write_txt('D:\PYTHON\phon.txt', phone_book)
            work_with_phonebook()
            break
        elif choice == 5:
            name = input("Введите новое название файла: ")
            write_txt(f"D:\PYTHON\{name}.txt", phone_book)
            work_with_phonebook()
            break
        elif choice == 6:
            choice_2 = show_menu_2()
            if choice_2 == 1:
                print(find_by_name_change(phone_book,input("Введите фамилию которую хотите изменить: ")))
                write_txt('D:\PYTHON\phon.txt', phone_book)
                work_with_phonebook()
                break
            elif choice_2 == 2:
                print(find_by_tel_change(phone_book,input("Введите телефон который хотите изменить: ")))
                write_txt('D:\PYTHON\phon.txt', phone_book)
                work_with_phonebook()
                break
            elif choice_2 == 3:
                work_with_phonebook()
                break
        elif choice == 7:
            choice_3 = show_menu_3()
            if choice_3 == 1:
                print(find_by_name_delete(phone_book,input("Введите фамилию которую хотите удалить: ")))
                write_txt('D:\PYTHON\phon.txt', phone_book)
                work_with_phonebook()
                break
            elif choice_3 == 2:
                print(find_by_tel_delete(phone_book,input("Введите телефон который хотите удалить: ")))
                write_txt('D:\PYTHON\phon.txt', phone_book)
                work_with_phonebook()
                break
            elif choice_3 == 3:
                work_with_phonebook()
                break

work_with_phonebook()