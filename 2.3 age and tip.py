age = input("what's you current age : ")
a = 90 - int(age)
days = a*365
weeks = a*52
months = a*12
print(f"you have {days} days, \n or { weeks} Weeks , \n or {months} months left to live if you live till 90,\n enjoy while you can" )


print("welcome to the tip calculator")
bill = int(input("what's your bill ? : "))
tip = int(input ("what's the percentage of tip you want to give ? : "))
people = int(input("how many people to split it in? : "))
pay = ((bill*tip)/100 + bill )/people
pay_1 = round (pay , 2)
print(f"Each person should pay {pay_1} rs")
