def main():
    userfullname =str(input("Enter your full name: " ))
    wordcheck = wordcounter(userfullname)
    firstmiddlelast =firstmiddlelastinitial(userfullname)
    if wordcheck >= 2 :
        print(firstmiddlelast)
    else: 
        print("You must enter your first middle and last name!")
        main()
        
def wordcounter(userfullname): 
    spacecounter = 0 
    for i in userfullname:
        if i == ' ':
            spacecounter += 1
    return int(spacecounter)

def firstmiddlelastinitial(userfullname):
    indexposition = 0 
    letter = userfullname[indexposition]
    initials = ''
    while indexposition != -1:
        letter= letter.upper()
        initials += letter
        initials += '.'
        indexposition = userfullname.find(' ', indexposition + 1)
        letter = userfullname[indexposition + 1]
    return initials

main()

