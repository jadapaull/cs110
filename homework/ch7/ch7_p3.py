
def main():
    file = r'/Users/jadapaul/Desktop/cs110/homework/ch7/p3_water.txt'
    readandlist1 = readandlist(file)
    nestedlist= nestedlistandaverage(readandlist1)



def readandlist(file):
    openfile = open(file,'r')
    fileread= openfile.readlines()
    february = []
    for day in fileread:
        february.append (int(day.rstrip()))
   
    return february

def nestedlistandaverage(readandlist1):
        week1= readandlist1[:7:]
        week2 = readandlist1 [7:14:]
        week3 = readandlist1[14:21:]
        week4= readandlist1[21:29:]
        nestedwater = [week1, week2, week3, week4]
        average1 = sum(week1)/len(week1)
        average2 = sum(week2)/len(week2)
        average3= sum(week3)/ len(week3)
        average4= sum(week4)/len(week4)

        print("Average glasses of water per week:")
        print(f"Week 1: {average1}")
        print(f"Week 2: {average2}")
        print(f"Week 3: {average3}")
        print(f"Week 4: {average4}")

        return
 


main()