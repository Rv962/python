# bmi = weight/ (height's square )
# ** used for multiplying that number again that many times
# print(5**3)

a = input ( " what's your weight in kg's : ")
b = input (" what's your height in m : ")
c= float(a)
d= float(b)
e= d**2
print ( " your BMI is : " + str( c/e))

a = input ( " what's your weight in kg's : ")
b = input (" what's your height in m : ")
print ( float(a) /  (float(b) **2))
print ( " your BMI is : " + str ( float(a) /  (float(b) **2)))


x =  float(a) /  (float(b) **2)
print(round (x , 2))