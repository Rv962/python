print ("welcome to pizza python")
size = input('what size do you want ? s, m or l : ')
pepperoni = input ('do you want pepperoni ? y or n : ')
cheese = input ('do you want extra cheese ? :')

bill = 0
if size == 's' :
    bill += 150
elif size == 'm' :
    bill += 200
else :
    bill += 250

if pepperoni == 'y' :
    if size == 's' :
        bill += 20
    elif size == 'm' :
        bill += 30
    else :
        bill += 40

if cheese == 'y':
    bill += 10
else:
    bill += 0
    
print (f"your bill is rs {bill}")