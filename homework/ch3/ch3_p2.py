EUR_EUROS_1 = 1.0727        #Euros constant
JAPANESE_YEN_1 = 0.0068     #Yen constant
POUND_STERLING_1 = 1.2502   #Sterling constant
MEXICAN_PESO_1 = 0.0567     #Pesos constant

print("(EUR) EUROS\n"
      "(JPY) Japanese Yen\n"
      "(GBP) Pound Sterling\n"      #prints statement for user to pick
      "(MXC) Mexican Peso")

usercurrency =str(input("Select a currency to convert from: ")) # user selects currenct ro convert from

if usercurrency == "EUR" or usercurrency == "eur":      #if statment reguarding eur
    amounteur = float(input("Enter amount of Euros to convert: € "))  #amount to convert
    converteur = EUR_EUROS_1 * amounteur    #conversion
    print(f"In USD that is $ {converteur:,.2f}")  #tells user amount in USD

elif usercurrency == "JPY" or usercurrency == "jpy":    #if statement reguarding jpy
    amountjpy = float(input("Enter amount of Japanese Yen to convert: ¥ "))   #amount to convert
    convertjpy = JAPANESE_YEN_1 * amountjpy #conversion
    print(f"In USD that is $ {convertjpy:,.2f}")  #tells user amount in USD

elif usercurrency == "GBP" or usercurrency == "gbp":    #elif statement reguarding gbp
    amountgbp = float(input("Enter amount of Pound Sterling to convert: ₽ ")) #amount to convert
    convertgbp = POUND_STERLING_1 * amountgbp   #conversion
    print(f"In USD that is $ {convertgbp:,.2f}")  #tells user amount in USD

elif usercurrency == "MXN" or usercurrency == "mxn":    #elif statement reguarding mxn
    amountmxn = float(input("Enter amount of Mexican Pesos to convert: ₱ "))  #amount to conver
    convertmxn = MEXICAN_PESO_1 * amountmxn     #conversion
    print(f"In USD that is $ {convertmxn:,.2f}")  #tells user amount in USD

else:
    print ( "Invalid entry. Please try again.") #try again if non are accepted