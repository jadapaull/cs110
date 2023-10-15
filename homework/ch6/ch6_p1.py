def main():
    numbers = open(r'Desktop/cs110/Homework/ch6/p1_numbers.txt','r')
    value = int(numbers.readline())
    value2 = int(numbers.readline())
    value3 = int(numbers.readline())
    value4 = int(numbers.readline())
    value5 = int(numbers.readline())
    numbers.close()
    print(value)
    print(value2)
    print(value3)
    print(value4)
    print(value5)
    print(f"Sum:{value + value2 + value3 + value4 + value5}")


main()