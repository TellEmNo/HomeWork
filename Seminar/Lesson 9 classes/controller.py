import view
import model
import text


def start():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_phonebook()
                view.print_message(text.load_successful)
            case 2:
                model.save_phonebook()
                print(view.print_message(text.save_successful))
            case 3:
                pb = model.get_pb()
                view.print_contact(pb, text.load_error)
            case 4:
                contact = view.input_contact(text.new_contact, text.cancel_input, text.oops)
                name = model.add_contact(contact)
                view.print_message(text.new_contact_successful(name))
            case 5:
                find = view.find_contact(text.find)
                res = model.find_contact(find)
                view.print_message(text.found_contact(res))
            case 6:
                pb = model.get_pb()
                index = view.input_index(text.index_change_contact, pb, text.load_error)
                contact = view.input_contact(text.change_contact_m, text.cancel_input, text.oops)
                name = model.change_contact(index, contact)
                view.print_message(text.change_cont(name))
                view.print_message(text.reminder)
            case 7:
                pb = model.get_pb()
                index = view.input_index(text.index_delete_contact, pb, text.load_error)
                name = model.delete_contact(index)
                view.print_message(text.delete_contact(name))
            case 8:
                break