import math
def conversion():
    print("Conversion")
    deg = int(input("Input degrees: ")) + int(input("Input minutes: "))/60 + int(input("Input seconds: "))/3600
    print(deg,"are the decimal degreess.")
    input("press enter to return to menu")

def radconversion():
    return (int(input("Input degrees: ")) + int(input("Input minutes: "))/60.0 + float(input("Input seconds: "))/3600.0) * math.pi/180;

def distancecalc():
   ## print("Distance Calculation")
   ## x = int(input("Input x value in meters: "))
   ## y = int(input("Input y value in meters: "))
   ## dis = math.sqrt((x*x)+(y*y))
   ## print("The resultant vector is", dis, "meters.")
   ## input("press enter to return to menu") 

def haversinecalc():
    print("Haversine Calculation")
    print("--Point 0 latitude--")
    point0lat = radconversion()
    print("--Point 0 longitiude--")
    point0long = radconversion()
    print("--Point 1 latitude--")
    point1lat = radconversion()
    print("--Point 1 longitiude--")
    point1long = radconversion()
    dlat = point1lat - point0lat
    dlong = point1long - point0long
    havtheta = (1-math.cos(dlat))/2 + math.cos(point0lat) * math.cos(point1lat) * (1-math.cos(dlong))/2
    rad = 2 * math.asin(math.sqrt(havtheta))
    distance = 6371000 * rad

    print("The haversine method indicates the two points are",distance,"meters apart")
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
