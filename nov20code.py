Var = 42

def add(num3):
    global Var
    number = num3 + Var
    Var = number
    print("The sum of the numbers is >",number)
    print("The updated global variable is >",Var)

def main():
    num1 = int(input("Enter the first number > "))
    num2 = int(input("Enter the second number > "))
    num3 = (num1 + num2)
    add(num3)

if __name__ == "__main__":
    main()
