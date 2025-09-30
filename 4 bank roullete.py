import random

# splitting a list of strings with ---SPLIT ---function

name_string = input(" Give me everybody's names separated by a comma :")
names = name_string.split(",")
#print(names)
#print(names[2])
length = len(names)
#print(length)
choice = random.randint(0, length-1)
#print(choice)
paywho = names[choice]
print(paywho + " is the person who is going to pay")