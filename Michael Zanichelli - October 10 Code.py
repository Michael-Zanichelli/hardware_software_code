def conversation():
    print('=============================================================================================')
    print()
    print("Welcome to my conversation.")
    input()
    print("Do you like coding?")
    answer = input("Answer > ")
    print()
    if answer == "yes":
        print("That's good.")
    else:
        print("That's too bad!")
    input()
    print("Thanks for talking with me!")
    input()
    input ('=============================== [ >> Press ENTER to exit. << ] ==============================')

def main():
    conversation()

if __name__ == "__main__":
    main()
