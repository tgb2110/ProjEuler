'''
If we list all the natural numbers below 10 that are 
multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of 
these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

array_of_num = []

for i in range(1000): # iterate over range
    if i % 5 == 0:
        array_of_num.append(i)
        continue
    elif i % 3 == 0:
        array_of_num.append(i)

total = 0

for element in array_of_num: # total up array
	total += element

print (total)