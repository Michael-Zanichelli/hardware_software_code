def max(num1, num2):
    if num1 >= num2:
        print("1:",num1)
        print()
        return num1
    print("2:",num2)
    print()
    return num2

def main():
    larger = max(1,5)
    print("Larger Number:")
    print(larger)
    print()
    input ('=============================== [ >> Press ENTER to exit. << ] ==============================')

if __name__ == "__main__":
    main()
