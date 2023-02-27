# 1. Открыть файл
# 2. Сохранить файл
# 3. Показать контакты
# 4. Добавить контакт
# 5. Изменить контакт
# 6. Найти контакт
# 7. Удалить контакт
# 8. Выход

import classes


def show_menu():
    menu = {
        1: 'Открыть файл',
        2: 'Сохранить файл',
        3: 'Показать контакты',
        4: 'Добавить контакт',
        5: 'Изменить контакт',
        6: 'Найти контакт',
        7: 'Удалить контакт',
        8: 'Выход'}

    for item in menu.keys():
        print(f'{item} \t {menu[item]}')
    user_input = input("Введите номер действия: ")
    if user_input.isdigit():
        return int(user_input)
    else:
        return 0

path = "phone_book.txt"
my_dict_view = classes.PhoneBookView(path)
my_dict_edit = classes.PhoneBookEdit(my_dict_view)
while True:
    user_choise = show_menu()
    match user_choise:
        case 1:
            my_dict_view.open_directory(path)
            my_dict_edit = classes.PhoneBookEdit(my_dict_view)
            my_dict_edit.set_data(my_dict_view.get_data())
        case 2:
            my_dict_edit.save_directory()
        case 3:
            my_dict_view.show_directory()
        case 4:
            my_dict_edit.add_directory()
            my_dict_view.set_data(my_dict_edit.get_data())
        case 5:
            my_dict_edit.change_directory()
            my_dict_view.set_data(my_dict_edit.get_data())
        case 6:
            my_dict_view.find_directory()
        case 7:
            my_dict_edit.delete_directory()
            ddd = my_dict_edit.get_data()
            my_dict_view.set_data(my_dict_edit.get_data())
        case 8:
            if my_dict_view.close_directory():
                break
        case _:
            print("Ошибка ввода")
