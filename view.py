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


class PhoneBookView:
    # def __init__(self):

    def show_contacts(self, data):
        if len(data) == 0:
            print("Нет записей")
        else:
            for i, key in enumerate(data.keys(), 1):
                value = data[key]
                print('%3d %30s %30s %30s %30s ' % (i, value[0][0], value[0][1], value[1], key))

    def search_request(self):
        menu = {
            1: 'По имени',
            2: 'По номеру',
            3: 'Отмена'}
        print("Искать \n")
        for item in menu.keys():
            print(f'{item} \t {menu[item]}')
        user_input = input("Введите номер действия: ")
        if user_input.isdigit():
            user_input = int(user_input)
            match user_input:
                case 1:
                    name = input("Введите строку поиска: ")
                    return 1, name
                case 2:
                    key = input("Введите номер телефона: ")
                    return 2, key
                case 3:
                    return 3, ''
        else:
            print("Ошибка ввода")
            return 0

    def add_request(self):

        surname = input("Введите фамилию: ").title()
        name = input("Введите имя : ").title()
        comment = input("Введите комментарий: ")
        key = input("Введите номер телефона: ")
        return key, ((name, surname), comment)

    def change_request(self, search_result):
        self.show_contacts(search_result)
        list_for_choice = [i for i in search_result.items()]
        user_input = input("Выберите контакт: ")
        if user_input.isdigit():
            user_input = int(user_input)
            contact = list_for_choice[user_input - 1]
            key = input("Введите номер телефона: ")
            name = tuple(input("Введите имя и фамилию: ").title().split())
            comment = input("Введите комментарий: ")
            return user_input - 1, (key if key else contact[0],
                                    (name if name else contact[1][0],
                                     comment if comment else contact[1][1]))
        else:
            print("Ошибка ввода")
            return 0

    def delete_request(self, search_result):
        self.show_contacts(search_result)
        list_for_choice = [i for i in search_result.items()]
        user_input = input("Выберите контакт: ")
        if user_input.isdigit():
            user_input = int(user_input)
            return list_for_choice[user_input - 1]
        else:
            return 0
