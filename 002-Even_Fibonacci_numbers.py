'''
Even Fibonacci numbers

Each new term in the Fibonacci sequence is generated by 
adding the previous two terms. By starting with 1 and 2, 
the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose 
values do not exceed four million, find the sum of the 
even-valued terms.
'''

'''
Fibonacci is i = i-1 + i-2
Base cases is 011
neither are divisible by 2 (even) so disregard

start array with 1, 2 and start count at 2 go to 4,000,000

mod by 2 and add to array if even
'''

evenFiboNumber = [2]
Fibonacci = [1,2]

checkNumber = 0

while checkNumber < 4000000:
	length = len(Fibonacci)
	checkNumber = Fibonacci[length-1] + Fibonacci[length-2]
	Fibonacci.append(checkNumber)
	print (checkNumber)
	if checkNumber % 2 == 0:
		evenFiboNumber.append(checkNumber)

total = 0

print (evenFiboNumber)

for number in evenFiboNumber:
	total += number;

print (total)






















