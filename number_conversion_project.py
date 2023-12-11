## number_conversion_project.py
## https://github.com/Michael-Zanichelli/hardware_software_code

## Hello, my name is Michael Zanichelli. This piece of code is for my Hardware and Software Number
## Conversion Project. It is meant to translate binary numbers into decimal numbers and vice versa,
## without using the built-in Python functions for those equations (int, bin) I have made the code
## visually appealing and user friendly, and due to that the code is very bulky. However, the actual
## equations for the translations are spaced out from the rest of the code.

## Limitations: This code is unable to perform any other conversions, such as octal and hexadecimal.

## Creation Date: Wednesday, November 8th, 2023
## Modified Date: Monday, November 29th, 2023




## This is the code that I used in order to clear the screen after
## a user input, reducing clutter and preventing the user from
## becoming too overwhelmed by the code due to its sheer scale.

from os import system, name

def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def binary_to_decimal_conversion(explain_binary_to_decimal):

## This is the equation that I used in translating binary numbers into
## decimal numbers without using the built-in Python functions (int, bin).
## I only used the int function in situations where the code needed me
## to differentiate between integers and strings.


    binary = int(input(" > Enter a binary number: "))
    bits = list(str(binary))
    decimal = 0
    counter = 0
    for i in reversed(bits):
        decimal += 2 ** counter * int(i)
        counter += 1
    print()
    print(" > The decimal number of",binary,"is",decimal,)


    print()
    input('> Press ENTER to continue: ')
    clear_screen()
    print("Would you like to do another conversion?")
    print()
    print("(1) Yes")
    print("(2) No")
    print()
    return_to_start1 = int(input("Type 1 or 2 > "))
    print()
    if return_to_start1 == 1:
        print("Okay, lets go back to the start!")
        print()
        input(' > Press ENTER to continue: ')
        clear_screen()
        return main()
    elif return_to_start1 == 2:
        print("Understood. Have a nice day!")
        print()
        input('> Press ENTER to exit: ')
        clear_screen()
    else:
        print("That is not a valid option. We'll return back to the start.")
        print()
        input(' > Press ENTER to restart:')
        clear_screen()
        return main()


def decimal_to_binary_conversion(explain_decimal_to_binary):

## This is the equation that I used in translating decimal numbers into
## binary numbers without using the built-in Python functions (int, bin).
## I only used the int function in situations where the code needed me
## to differentiate between integers and strings.


    userinput = decimal = int(input(" > Enter a decimal number: "))
    a = 0
    b = 1
    while b < userinput:
       a = a+1
       b = 2**a
    binary = [0] * (a+1)
    for b in range(a, -1, -1):
       if (userinput - (2**b)) < 0:
          binary[b] = 0
       else:
          binary[b] = 1
          userinput = (userinput - (2**b))
    c = binary[::-1]
    answer = ''.join(map(str, c))
    print()
    print(" > The binary number of",decimal,"is",answer,)


    print()
    input(' > Press ENTER to continue: ')
    clear_screen()
    print("Would you like to do another conversion?")
    print()
    print("(1) Yes")
    print("(2) No")
    print()
    return_to_start2 = int(input("Type 1 or 2 > "))
    print()
    if return_to_start2 == 1:
        print("Okay, lets go back to the start!")
        print()
        input(' > Press ENTER to continue: ')
        clear_screen()
        return main()
    elif return_to_start2 == 2:
        print("Understood. Have a nice day!")
        print()
        input(' > Press ENTER to exit: ')
    else:
        print("That is not a valid option. We'll return back to the start.")
        print()
        input('> Press ENTER to restart: ')
        clear_screen()
        return main()


def binary_to_decimal(answer):

## I added this section as a way to explain what this code is doing
## for people who do not understand the difference between binary and
## decimal numbers in order to make this code user friendly.

    print(" > We will now begin converting binary to decimal.")
    print()
    input(' > Press ENTER to continue: ')
    clear_screen()
    print(" > Would you like an explanation as to what that means?")
    print()
    print(" > (1) Yes")
    print(" > (2) No")
    print()
    explain_binary_to_decimal = int(input(" > Type 1 or 2: "))
    print()
    if explain_binary_to_decimal == 1:
        print(" > Yes? In that case, let me explain.")
        print()
        input(' > Press ENTER to continue: ')
        clear_screen()
        print(" > A binary number is made of 0s and 1s and is the language computers speak.")
        print(" > We will be converting a binary number into a decimal number, which is what we use.")
        clear_screen()
        input(' > Press ENTER to continue: ')
        print()
        print(" > Now let us begin.")
        print()
        input(' > Press ENTER to continue: ')
        clear_screen()
        binary_to_decimal_conversion(explain_binary_to_decimal)
    elif explain_binary_to_decimal == 2:
        print(" > No? Then let us begin.")
        print()
        input(' > Press ENTER to continue: ')
        clear_screen()
        binary_to_decimal_conversion(explain_binary_to_decimal)
    else:
        print(" > That is not a valid option. Try again.")
        print()
        input(' > Press ENTER to restart: ')
        clear_screen()
        return binary_to_decimal(answer)


def decimal_to_binary(answer):

## I added this section as a way to explain what this code is doing
## for people who do not understand the difference between binary and
## decimal numbers in order to make this code user friendly.

    print(" > We will now begin converting decimal to binary.")
    print()
    input('> Press ENTER to continue: ')
    clear_screen()
    print(" > Would you like an explanation as to what that means?")
    print()
    print(" > (1) Yes")
    print(" > (2) No")
    print()
    explain_decimal_to_binary = int(input(" > Type 1 or 2: "))
    print()
    if explain_decimal_to_binary == 1:
        print(" > Yes? In that case, let me explain.")
        print()
        input(' > Press ENTER to continue: ')
        clear_screen()
        print(" > A binary number is made of 0s and 1s and is the language computers speak.")
        print(" > We will be converting a decimal number, which is what we use, into a binary number.")
        print()
        input(' > Press ENTER to continue: ')
        clear_screen()
        print(" > Now let us begin.")
        print()
        input(' > Press ENTER to continue: ')
        clear_screen()
        decimal_to_binary_conversion(explain_decimal_to_binary)
    elif explain_decimal_to_binary == 2:
        print(" > No? Then let us begin.")
        print()
        input(' > Press ENTER to continue: ')
        clear_screen()
        decimal_to_binary_conversion(explain_decimal_to_binary)
    else:
        print(" > That is not a valid option. Try again.")
        print()
        input(' > Press ENTER to restart: ')
        clear_screen()
        return decimal_to_binary(answer)

def main():

## This section is designed to identify whether or not the user is
## trying to translate binary to decimal or vice versa, and will
## direct them to the location of their choice.

    print()
    print(" > This is an automated code that lets you convert binary to decimal and vice versa.")
    print()
    input(' > Press ENTER to continue: ')
    clear_screen()
    print()
    print(" > Choose which conversion you want:")
    print()
    print(" > (1) Binary to Decimal")
    print(" > (2) Decimal to Binary.")
    print()
    answer = int(input(" > Type 1 or 2: "))
    print()
    if answer == 1:
        print(" > You have chosen Binary to Decimal.")
        binary_to_decimal(answer)
    elif answer == 2:
        print(" > You have chosen Decimal to Binary.")
        decimal_to_binary(answer)
    else:
        print(" > That is not a valid option. Try again.")
        print()
        input('> Press ENTER to restart: ')
        clear_screen()
        return main()

if __name__ == "__main__":
    main()
