def print_meters_to_cm(meters):
    print("Print Meters")
    print(100 * meters)

def return_meters_to_cm(meters):
    return 100 * meters

def main():
    printcm = print_meters_to_cm(2)
    returncm = return_meters_to_cm(2)
    print()
    print("Return Meters")
    print(returncm)
    print()
    input('=============================== [ >> Press ENTER to exit. << ] ==============================')

if __name__ == "__main__":
        main()
