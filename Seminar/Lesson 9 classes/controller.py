import view
import model
import text


def start():
    my_pb = model.PhoneBook()
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                my_pb.open()
                view.print_message(text.load_successful)
            case 2:
                my_pb.save()
                print(view.print_message(text.save_successful))
            case 3:
                pb = my_pb.load()
                view.print_contact(pb, text.load_error)
            case 4:
                contact = view.input_contact(text.new_contact, text.cancel_input, text.oops)
                name = my_pb.add(contact)
                view.print_message(text.new_contact_successful(name))
            case 5:
                find = view.find_contact(text.find)
                res = my_pb.search(find)
                view.print_message(text.found_contact(res))
            case 6:
                pb = my_pb.load()
                index = view.input_index(text.index_change_contact, pb, text.load_error)
                contact = view.input_contact(text.change_contact_m, text.cancel_input, text.oops)
                name = my_pb.change(index, contact)
                view.print_message(text.change_cont(name))
                view.print_message(text.reminder)
            case 7:
                pb = my_pb.load()
                index = view.input_index(text.index_delete_contact, pb, text.load_error)
                name = my_pb.delete(index)
                view.print_message(text.delete_contact(name))
            case 8:
                break