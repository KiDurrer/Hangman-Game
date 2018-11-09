'''
Programmer: Ki Durrer

TODO

1.Setup Basics, Introduction

2.Setup random word generator that appends to lists

3. Program system to show if you guessed right letter

'''
import random
import os

print('Welcome to Hang-man!')
input('Press ENTER To Play')


def randomword():
    #test word list
    global rword
    randomwordlist = ['car','shop','man','blue'] # Current test list of words, can add more later
    rword = random.choice(randomwordlist)
    return rword

    #introduction
def hangman(word):
    print('DEBUG ANSWER: ' + word) #debug answer
    print('Your word is ' + len(word)*' _ ' + ' spaces long.\n' + 'Begin Guessing!\n')
    guess = '1'
    answer = word
    guessed = []
    
#     listed = len(word)*'{} ' G1
#     unlisted = '_',
    
    #main game loop
    while word != guess or '':
        guess = input('Guess a letter: ')
        print('\n'*100) #for the time being this works for clearing screen
        os.system('cls')
        print(len(word)*' _ ') #placeholderWIP

#         print(listed) G1

        if guess in answer:
            word.replace(guess, "")
        elif guess not in answer and guess not in guessed:
            guessed.append(guess)
        print('Guessed Letters ' + str(guessed))
        
hangman(randomword())


