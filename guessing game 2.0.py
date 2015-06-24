#Author: Asad Aftab
# This is a guess the number game.
import random

guessesTaken = 0

digit_a  = random.randint(1, 9)
digit_b  = random.randint(1, 9)
digit_c  = random.randint(1, 9) 

number = digit_a,digit_b,digit_c
while guessesTaken < 3:
    print('Take a guess for the first digit.') 
    guess_1 = input()
    guess_1 = int(guess_1)

    guessesTaken = guessesTaken + 1

    if guess_1 < digit_a:
        print('Your guess is too low for the first digit.') 

    if guess_1 > digit_a:
        print('Your guess is too high for the first digit.')

    if guess_1 == digit_b or guess_1 == digit_c:
		print('The digit\'s right but the placement is wrong!')
	
	if guess_1 == digit_a:
		break
	
while guessesTaken < 3:
    print('Take a guess for the second digit.')
	guess_2 = input()
    guess_2 = int(guess_2)
	
	guessesTaken = guessesTaken + 1
	
	if guess_2 < digit_2:
		print('Your guess is too low for the second digit')
	
	if guess_2 > digit_2:
		print('The guess is too high for the second digit')
		
	if guess_2 == digit_a or guess_2 == digit_c:
		print('Your digit\'s right but the placement is wrong!')
		
	if guess_2 == digit_b:
		break
	
while guessesTaken < 3:
	print('Take a guess for the second digit.')	
	guess_3 = input()
    guess_3 = int(guess_3)
	
	if guess_3 < digit_c:
		print('Your guess is too low for the third digit.') 
	
	if guess_3 > digit_C:
		print('your guess is too high for the third digit')
	
	if guess_3 == digit_a or guess_3 == digit_b:
		print('Your digit\'s right but the placement is wrong!')
	
	if guess_3 == digit_c:
		break

	guess = guess_1,guess_2,guess_3
	
if guess == number:
	guessesTaken = str(guessesTaken)
    print('Good job! You guessed the number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('You lose! The number I was thinking of was ' + number)