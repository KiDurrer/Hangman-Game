'''
Programmer: Ki Durrer, Miles Boswell
TODO:
[X] Setup Basics, Introduction
[X] Program loop system to show if you guessed right letter
[ ] Use larger list of words to choose from
[X] Display image of hangman
[ ] Show letter guesses in color
'''
from hangman import HANGMAN
import random
import os

print('Welcome to Hang-man!')
input('Press ENTER To Play')


def randomword():
	#test word list
	randomwordlist = ['car','shop','man','blue','blueberry']
	rword = random.choice(randomwordlist)
	return rword

def place_letters(wordmat, word, letter):
	locations = [i for i, _ in enumerate(word) if word.startswith(letter, i)]

	for loc in locations:
		wordmat = wordmat[:loc] + letter + wordmat[loc+1:]
	return wordmat


def hangman(word):
	print('DEBUG ANSWER: ' + word)

	guessed = []
	attempts = 7 
	n = attempts

	wordmat = '_' * len(word)
	blanks = ' '.join(wordmat)

	#main game loop
	while attempts > 0:
		print('=====================================')
		print('Guessed letters: {}\nAttempts left: {}' \
		    .format(','.join(guessed), attempts))
		print(blanks)

		guess = input('Guess a letter: ')


		if guess in guessed:
			print('You already guessed {}. Guess again!'.format(guess))

		elif guess not in word:
			print('{} is not in my word.'.format(guess))
			guessed.append(guess)
			attempts -= 1

		else:
			# guess is in word and hasn't been guessed already
			guessed.append(guess)
			wordmat = place_letters(wordmat, word, guess)
			blanks = ' '.join(wordmat)

			if wordmat == word:
				print(HANGMAN[n - attempts])
				print('Congratulations! You guessed {}!'.format(word))
				break
		print(HANGMAN[n - attempts])

	else:
		print('Game over, you ran out of guesses. My word was {}.'.format(word))


print()
print('Begin Guessing!')
hangman(randomword())
