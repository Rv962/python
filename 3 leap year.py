print("Leap year finder")
year = int(input("which year do you want to check ? : "))
if year % 4 == 0 :
    if year % 100 == 0 :
        if year % 400 == 0:
            print ("it's a leap year by 400")
        else:
            print( " it's not a leap year by 400")
    else :
        print("it's a leap year by 100")
else :
    print ("it's not a leap year by 4")
    
