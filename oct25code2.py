def stack_me_high(num1):
    if num1 == 0 | 10:
        return num1
    print("Current count:",num1)
    num1 += 1
    stack_me_high(num1)

def main():
    num1 = stack_me_high(1)
    print("Current count:",num1)

if __name__ == "__main__":
    main()

# The nature of this code prevents me from putting an input() command to
# prevent certain devices from closing immediately upon completion of the
# task. I apologize if you are unable to view the code due to this.
