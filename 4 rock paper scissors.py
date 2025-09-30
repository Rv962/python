rock = '''
    _______
---'   _____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    ______
---'   ____ )____
          ________)
          _________)
         _________)
---.__________)
'''

scissors = '''
    ______
---'   ____)____
          ________)
       ___________)
      (____)
---._(____)
'''

#Write your code below this line 👇
choice = int(input(" what's your choice? type 0 for rock, 1 for paper and 2 for scissors : "))
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print (scissors)
    
print("computer choice is --")
import random
computer = random.randint(0, 2)
if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
elif computer == 2:
    print (scissors)
    

if choice == computer:
    print("it's a draw")
elif choice ==0 and computer ==2 :
    print("player wins")
elif choice > computer :
     print ("player wins")
else:
    print(" player lose")
