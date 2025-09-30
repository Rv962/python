import random
from replit import clear

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                  

deck =[ 11, 2 , 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10 ]
def deal() :        
    card = random.choice(deck)
    return card
                                                                                                                                
def total_score (cards) :
    if  11 in cards and len(cards)   == 2 :
        cards.remove(11)
        cards.append( 1 )
    return sum(cards)                                                 

def compare(user_score, comp_score) :
    if user_score > 21 and comp_score > 21 :
        return "you both loose"                
    
    if user_score == comp_score :
        return "it's a draw"                                     
    elif user_score == 21 :
        return "user wins"                                                      
    elif comp_score == 21 :
        return "user loose"                                                         
    elif user_score >  21 :
        return "user loose "                                                      
    elif comp_score  > 21 :
        return "user win"                   
    elif user_score > comp_score :
        return "user win"                                                             
    else :
        return "user loose"                                              

                                                 
                                                                     

def play_game ( ) :
    print(logo)
    user = [ deal() , deal() ]
    comp = [ deal(), deal()]


    

    while True :
        user_score = total_score(user)
        comp_score = total_score(comp)
        print(f"your cards are : {user} & your score  = {user_score} ")
        print(f"computer first card is :  {comp[0]}")
        
        if user_score == 21 or comp_score == 21 or user_score > 21 :
            break
        else :
            another_card = input(" type 'y' to get another card or 'n' to pass : ")
            if another_card == "y" :
                user.append(deal())
            else :
                break
                
    while comp_score < 17 :
        comp.append(deal())
        comp_score = total_score(comp)
            
    print(f"your final hand is : {user} & your score = {user_score}")
    print(f"computer final hand is :{comp} & it's score = {comp_score} ")
    print(compare(user_score, comp_score))        


while input("do you want to play ? 'y' or 'n'  :  ") :
    clear()
    play_game()
