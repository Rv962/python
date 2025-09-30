print ('welcome to the treasure Island')
print ('your mission is to find the treasure')
a = input('you are at crossroads, choose right or left : ').lower()
if a == 'left' :
    b= input("you now at a pond, will you wait or swim ? :  ").lower()
    if b == 'wait' :
        c= input("you've found a 3 doors, red , blue and yellow, choose one : ").lower()
        if c== 'yellow' :
            print ("you win")
        else:
            print("game over")
    else:
        print("game over")
else:
    print("game over")
            
         
            
        
        