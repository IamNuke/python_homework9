class PhoneBookView:
    def __init__(self, path):
        self.is_open = False
        self.path = path
        self.data = dict()

    def open_directory(self, path):
        try:
            with open(path, 'r', encoding='utf-8') as data:
                self.data.clear()
                for current_row in data:
                    tmp = current_row.replace('\n', '').split(";")
                    self.data[tmp[1]] = (tuple(tmp[0].split()), tmp[2])
            print("Справочник открыт.")
            self.is_open = True
        except:
            print("Файл справочника не найден.")

    def show_directory(self):
        if not self.is_open:
            print("Справочник не открыт.")
            return
        for key in self.data.keys():
            value = self.data[key]
            print('%30s %30s %30s %30s ' % (value[0][0], value[0][1], value[1], key))

    def find_directory(self):
        if not self.is_open:
            print("Справочник не открыт.")
            return

        menu = {
            1: 'По имени',
            2: 'По номеру',
            3: 'Отмена'}

        for item in menu.keys():
            print(f'{item} \t {menu[item]}')
        find_user_choise = int(input("Введите номер действия: "))
        match find_user_choise:
            case 1:
                name = tuple(input("Введите имя и фамилию: ").split())
                for key, value in self.data.items():
                    if name == value[0]:
                        print('%30s %30s %30s %30s ' % (value[0][0], value[0][1], value[1], key))
            case 2:
                key = input("Введите номер телефона: ")
                value = self.data[key]
                print('%30s %30s %30s %30s ' % (value[0][0], value[0][1], value[1], key))
            case 3:
                return

    def close_directory(self):
        if not self.is_open:
            print("Справочник не открыт.")
            return

        menu = {
            1: 'Закрыть',
            2: 'Отмена'}

        for item in menu.keys():
            print(f'{item} \t {menu[item]}')
        find_user_choise = int(input("Все не сохраненные изменения будут потеряны. Закрыть?: "))
        match find_user_choise:
            case 1:
                self.data.clear()
                return True
            case 2:
                return False


class PhoneBookEdit:
    def __init__(self, view):
        self.is_open = view.is_open
        self.path = view.path
        self.data = view.data

    def save_directory(self):
        with open(self.path, 'w', encoding='utf-8') as data:
            for key, value in self.data.items():
                current_record = ";".join((' '.join(value[0]), key, value[1])) + '\n'
                data.write(current_record)
        print("Файл записан")

    def add_directory(self):
        if not self.is_open:
            print("Справочник не открыт.")
            return

        surname = input("Введите фамилию: ").title()
        name = input("Введите имя : ").title()
        comment = input("Введите комментарий: ")
        value = ((name, surname), comment)
        if value in self.data.values():
            print("Такая запись уже существует!")
        else:
            key = input('Введи номер телефона: ')
            self.data[key] = value
            print("Запись добавлена.")

    def change_directory(self):
        if not self.is_open:
            print("Справочник не открыт.")
            return
        key = input("Введите номер телефона: ")
        if key in self.data:
            name = tuple(input("Введите имя и фамилию: ").title().split())
            comment = input("Введите комментарий: ")
            value = (name, comment)
            if value in self.data.values():
                print("Такая запись уже существует!")
            else:
                self.data[key] = value
                print("Запись изменена.")
        else:
            print("Такого номера нет.")

    def delete_directory(self):
        if not self.is_open:
            print("Справочник не открыт.")
            return

        menu = {
            1: 'По имени',
            2: 'По номеру',
            3: 'Отмена'}

        for item in menu.keys():
            print(f'{item} \t {menu[item]}')
        find_user_choise = int(input("Введите номер действия: "))
        match find_user_choise:
            case 1:
                name = tuple(input("Введите имя и фамилию: ").split())
                for key, value in self.data.items():
                    if name == value[0]:
                        self.data.pop(key)
            case 2:
                key = input("Введите номер телефона: ")
                if key in self.data:
                    self.data.pop(key)
            case 3:
                return
        print("Записи удалены")
