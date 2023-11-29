answer = 'QUIT'

def user_selection():
    while True:
        print()
        userinput = input("Type QUIT to leave. ")
        print()
        if userinput == answer:
            print("That's correct. Have a nice day.")
            break
        else:
            print("Incorrect. Try again.")

def main():
    print("You will not be able to leave until you type QUIT.")
    user_selection()

if __name__ == "__main__":
    main()
