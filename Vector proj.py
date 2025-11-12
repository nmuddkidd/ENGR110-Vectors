import math
def conversion():
    print("Conversion")
    deg = int(input("Input degrees: ")) + int(input("Input minutes: "))/60 + int(input("Input seconds: "))/3600
    print(deg,"are the decimal degreess.")
    input("press enter to return to menu")

def directconversion(degrees, minutes, seconds):
    return degrees+minutes/60+seconds/3600;
1
def distancecalc():
    print("Distance Calculation")
    x = int(input("Input x value in meters: "))
    y = int(input("Input y value in meters: "))
    dis = math.sqrt((x*x)+(y*y))
    print("The resultant vector is", dis, "meters.")
    input("press enter to return to menu")

def haversinecalc():
    print("Haversine Calculation")
    input("press enter to return to menu")

choice = -1;
while choice != 0:
    print("MENU:")
    print("0) exit")
    print("1) Geographic Coordinate Conversion")
    print("2) Resultant vector calculation (Distance)")
    print("3) Resultant vector calculation (Haversine)")
    choice = int(input())
    match choice:
        case 1:
            conversion()
        case 2:
            distancecalc()
        case 3:
            haversinecalc()
