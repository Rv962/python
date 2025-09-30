#to print random integers

import random

a = random.randint(1 , 10)
print(a)

# to print random float number between o and 1
b = random.random()
print(b)

# virtual coin toss program

import random
c = random.randint( 0, 1 )
if c == 1:
    print('heads')
else:
    print('tails')

# rounding off 
d = round(random.random(),5)
print(d)