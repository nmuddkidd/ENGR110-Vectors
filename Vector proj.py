import math
def conversion():
    print("Conversion")
    deg = int(input("Input degrees: "))
    if(deg>=0):
        deg += (int(input("Input minutes: "))/60 + float(input("Input seconds: "))/3600)
    else:
        deg -= (int(input("Input minutes: "))/60 + float(input("Input seconds: "))/3600)
    print(f"{deg:.4f} are the decimal degrees.")
    input("press enter to return to menu")

def con():
    deg = int(input("Input degrees: "))
    if(deg>=0):
        deg += (int(input("Input minutes: "))/60 + float(input("Input seconds: "))/3600)
    else:
        deg -= (int(input("Input minutes: "))/60 + float(input("Input seconds: "))/3600)
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
   x = lat2-lat1
   y = long2-long1
   heading = ((math.atan2(y,x))*180/math.pi)+360
   dis = math.sqrt((math.pow((lat1-lat2), 2)+math.pow((long1-long2),2)))
   print(f"The resultant vector is {dis:.2f} meters with the heading {heading:.1f} degrees from north.")
<<<<<<< HEAD
   print(f"The vector is {x:.2f}i + {y:.2f}j")
=======
   print(f"The vector is {y:.2f}i + {x:.2f}j meters")
>>>>>>> 994bdf04839dda796ed93e8afabff8653143e4ff
   input("press enter to return to menu") 

def haversinecalc():
    print("Haversine Calculation")
    print("--Point 0 latitude--")
    point0lat = con()
    print("--Point 0 longitiude--")
    point0long = con()
    print("--Point 1 latitude--")
    point1lat = con()
    print("--Point 1 longitiude--")
    point1long = con()
    dlat = (point1lat - point0lat)*math.pi/180
    dlong = (point1long - point0long)*math.pi/180
    print(f"{(abs(point1long) - abs(point0long))*111320*abs(math.cos(point1lat)):.2f}i {(point1lat - point0lat)*111200:.2f}j")
    print((point1long - point0long))
    point0lat *= math.pi/180
    point0long *= math.pi/180
    point1lat *= math.pi/180
    point1long *= math.pi/180
    havtheta = (1-math.cos(dlat))/2 + math.cos(point0lat) * math.cos(point1lat) * (1-math.cos(dlong))/2
    rad = 2 * math.atan2(math.sqrt(havtheta), math.sqrt(1-havtheta));
    distance = 6371000 * rad

    y = math.sin(dlong)*math.cos(point1lat)
    x = math.cos(point0lat)*math.sin(point1lat)-math.sin(point0lat)*math.cos(point1lat)*math.cos(dlong)
    bearing = math.atan2(y,x)*180/math.pi
    bearing = (bearing+360)%360

    print(f"The haversine method indicates the two points are {distance:.2f} meters apart with a bearing of {bearing:.2f} degrees from north")
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
