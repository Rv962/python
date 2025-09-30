# to find if a number is odd or even
print("find if a number is odd or even")
number = int(input("enter number : "))
a = number % 2
if a == 1 :
    print( " this is odd number")
else :
    print (" this is even number")
    
    
# rollercoster ride with tickets   
print("Welcome to the rollercoster ride ")
height = int(input("Enter your height in cms  : "))
   
if height >= 120 :
    
    age = int(input("your age ? : "))
    if age > 5 :
        print("you can ride rollercoaster")
        if age < 12 :
            print ("you have to pay 5 rs")
        elif age <= 18 :
            print ("you have to pay 7 rs")
        else :
            print("you have to pay 12 rs")
    else :
        print("you are underage, can't ride ")
else :
     print ("sorry you've to grow taller ,  so can't ride")
     
    
    