CORRECTFIRSTLETTER = False
CORRECTENDING= False
LOWERCASE= False
ALPHANUMERIC= False

def main():
    email =str(input("Enter a USF email: " ))
    validateemail = validateusfemail(email)
    if validateemail == True:
        print("Valid USF email! ")
    else: 
        print("Enter a Valid USF email! ")
        main()

def validateusfemail(email):
    indexposition = 0  
    if email[0].isalpha():
        CORRECTFIRSTLETTER = True
    else: 
        CORRECTFIRSTLETTER= False
    if email.endswith("@usfca.edu"):
        CORRECTENDING = True
    else: 
        CORRECTENDING = False
    indexposition = email.find('@', indexposition)
    for i in range(indexposition):
        if email[0:indexposition:1].islower():
            LOWERCASE = True
        else: 
            LOWERCASE = False
        if email[0:indexposition:1].isalnum():
            ALPHANUMERIC= True
        else: 
            ALPHANUMERIC = False
    if CORRECTFIRSTLETTER and CORRECTENDING and LOWERCASE and ALPHANUMERIC:
        return True
    else:
        return False

main()