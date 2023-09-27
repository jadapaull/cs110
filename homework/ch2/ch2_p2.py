VODKA_OZ= 2.0
TRIPLE_SEC_OZ= 0.5
LEMON_JUICE_OZ= 1.0             #constants for each ingredient
SIMPLE_SYRUP_OZ= 1.0
OZ_TBS = 2
lemondrops= int(input("How many Lemon Drops to make: ")) #asks users how many to make
print (f"To make {lemondrops} Lemon Drop/(s) mix:")
vodkatbs = VODKA_OZ* OZ_TBS
triplesectbs = TRIPLE_SEC_OZ* OZ_TBS
simplesyruptbs = SIMPLE_SYRUP_OZ* OZ_TBS            #converts ounces to tablespoons
lemonjuicetbs= LEMON_JUICE_OZ* OZ_TBS
vodka = float(vodkatbs*lemondrops)
triplesec = float(triplesectbs*lemondrops)     #converts number of lemondrops user entered
lemonjuice = float(lemonjuicetbs*lemondrops)    #to the amount they need to add
simplesyrup = float(simplesyruptbs*lemondrops)
print (f"* {vodka} tbs of vodka")
print ( f"* {triplesec} tbs of triple sec")     #shows recipie user needs to make
print(f"* {lemonjuice} tbs of lemon juice")
print(f"* {simplesyrup} tbs of simple syrup")

