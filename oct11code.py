def choose_a_door():
    prize = 4
    print('=============================================================================================')
    msg = "Choose the correct door: 1, 2 or 3 > "
    print()
    print("Do you want to win a prize?")
    print()
    door = int(input(msg))

    while door < 1 or door > 3:
        print("Invalid Door!")
        door = int(input(msg))
    if door == 1:
        prize = 2 + 9 // 10 * 100
    elif door == 2:
        prize += 6
    elif door == 3:
        for i in range(door):
            prize += i
    print()
    print("You won " + str(prize) + " tickets!")
    print()
    input ('=============================== [ >> Press ENTER to exit. << ] ==============================')

def main():
    choose_a_door()

if __name__ == "__main__":
    main()
