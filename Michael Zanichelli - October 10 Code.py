def conversation():
    print('=============================================================================================')
    print()
    print("Welcome to my conversation.")
    input()
    print("Do you like coding?")
    answer = input("Answer > ")
    print()
    if answer.lower() == "yes":
        print("That's good.")
    elif answer.lower() == "no":
        print("That's too bad.")
    else:
        print("I don't understand.")
    input()
    print("Thanks for talking with me!")
    input()
    input ('=============================== [ >> Press ENTER to exit. << ] ==============================')

def main():
    conversation()

if __name__ == "__main__":
    main()
