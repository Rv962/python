import random

print("welcome to number Guessing Game")
print("I'm thinking of a number between 1 and 100")

chosen_no = int(random.randint(1, 101) )
#print(chosen_no)
level = input("choose diffculty level,   E for 'Easy' , H for ' Hard'  :  ")

if level == "E" :
    lives = 10
    print("you've 10 attempts")
else :
    lives = 5
    print ("you've 5 attempts")      
    
while True :
    if lives > 0 :
        guess = int(input(" Guess the number : "))
        if guess > chosen_no : 
            lives  -= 1
            print(f"you've {lives} attenpts ")    
            print( "Guess is too high")
        elif guess < chosen_no :
            lives -= 1
            print(f"you've {lives} attempts " )
            print("Guess is too low")
        elif guess == chosen_no :
            print("Correct answer, You Win")
            break
    else :
        print("you've lost")
        break
    
    
