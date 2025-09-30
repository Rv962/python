# adding even numbers from 1 to 100

total = 0
for number in range (2 , 101 , 2):
    total += number
print(total)

# For a number printing frizzbuzz 
# % is used to get reminder 

for number in range (1, 101):
    if number % 3 ==0 and number % 5 == 0:
        print ("frizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzzz")
    
        
    else:
        print(number)