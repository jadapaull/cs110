def main():
    nameIn = open(r"/Users/jadapaul/Desktop/cs110/homework/ch8/p2_runnybabbit.txt", "r")
    for line in nameIn:
        names = makeWords(line)
        writeFile(names)
    return

def makeWords(line):
    correctedName = correctLetters(line)
    return correctedName

def correctLetters(name):
    first = ''
    last = ''
    name = str(name)
    space = name.find(" ")
    first += name[space + 1]
    last += name[0]
    for letter in range(1, space):
        first += name[letter]
    for letter in range(space + 2, len(name)):
        last += name[letter]
    last = last.strip()
    names = [first, last]
    return names


def writeFile(correctName):
    namesOut = open(r"/Users/jadapaul/Desktop/cs110/homework/ch8/names.txt", "a")
    namesOut.write(str(correctName[0]))
    namesOut.write(" ")
    namesOut.write(str(correctName[1]))
    namesOut.write("\n")
    return

main()