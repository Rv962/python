alphabet =     ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input ("encode for encryption and decode for decryption :\n")
text = input("enter test you want to encode : \n").lower()
shift = int(input ("letters you want to shift : \n"))

# function created for encryption

def encrypt (plain_text, plain_shift):
    display = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + plain_shift
        if new_position > 26:
            new_position = new_position - 26
        new_letter = alphabet[new_position]
        display += new_letter
           
    print(f"your encoded texts are {display}")
    
    
#encrypt(plain_text = text, plain_shift = shift)


def decrypt (plain_text, plain_shift):
    display = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position - plain_shift
        if new_position < 0:
            new_position = new_position + 26
        new_letter = alphabet[new_position]
        display += new_letter
           
    print(f"your decoded texts are {display}")
    
    
#decrypt(plain_text = text, plain_shift = shift)

if direction  == "encode":
    encrypt(plain_text = text, plain_shift = shift)
elif direction == "decode":
    decrypt(plain_text = text, plain_shift = shift)
else:
    print("choose correctly")

        
        
        
    