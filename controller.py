import view
import phonebook
import config



def start():
    path = config.Config.getPath()
    my_dict_view = view.PhoneBookView()
    my_dict_edit = phonebook.PhoneBookEdit(path)
    while True:
        user_choice = view.show_menu()
        match user_choice:
            case 1:
                my_dict_edit.open_directory()
            case 2:
                my_dict_edit.save_directory()
            case 3:
                my_dict_view.show_contacts(my_dict_edit.get_data())
            case 4:
                add_request = my_dict_view.add_request()
                my_dict_edit.add_directory(add_request)
            case 5:
                request = my_dict_view.search_request()
                if request != 0:
                    search_result = my_dict_edit.find_directory(request)
                    change_request = my_dict_view.change_request(search_result)
                    if change_request != 0:
                        list_for_choice = [i for i in search_result.items()]
                        my_dict_edit.change_directory(list_for_choice[change_request[0]], change_request[1])
            case 6:
                request = my_dict_view.search_request()
                if request != 0:
                    result = my_dict_edit.find_directory(request)
                    my_dict_view.show_contacts(result)
            case 7:
                request = my_dict_view.search_request()
                if request != 0:
                    search_result = my_dict_edit.find_directory(request)
                    delete_request = my_dict_view.delete_request(search_result)
                    if delete_request != 0:
                        result = my_dict_edit.delete_from_directory(delete_request)
            case 8:
                if my_dict_edit.close_directory():
                    del my_dict_edit
                    del my_dict_view
                    break
            case _:
                print("Ошибка ввода")
