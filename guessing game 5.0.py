#Author: Asad Aftab 
# This is a guess the number game.
import random

guessesTaken = 0

digit_1  = random.randint(100, 999)

number = digit_1
number_0 = str(number)
digit_a = number_0[0]
digit_b = number_0[1]
digit_c = number_0[2]

print('You have three tries to guess the three digit number!')
print('Good luck!')


while guessesTaken < 3:
	print('Take a guess for the number.') 
	guess = input()
	guess_str = str(guess)
	number_1 = guess_str[0]
	number_2 = guess_str[1]
	number_3 = guess_str[2]
	
	guessesTaken = guessesTaken + 1
	
	if number_1 < digit_a:
		print('Your guess is too low for the first digit.') 

	if number_1 > digit_a:
		print('Your guess is too high for the first digit.')
	
	if number_1 == digit_a:
		print('Your guess for the first digit is right!')
	
	if number_2 < digit_b:
		print('Your guess is too low for the second digit')
	
	if number_2 > digit_b:
		print('The guess is too high for the second digit')
	
	if number_2 == digit_b:
		print('Your guess for the second digit is right!')
	
	if number_3 < digit_c:
		print('Your guess is too low for the third digit.') 
	
	if number_3 > digit_c:
		print('Your guess is too high for the third digit')
	
	if number_3 == digit_c:
		print('Your guess for the third digit is right!')
		break

if guess_str == number_0:
    guessesTaken = str(guessesTaken)
    print('Good job! You guessed the number in ' + guessesTaken + ' tries!')

if guess_str != number_0:
    number = str(number)
    print('You lose! The number I was thinking of was ' + number)