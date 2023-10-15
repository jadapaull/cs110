def main():
    userradius = float(input("Enter the radius: "))
    validradius = is_valid_radius(userradius)
    diameter = calc_diameter(userradius)
    circumference = calc_circumference(userradius)
    area = calc_area(userradius)
    print (f"A circle of radius {userradius}, has a diameter of {diameter:.3f}, a circumference of {circumference:.3f}, and an area of {area:.3f}. ")
    
def is_valid_radius(userradius):
    if userradius <= 0:
        print("Goodbye!")
        exit()

def calc_diameter(userradius):
    diameter = userradius * 2
    return diameter

def calc_circumference(userradius):
    import math
    circumference = 2* math.pi * userradius 
    return circumference

def calc_area(userradius):
    import math 
    area = math.pi * userradius **2
    return area

main()