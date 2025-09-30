print("Welcome to the roller coster ride ")
height = int(input(" enter your height in cms : "))
   
if height >= 120 :
    
    age = int(input("your age ? "))
    print("you can ride rollercoaster")
    photo = input ("do you want photos ?  yes or no  : ")
    
    
    if age < 12 :
        bill = 10
        print ("you have to pay 10 rs")
    elif age <= 18 :
        bill = 15
        print ("you have to pay 15 rs")
   
    elif age >= 45 and age <= 55 :
             bill = 0
             print ("don't have to pay ride is on us")
    else:
        bill = 20
        print("you have to pay 20 rs")
        
        
    
    if photo == "yes" :
              bill += 50
              print (f" you have to pay { bill } ")
              
         
else :
     print ("sorry you've to grow taller ,  so can't ride")