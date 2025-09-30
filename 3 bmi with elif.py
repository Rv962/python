a = float(input ( " what's your weight in kg's : "))
b = float(input (" what's your height in m : "))
c = round( (a) /  ((b) **2),2)
print ( " your BMI is : " + str(c ))
if c < 18.5 :
    print (" you are underweight ")
elif c < 25 :
    print (" you've have normal weight")
elif c < 30 :
    print (" you are  overweight")
elif c <= 35 :
    print ("you are obese")
else:
    print ("you are clinically obese")
    