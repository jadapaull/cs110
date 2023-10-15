def main():
    readfile = 'Desktop/cs110/Homework/ch6/p3_numbers.txt'
    writefile = 'Desktop/cs110/Homework/ch6/squared.txt'
    squareWrite(readfile, writefile)

def squareWrite(readfile, writefile):
    file = open(readfile, 'r')
    file1 = open(writefile, 'w')
    errors = 0
    for line in file:
        try:
            number = 0
            number = int(line)
            square = number**2
            file1.write(str(square))
            file1.write('\n')
        except:
            errors += 1
    file1.write(str(square))
    print("number of errors is", errors)
    file.close()
    file1.close()

main()