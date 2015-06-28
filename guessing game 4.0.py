#Author: Asad Aftab
# This is a guess the number game.
import random

guessesTaken = 0

digit_a  = random.randint(1, 9)
digit_b  = random.randint(1, 9) 
digit_c  = random.randint(1, 9) 

number = digit_a,digit_b,digit_c
print('You have eight tries to guess all the digits!')
print('To guess the 2nd and 3rd digits you need to guess the 1st digit correctly!')
print number

while guessesTaken < 12:
	print('Take a guess for the first digit.') 
	guess_1 = input()
	guess_1 = int(guess_1)
	print('Take a guess for the second digit.')
	guess_2 = input()
	guess_2 = int(guess_2)
	print('Take a guess for the third digit.')	
	guess_3 = input()
	guess_3 = int(guess_3)
	
	guessesTaken = guessesTaken + 1

	if guess_1 < digit_a:
		print('Your guess is too low for the first digit.') 

	if guess_1 > digit_a:
		print('Your guess is too high for the first digit.')
	
	if guess_1 == digit_a:
		print('Your guess for the first digit is right!')
	
	guessesTaken = guessesTaken + 1
	
	if guess_2 < digit_b:
		print('Your guess is too low for the second digit')
	
	if guess_2 > digit_b:
		print('The guess is too high for the second digit')
	
	if guess_2 == digit_b:
		print('Your guess for the second digit is right!')
	
	guessesTaken = guessesTaken + 1
	
	if guess_3 < digit_c:
		print('Your guess is too low for the third digit.') 
	
	if guess_3 > digit_c:
		print('Your guess is too high for the third digit')
	
	if guess_3 == digit_c:
		print('Your guess is for the third digit is right!')
		break

guess = guess_1,guess_2,guess_3
	
if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job! You guessed the number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('You lose! The number I was thinking of was ' + number)