alphabet =     ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
'p',   'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cypher (plain_text, plain_shift, direction):
    display = ""
    if direction == "decode":
            plain_shift  *=  -1
    for letter in plain_text:
        if letter in alphabet:
        
       
            position = alphabet.index(letter)
        
            new_position = position + plain_shift
            if new_position > 26:
                new_position = new_position - 26
            elif  new_position < 0:
                new_position = new_position + 26
            new_letter = alphabet[new_position]
            display += new_letter
            
        else:
           display += letter
           
    print(f"your {direction} texts are :  {display}")
    
    
should_continue = True
while should_continue :
    
    direction = input ("encode for encryption and decode for decryption :\n")
    text = input("enter test you want to encode : \n").lower()
    shift = int(input ("letters you want to shift : \n"))
    shift = shift % 26
    
    cypher(plain_text = text, plain_shift = shift, direction=direction )
    
    result = input("type yes to continue and no to stop: \n").lower()
    if result == "no":
        should_continue = False
        print("Good bye")
    

