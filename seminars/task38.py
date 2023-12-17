"""
Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать
функционал для изменения и удаления данных

"""


def display_menu():
    flag = True
    while flag:
        print("Choose action >> ")
        print("""
        1. Show all contacts
        2. Add new contact
        3. Edit contact
        4. Delete contact
        5. Find by name
        6. Find by number
        7. Exit
            """)

        choice = input("Your choice is >> ")

        if choice == "1":
            print("Contacts list")
            view_contacts()

        elif choice == "2":
            add_contact()
            print('Here is your phone book after saving >> ')
            view_contacts()

        elif choice == '3':
            add_contact(edit_contact())
            print('Here is your phone book after editing >> ')
            view_contacts()

        elif choice == '4':
            delete_contact()
            print('Here is your phone book after deleting >> ')
            view_contacts()

        elif choice == '5':
            find_by_name()

        elif choice == '6':
            find_by_number()

        elif choice == '7':
            flag = False

        else:
            print('No such point, choose another point')


def view_contacts():
    with open("phonebook.txt", "r+", encoding='utf-8') as file:
        data = file.read()
        print(data)


def add_contact(data=None):
    if data is not None:
        with open("phonebook.txt", "w+", encoding='utf-8') as file:
            file.writelines(data)
    else:
        with open("phonebook.txt", "a+", encoding='utf-8') as file:
            name = input('input name >> ')
            phone = input('input phone number >> ')
            data = f'{name}\t{phone}\n'
            file.write(data)


def edit_contact():
    name = input("Write name for editing >> ")
    with open("phonebook.txt", "r+", encoding='utf-8') as file:
        data = file.readlines()
        found = False
        for index, line in enumerate(data):
            if name.lower() in line.lower():
                new_name = input("Input new name >> ")
                new_number = input("Input new number >> ")
                new_data = f'{new_name}\t{new_number}\n'
                data[index] = new_data
                add_contact(data)


def delete_contact():
    name = input("Write name for searching >> ")
    with open("phonebook.txt", "a+", encoding='utf-8') as file:
        file.seek(0)
        data = file.readlines()
        found = False
        for line in data:
            if name.lower() in line.lower():
                data.remove(line)
                found = True
    if found:
        add_contact(data)
        print('the contact was deleted')
    else:
        print("there is no such a contact")


def find_by_name():
    name = input("Write name for searching >> ")
    with open('phonebook.txt', 'r+', encoding='utf-8') as file:
        data = file.readlines()
        for line in data:
            if name.lower() in line.lower():
                print(f'Found\n{line}')
        print('Search end')


def find_by_number():
    number = input("Write number or part of for searching >> ")
    with open('phonebook.txt', 'r+', encoding='utf-8') as file:
        data = file.readlines()
        for line in data:
            if number.lower() in line.lower():
                print(f'Found\n{line}')
        print('Search end')


def main():
    display_menu()


if __name__ == "__main__":
    main()
