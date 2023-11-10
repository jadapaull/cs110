def main():
    num1= int(input("enter number 1: "))
    num2= int(input("enter number 2: "))
    num3= int(input("enter number 3: "))
    num4= int(input("enter number 4: "))
    num5= int(input("enter number 5: "))
    num_list = [num1,num2,num3,num4,num5]
    low = lowest(num_list)
    high = highest(num_list)
    totalnum = total(num_list)
    averagenum = average(totalnum)
    print(" ")
    print (f"Lowest Number : {low}")
    print(f"Highest number: {high} ")
    print (f"Total: {totalnum}")
    print(f"Average: {averagenum}")

def lowest(num_list):
    return (min(num_list))

def highest(num_list):
    return (max(num_list))

def total(num_list):
    total = 0
    for i in num_list:
        total += i
    return total

def average(totalnum, num_list):
    averagenum =totalnum/len(num_list)
    return averagenum

main()