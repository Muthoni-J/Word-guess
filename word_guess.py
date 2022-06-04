import random
name = input("What is your name? ")
# User first name 
print("Good Luck ! ", name)
words = ['school', 'languages', 'class', 'programming',
         'python', 'mathematics', 'games', 'code',
         'design', 'journey', 'profession', 'graduation']
 
# Function will choose one random
# word from this list of words
word = random.choice(words)
print("Guess the characters")
guesses = ''
# any number of turns can be used here
turns = 5
while turns > 0:    
 # counts the number of times a user fails
    failed = 0    
    for char in word:        
        if char in guesses:
            print(char, end=" ")            
        else:
            print("_")
            print(char, end=" ")
            failed += 1
    if failed == 0:
        print("You Win")
        print("The word is: ", word)
        break
    print()
    guess = input("guess a character:")
    guesses += guess
    if guess not in word:  
        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')    
        if turns == 0:
            print("You Loose")