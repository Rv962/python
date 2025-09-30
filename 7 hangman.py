HANGMANPICS =  [ '''
 
 +---+
  |      |
  O    |
 /|\   |
 / \   |
        |
========= ''', '''

 +---+
  |      |
  O    |
 /|\   |
 /      |
        |
=========''', '''

  +---+
  |     |
  O   |
 /|\  |
        |
        |
=========''', '''
  +---+
  |     |
  O   |
 /|    |
        |
        |
=========''', '''
  +---+
  |     |
 O    |
  |     |
        |
        |
=========''', '''
  +---+
  |   |
 O   |
      |
      |
      |
=========''', '''
+---+
  |   |
      |
      |
      |
      |
=========''',  
 ]


#from replit import clear
import random
# if suppose you've another file named hangman containing many words under a list called word_list
# then you can import that file with import command
 # import hangman 1way
 # chosen_word = random.choice(hangman.word_list)
word_list = ["safipur" , "monkey"]
chosen_word = random.choice(word_list)
#print(chosen_word)

# display blanks as much as chosen word
display = [ ]
for letters in chosen_word:
    display += "_"
#print(display)

end_of_game = False
Lives = 6

while  end_of_game == False:
    guess = input("Guess a letter of your choosing : ")
    
    #clear()
    
    if guess in display:
        print(f"you've already guessed {guess}")
    # replace guessed letters with blanks
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
       print(f"you guessed {guess} which is wrong so you lose a life")
       Lives -= 1
       if Lives == 0:
           end_of_game = True
           print ("you lose")
       
    #print(display)
    print(f"{' '. join(display)}")
  
    print(Lives)
    if "_" not in display:
            end_of_game = True
            print("you win")
            
    print(HANGMANPICS[Lives])



