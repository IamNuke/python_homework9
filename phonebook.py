
from abc import ABC, abstractmethod

class DirectoryEdit:
    @abstractmethod
    def set_data(self, data):
        pass    
    @abstractmethod
    def get_data(self):
        pass
    @abstractmethod
    def open_directory(self):
        pass
    @abstractmethod
    def save_directory(self):
        pass
    @abstractmethod
    def add_directory(self, add_request):
        pass
    @abstractmethod
    def change_directory(self, current_data, new_data):
        pass
    @abstractmethod
    def delete_from_directory(self, delete_request):
        pass
    @abstractmethod
    def find_directory(self, request):
        pass
    @abstractmethod
    def close_directory(self):
        pass



class PhoneBookEdit(DirectoryEdit):
    def __init__(self, path):
        self._is_open = False
        self._path = path
        self.__data = dict()

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data

    def open_directory(self):
        try:
            with open(self._path, 'r', encoding='utf-8') as data:
                self.__data.clear()
                for current_row in data:
                    tmp = current_row.replace('\n', '').split(";")
                    self.__data[tmp[1]] = (tuple(tmp[0].split()), tmp[2])
            print("Справочник открыт.")
            self._is_open = True
        except:
            print("Ошибка чтения файла.")

    def save_directory(self):
        with open(self._path, 'w', encoding='utf-8') as data:
            for key, value in self.__data.items():
                current_record = ";".join((' '.join(value[0]), key, value[1])) + '\n'
                data.write(current_record)
        print("Файл записан")

    def add_directory(self, add_request):
        if not self._is_open:
            print("Справочник не открыт.")
            return

        key = add_request[0]
        value = add_request[1]
        if add_request in self.__data.values():
            print("Такая запись уже существует!")
        else:
            self.__data[key] = value
            print("Запись добавлена.")

    def change_directory(self, current_data, new_data):
        if not self._is_open:
            print("Справочник не открыт.")
            return
        self.__data.pop(current_data[0])
        self.__data[new_data[0]] = new_data[1]

    def delete_from_directory(self, delete_request):
        if not self._is_open:
            print("Справочник не открыт.")
            return

        self.__data.pop(delete_request[0])
        print("Запись удалена")

    def find_directory(self, request):
        result = dict()
        if not self._is_open:
            print("Справочник не открыт.")
            return result

        match request[0]:
            case 1:
                name = request[1]
                for key, value in self.__data.items():
                    if name in value[0]:
                        result[key] = value
                return result
            case 2:
                search_key = request[1]
                for key, value in self.__data.items():
                    if search_key in key:
                        result[key] = value
                return result
            case 3:
                return result

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
