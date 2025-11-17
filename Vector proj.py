import math
def conversion():
    print("Conversion")
    deg = int(input("Input degrees: ")) + int(input("Input minutes: "))/60 + float(input("Input seconds: "))/3600
    print(f"{deg:.4f} are the decimal degreess.")
    input("press enter to return to menu")

def radconversion():
    return (int(input("Input degrees: ")) + int(input("Input minutes: "))/60.0 + float(input("Input seconds: "))/3600.0) * math.pi/180;

def con():
    deg = int(input("Input degrees: ")) + int(input("Input minutes: "))/60 + float(input("Input seconds: "))/3600
    print("Converting.")
    return deg

def distancecalc():
   print("Distance Calculation")
   print ("Input first latitude.")
   lat1 = (40000000/360) * con()
   print ("Input first longitude.")
   long1 = (40000000/360) * con()
   print ("Input second latitude.")
   lat2 = (40000000/360) * con()
   print ("Input second longitude.")
   long2 = (40000000/360) * con()
   dis = math.sqrt((math.pow((lat1-lat2), 2)+math.pow((long1-long2),2)))
   print(f"The resultant vector is {dis:.2f} meters.")
   input("press enter to return to menu") 

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
