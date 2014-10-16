'''
Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''

'''
Prime number is divisible by itself and 1 only

so lets factor out all factors first then decide which ones are prime
'''

all_factors = []

number_to_check = 600851475143

for number in range(1, number_to_check, 2):
	if number_to_check % number == 0:
		all_factors.append(number)

print(all_factors)