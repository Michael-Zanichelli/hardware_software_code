from os import system, name

def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def display_menu():
    print()
    print("What is your favorite video game console?")
    print()
    menu_dict = {
    1: ("- PlayStation 5"),
    2: ("- Xbox Series S"),
    3: ("- Nintendo Switch"),
    4: ("- Smartphone"),
    5: ("- PC"),
    6: ("- Choose Another")
    }
    for items, value in menu_dict.items():
        print(items,value)
    print()
    answer = int(input("Choose your favorite console > "))
    print()
    if answer == 1:
        print("So your favorite is the PlayStation 5?")
        print()
        input("Press ENTER to continue")
        clear_screen()
        return display_menu()
    elif answer == 2:
        print("So your favorite is the Xbox Series S?")
        print()
        input("Press ENTER to continue")
        clear_screen()
        return display_menu()
    elif answer == 3:
        print("So your favorite is the Nintendo Switch?")
        print()
        input("Press ENTER to continue")
        clear_screen()
        return display_menu()
    elif answer == 4:
            print("So your favorite is the Smartphone?")
            print()
            input("Press ENTER to continue")
            clear_screen()
            return display_menu()
    elif answer == 5:
            print("So your favorite is the PC?")
            print()
            input("Press ENTER to continue")
            clear_screen()
            return display_menu()
    elif answer == 6:
        menu_dict[6] = input("Type your favorite console > ")
        print()
        print("So your favorite is the",menu_dict[6],"?")
        print()
        input("Press ENTER to continue")
        clear_screen()
        return display_menu()
    else:
        print("That is not a valid option. Try again")
        print()
        input("Press ENTER to continue")
        clear_screen()
        return display_menu()

def main():
    display_menu()

if __name__ == "__main__":
    main()
