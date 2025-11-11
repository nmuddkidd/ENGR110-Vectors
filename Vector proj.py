def conversion():
    print("conversion")
    deg = int(input("input degrees: ")) + int(input("input minutes: "))/60 + int(input("input seconds: "))/3600
    print(deg,"are the decimal degrees")
    input("press enter to return to menu")

def directconversion(degrees, minutes, seconds):
    return degrees+minutes/60+seconds/3600;
1
def distancecalc():
    print("distance calc")
    input("press enter to return to menu")

def haversinecalc():
    print("haversine calc")
    input("press enter to return to menu")

choice = -1;
while choice != 0:
    print("MENU:")
    print("0) exit")
    print("1) Geographic coordinate conversion")
    print("2) Resultant vector calculation (distance)")
    print("3) Resultant vector calculation (haversine)")
    choice = int(input())
    match choice:
        case 1:
            conversion()
        case 2:
            distancecalc()
        case 3:
            haversinecalc()
