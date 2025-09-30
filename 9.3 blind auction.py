from replit import clear

# to find highest bidder name
def highest_bidder(record):
    highest = 0
    name =" "
    for bidder in record:
          bid_amount = record[bidder]                            
          if bid_amount > highest :
              highest = bid_amount
              name = bidder
    print(f"the winner is {name} with a bid of  {highest}")              
              
              
          
auction = {
"ram" : 81
}

while True :
    answer = input("do you want to auction ,  y or n : ")
    if answer == "y":
        x = input("enter name : ")
        y = int(input("enter price : "))
        auction[x] = y
        
        clear()
    else:
        highest_bidder(auction)
        break
        
print(auction) # should be hidden

prices = [ ]    
for i in auction :
    prices.append(auction[i])                                        
winner = max(prices)
print("so the winner is : ", winner)



                          
                    
            
                    
        