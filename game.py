'''
Programmer: Ki Durrer

TODO

1.Setup Basics, Introduction

2.Setup random word generator that appends to lists

3. Program loop system to show if you guessed right letter

'''
import random
import os

print('Welcome to Hang-man!')
input('Press ENTER To Play')


def randomword():
    #test word list
    global rword
    randomwordlist = ['car','shop','man','blue','blueberry'] # Current test list of words, can add more later
    rword = random.choice(randomwordlist)
    return rword

    #introduction
def hangman(word):
    print('DEBUG ANSWER: ' + word) #debug answer
    print('Your word is ' + len(word)*' _ ' + ' spaces long.\n' + 'You have 10 attempts\n' + 'Begin Guessing!\n')
    guess = '1'
    answer = word
    guessed = []
    log = []
    attempts = 10 
    
    #main game loop
    while attempts > 0:
        guess = input('Guess a letter: ')
        wordmat = ''
        log.append(guess)  
        print('\n'*100) #for the time being this works for clearing screen
        os.system('cls')

        for letters in word:
            if letters in log:
                wordmat = wordmat + letters
            else:
                wordmat = wordmat + " _ "
                
        print(wordmat)
        
        if wordmat == word:
            break
        
        if guess not in answer and guess not in guessed:
            guessed.append(guess)
        print('Guessed Letters ' + str(guessed))

        if guess not in word:
            attempts -= 1
        print('Attempts left: '+str(attempts))
        
    if attempts:
        print('You guessed ' + word)
    else:
        print('Game over, you did not guess ' + word)
hangman(randomword())
