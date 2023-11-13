def check_number():
    number = input("Enter a whole number: ")
    try:
        return(True, int(number))
    except:
        print()
        print("That is not a valid input.")
        return(False, None)

def main():
    good_selection = False
    while not good_selection:
        good_selection, number = check_number()
    print()
    print("Good job!", number ,"is a whole number.")
    input()

if __name__ == "__main__":
    main()
