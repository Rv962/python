print ('welcome to the love calculator') 
name1 = input('what is your name ? : ').lower()
name2 = input('what if her/his name ? : ').lower()

# first = name1.count('t') + name1.count('r') + name1.count('u') + name1.count('e') + name2.count('t') + name2.count('r') + name2.count('u') + name2.count('e')
# second = name1.count('l') + name1.count('o') + name1.count('v') + name1.count('e') + name2.count('l') + name2.count('o') + name2.count('v') + name2.count('e')
# total = int(str(first) + str(second))
# if total <10 or total >90 :
#     print (f" your score is {total} , you go together like coke and mentos ")
# elif total >40 and total <50 :
#     print (f" your score of {total}, you are alright together")
# else :
#     print(f"you score is {total}")
    
    
# second method 
# count function is used to count letters in a string
combine = name1 + name2
first = combine.count('t') + combine.count('r') + combine.count('u') + combine.count('e')
second = combine.count('l') + combine.count('o') +combine.count('v') + combine.count('e')
total = int(str(first) + str(second))
if total <10 or total >90 :
    print (f" your score is {total} , you go together like coke and mentos ")
elif total >40 and total <50 :
    print (f" your score of {total}, you are alright together")
else :
    print(f"you score is {total}")
