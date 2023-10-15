
def main():
    userx1 = float(input("Enter x for center point: "))
    usery1 = float(input("Enter y for center point: "))
    userx2 = float(input("Enter x for perimeter point: "))
    usery2 = float(input("Enter y for perimeter point: "))
    userdistance = distance(userx1, usery1,userx2,usery2)
    userperimeter= perimeter(userdistance)
    print (f"Perimeter of circle centered at ({userx1},{usery1}), with a radius of {userdistance} is {userperimeter}" )

def distance(userx1, usery1,userx2,usery2):
    import math 
    distance = math.sqrt((userx2 - userx1)**2 + (usery2 - usery1)**2)
    return distance


def perimeter(userdistance):
    import math
    perimeter = 2 * math.pi * userdistance
    return perimeter

main()