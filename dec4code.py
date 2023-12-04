from os import system, name

def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def display_menu():
    print("Console Generations")
    print()
    menu = {
    1: ("- 1st Gen (1970 - 1980)"),
    2: ("- 2nd Gen (1976 - 1992)"),
    3: ("- 3rd Gen (1983 - 2003)"),
    4: ("- 4th Gen (1987 - 2004)"),
    5: ("- 5th Gen (1993 - 2006)"),
    6: ("- 6th Gen (1998 - 2013)"),
    7: ("- 7th Gen (2005 - 2017)"),
    8: ("- 8th Gen (2012 - Now)"),
    9: ("- 9th Gen (2020 - Now)")
    }
    for items, value in menu.items():
        print(items,value)
    print()
    gen = int(input("Enter a value: "))
    clear_screen()

    if gen == 1:
        print("First Generation (1970 - 1980)")
        print()
        print("[Console Name] [Years]")
        print()
        gen1 = {
        1: ("- Magnavox Odyssey           (1972 - 1975)"),
        2: ("- Ping-O-Tronic              (1974 - 1974)"),
        3: ("- Home Pong Series           (1975 - 1975)"),
        4: ("- TV Tennis Electrotennis    (1975 - 1975)"),
        5: ("- Coleco Telstar             (1976 - 1796)"),
        6: ("- Color TV-Game              (1977 - 1980)")
        }
        for items, value in gen1.items():
            print(items,value)
        print()
        input("Press ENTER to continue")
        clear_screen()
        return display_menu()

    elif gen == 2:
        print("Second Generation (1976 - 1992)")
        print()
        print("[Console Name] [Years]")
        print()
        gen2 = {
        1: ("- Fairchild Channel F       (1976 - 1983)"),
        2: ("- Atari 2600                (1977 - 1992)"),
        3: ("- Magnavox Odyssey 2        (1978 - 1984)"),
        4: ("- Intellivision             (1980 - 1990)"),
        5: ("- ColecoVision              (1982 - 1985)"),
        6: ("- Atari 5200                (1982 - 1984)")
        }
        for items, value in gen2.items():
            print(items,value)
        print()
        input("Press ENTER to continue")
        clear_screen()
        return display_menu()

    elif gen == 3:
        print("Third Generation (1983 - 2003)")
        print()
        print("[Console Name] [Years]")
        print()
        gen3 = {
        1: ("- Famicom / NES               (1983 - 2003)"),
        2: ("- Mark III / Master System    (1985 - 1996)"),
        3: ("- Atari 7800                  (1986 - 1992)"),
        4: ("- Atari XEGS                  (1987 - 1992)")
        }
        for items, value in gen3.items():
            print(items,value)
        print()
        input("Press ENTER to continue")
        clear_screen()
        return display_menu()

    elif gen == 4:
        print("Fourth Generation (1987 - 2004)")
        print()
        print("[Console Name] [Years]")
        print()
        gen4 = {
        1: ("- PC Engine / TurboGrafx-16    (1987 - 1994)"),
        2: ("- Mega Drive / Genesis         (1988 - 1997)"),
        3: ("- Neo Geo                      (1990 - 1997)"),
        4: ("- Super Famicom / Super NES    (1990 - 2003)"),
        5: ("- Sega CD / Mega CD            (1991 - 1996)"),
        6: ("- CD-i                         (1991 - 1998)"),
        7: ("- Neo Geo CD                   (1994 - 1997)")
        }
        for items, value in gen4.items():
            print(items,value)
        print()
        print("[Handheld Name] [Years]")
        print()
        gen4h = {
        1: ("- Game Boy                     (1989 - 2003)"),
        2: ("- Atari Lynx                   (1989 - 1995)"),
        3: ("- Game Gear                    (1990 - 1997)"),
        4: ("- TurboExpress                 (1990 - 1994)")
        }
        for items, value in gen4h.items():
            print(items,value)
        print()
        input("Press ENTER to continue")
        clear_screen()
        return display_menu()

    elif gen == 5:
        print("Fifth Generation (1993 - 2006)")
        print()
        print("[Console Name] [Years]")
        print()
        gen5 = {
        1: ("- FM Towns Marty       (1993 - 1995)"),
        2: ("- Amiga CD32           (1993 - 1994)"),
        3: ("- Atari Jaguar         (1993 - 1996)"),
        4: ("- 3DO                  (1993 - 1996)"),
        5: ("- PC-FX                (1994 - 1998)"),
        6: ("- Sega 32X             (1994 - 1996)"),
        7: ("- Sega Saturn          (1994 - 2000)"),
        8: ("- Playstation          (1994 - 2006)"),
        9: ("- Nintendo 64          (1996 - 2002)"),
        10: ("- Apple Pippin        (1996 - 1997)")
        }
        for items, value in gen5.items():
            print(items,value)
        print()
        print("[Handheld Name] [Years]")
        print()
        gen5h = {
        1: ("- Virtual Boy          (1993 - 1996)"),
        2: ("- Genesis Nomad        (1995 - 1999)"),
        3: ("- Game Boy Pocket      (1996 - 1996)"),
        4: ("- Game.com             (1997 - 2000)"),
        5: ("- Game Boy Light       (1998 - 1998)"),
        6: ("- Game Boy Color       (1998 - 2003)"),
        7: ("- Neo Geo Pocket       (1998 - 1999)"),
        8: ("- WonderSwan           (1999 - 1999)"),
        9: ("- Neo Geo Pocket Color (1999 - 2001)"),
        10: ("- WonderSwan Color    (2000 - 2000)")
        }
        for items, value in gen5h.items():
            print(items,value)
        print()
        input("Press ENTER to continue")
        clear_screen()
        return display_menu()

    elif gen == 6:
        print("Sixth Generation (1998 - 2013)")
        print()
        print("[Console Name] [Years]")
        print()
        gen6 = {
        1: ("- DreamCast        (1998 - 2001)"),
        2: ("- PlayStation 2    (2000 - 2013)"),
        3: ("- GameCube         (2001 - 2007)"),
        4: ("- Xbox             (2001 - 2009)"),
        }
        for items, value in gen6.items():
            print(items,value)
        print()
        print("[Handheld Name] [Years]")
        print()
        gen6h = {
        1: ("- Game Boy Advance  (2001 - 2010)"),
        2: ("- N-Gage            (2003 - 2005)"),
        }
        for items, value in gen6h.items():
            print(items,value)
        print()
        input("Press ENTER to continue")
        clear_screen()
        return display_menu()

    elif gen == 7:
        print("Seventh Generation (2005 - 2012)")
        print()
        print("[Console Name] [Years]")
        print()
        gen7 = {
        1: ("- Xbox 360         (2005 - 2016)"),
        2: ("- PlayStation 3    (2006 - 2017)"),
        3: ("- Wii              (2006 - 2017)"),
        }
        for items, value in gen7.items():
            print(items,value)
        print()
        print("[Handheld Name] [Years]")
        print()
        gen7h = {
        1: ("- Nintendo DS            (2004 - 2013)"),
        2: ("- PlayStation Portable   (2004 - 2014)"),
        }
        for items, value in gen7h.items():
            print(items,value)
        print()
        input("Press ENTER to continue")
        clear_screen()
        return display_menu()

    elif gen == 8:
        print("Eighth Generation (2012 - 2020)")
        print()
        print("[Console Name] [Years]")
        print()
        gen8 = {
        1: ("- Wii U                (2012 - 2017)"),
        2: ("- Nintendo Switch      (2017 - Now)"),
        3: ("- PlayStation 4        (2014 - Now)"),
        4: ("- Xbox One             (2013 - 2020)"),
        }
        for items, value in gen8.items():
            print(items,value)
        print()
        print("[Handheld Name] [Years]")
        print()
        gen8h = {
        1: ("- Nintendo 3DS           (2011 - 2020)"),
        2: ("- Nintendo Switch Lite   (2019 - Now)"),
        3: ("- PlayStation Vita       (2011 - 2019)")
        }
        for items, value in gen8h.items():
            print(items,value)
        print()
        input("Press ENTER to continue")
        clear_screen()
        return display_menu()

    elif gen == 9:
        print("Ninth Generation (2020 - Now)")
        print()
        print("[Console Name] [Years]")
        print()
        gen9 = {
        1: ("- PlayStation 5                (2020 - Now)"),
        2: ("- Xbox Series X / Series S     (2020 - Now)")
        }
        for items, value in gen9.items():
            print(items,value)
        print()
        input("Press ENTER to continue")
        clear_screen()
        return display_menu()

    else:
        print("That is not a valid option. Try again.")
        print()
        input("Press ENTER to continue")
        clear_screen()
        return display_menu()

def main():
    display_menu()

if __name__ == "__main__":
    main()
