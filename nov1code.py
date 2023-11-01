def meal_test(answer):
    if answer == int(1):
        print()
        print("So you prefer some chicken? That's a good choice!")
        print()
        input('=============================== [ >> Press ENTER to exit. << ] ==============================')
    elif answer == int(2):
        print()
        print("So you prefer a burger? That's a good choice!")
        print()
        input('=============================== [ >> Press ENTER to exit. << ] ==============================')
    elif answer == int(3):
        print()
        print("So you prefer a slice of pizza? That's a good choice!")
        print()
        input('=============================== [ >> Press ENTER to exit. << ] ==============================')
    else:
        print()
        print("I don't believe that's an option.")
        print()
        input('=============================== [ >> Press ENTER to exit. << ] ==============================')

def main():
    print ('=============================================================================================')
    print()
    print("Which meal is your favorite?")
    print()
    print("(1) Chicken")
    print()
    print("(2) Burger")
    print()
    print("(3) Pizza")
    print()
    answer = int(input("Type the number > "))
    meal_test(answer)

if __name__ == "__main__":
    main()
