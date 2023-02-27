class PhoneBookView:
    def __init__(self, path):
        self._is_open = False
        self._path = path
        self.__data = dict()

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data
    def open_directory(self, path):
        try:
            with open(path, 'r', encoding='utf-8') as data:
                self.__data.clear()
                for current_row in data:
                    tmp = current_row.replace('\n', '').split(";")
                    self.__data[tmp[1]] = (tuple(tmp[0].split()), tmp[2])
            print("Справочник открыт.")
            self._is_open = True
        except:
            print("Файл справочника не найден.")

    def show_directory(self):
        if not self._is_open:
            print("Справочник не открыт.")
            return
        for key in self.__data.keys():
            value = self.__data[key]
            print('%30s %30s %30s %30s ' % (value[0][0], value[0][1], value[1], key))

    def find_directory(self):
        if not self._is_open:
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
                for key, value in self.__data.items():
                    if name == value[0]:
                        print('%30s %30s %30s %30s ' % (value[0][0], value[0][1], value[1], key))
            case 2:
                key = input("Введите номер телефона: ")
                value = self.__data[key]
                print('%30s %30s %30s %30s ' % (value[0][0], value[0][1], value[1], key))
            case 3:
                return

    def close_directory(self):
        if not self._is_open:
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
                self.__data.clear()
                return True
            case 2:
                return False


class PhoneBookEdit:
    def __init__(self, view):
        self._is_open = view._is_open
        self._path = view._path
        self.__data = dict()

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data
    def save_directory(self):
        with open(self._path, 'w', encoding='utf-8') as data:
            for key, value in self.__data.items():
                current_record = ";".join((' '.join(value[0]), key, value[1])) + '\n'
                data.write(current_record)
        print("Файл записан")

    def add_directory(self):
        if not self._is_open:
            print("Справочник не открыт.")
            return

        surname = input("Введите фамилию: ").title()
        name = input("Введите имя : ").title()
        comment = input("Введите комментарий: ")
        value = ((name, surname), comment)
        if value in self.__data.values():
            print("Такая запись уже существует!")
        else:
            key = input('Введи номер телефона: ')
            self.__data[key] = value
            print("Запись добавлена.")

    def change_directory(self):
        if not self._is_open:
            print("Справочник не открыт.")
            return
        key = input("Введите номер телефона: ")
        if key in self.__data:
            name = tuple(input("Введите имя и фамилию: ").title().split())
            comment = input("Введите комментарий: ")
            value = (name, comment)
            if value in self.__data.values():
                print("Такая запись уже существует!")
            else:
                self.__data[key] = value
                print("Запись изменена.")
        else:
            print("Такого номера нет.")

    def delete_directory(self):
        if not self._is_open:
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
                for key, value in self.__data.items():
                    if name == value[0]:
                        self.__data.pop(key)
            case 2:
                key = input("Введите номер телефона: ")
                if key in self.__data:
                    self.__data.pop(key)
            case 3:
                return
        print("Записи удалены")
