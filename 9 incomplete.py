from replit import clear

auction = [  ]

def add_new(name,  price):
    new_name = { }
    new_name["name"]  = name
    new_name["price"] = price
    
    auction.append(new_name)
    
    
    highest_bid = 0
    for bidder in new_name:
        bid_amount = new_name["price"]  
        if bid_amount > highest_bid:
            highest_bid = bid_amount
    
    
    
    
people = True
while people:
    name = input("enter name: ")
    price = int(input ("entry price : \n$"))
    answer = input("do you have more people, yes or no : \n")
    if answer == "no":
        people = False
        print("ok, wait for the results")
    elif answer == "yes":
        clear()
        
    add_new(name, price)



print(auction)


