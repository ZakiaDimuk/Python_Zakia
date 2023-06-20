from os import path

file_base = "base.txt"
last_id = 0
all_data = []

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    global last_id, all_data

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])
            return all_data
    return []


def show_all():
    if all_data:
        print(*all_data, sep="\n")
    else:
        print("Empty data")


def add_new_contact():
    global last_id
    array = ["surname", "name", "patronymic", "phone_number"]
    string = ""
    for i in array:
        string += input(f"Enter {i} ") + " "
    last_id += 1

    with open(file_base, "a", encoding="utf-8") as f:
        f.write(f"{last_id} {string}\n")

def change_data():
    print('\nПП | ФИО | Телефон')

    with open(file_base, 'r', encoding='utf-8') as data:
        tel_book = data.read()
        print(tel_book)
    print('')
    
    index_delete_data = int(input('Введите номер строки для редактирования: ')) - 1
    tel_book_lines = tel_book.split('\n')
    edit_tel_book_lines = tel_book_lines[index_delete_data]
    elements = edit_tel_book_lines.split(' | ')

    surname = input('Введите Фамилию: ')
    name = input('Введите Имя: ')
    patronymic = input('Введите Отчество: ')
    phone = input('Введите номер телефона: ')
    
    num = elements[0]
    if len(surname) == 0:
        surname = elements[1]
    if len(name) == 0:
        name = elements[2]
    if len(patronymic) == 0:
        patronymic = elements[3]
    if len(phone) == 0:
        phone = elements[4]

    edited_line = f'{num} | {surname} | {name} | {patronymic} | {phone}'
    tel_book_lines[index_delete_data] = edited_line
    print(f'Запись — {edit_tel_book_lines}, изменена на — {edited_line}\n')

    with open(file_base, 'w', encoding='utf-8') as f:
        f.write('\n'.join(tel_book_lines))

def delete_data():
    print('\nПП | ФИО | Телефон')

    with open(file_base, 'r', encoding='utf-8') as data:
        tel_book = data.read()
    print(tel_book)
    print('')
    
    index_delete_data = int(input('Введите номер строки для удаления: ')) - 1
    tel_book_lines = tel_book.split('\n')
    del_tel_book_lines = tel_book_lines[index_delete_data]
    tel_book_lines.pop(index_delete_data)
    print(f'Удалена запись: {del_tel_book_lines}\n')
    with open(file_base, 'w', encoding='utf-8') as data:
        data.write('\n'.join(tel_book_lines))

def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Change\n"
                       "5. Delete\n"
                       "6. Exp/Imp\n"
                       "7. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                pass
            case "4":
                change_data()
            case "5":
                delete_data()
            case "6":
                pass
            case _:
                print("Try again!\n")


main_menu()