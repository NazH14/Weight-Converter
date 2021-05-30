Weight = int(input("What is your weight?: "))
Unit = str(input("Is this in (K)g or or (L)bs? (please type K or L): "))

if Unit.upper() == "K":
    converted = Weight * 2.20462
    print("This is " + str(converted) + " Lbs")
else:
    converted = Weight / 2.20462
    print("This is " + str(converted) + " Kg")




0