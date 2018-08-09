"""
Even Fibonacci numbers

https://projecteuler.net/problem=2

Each new term in the Fibonacci sequence is generated 
by adding the previous two terms. By starting with 1 and 2, 
the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values 
do not exceed four million, find the sum of the even-valued terms.
"""

s = 2
pprev = 1
prev = 2
cur = 0

while prev < 4000000:
	cur = prev + pprev
	
	if cur % 2 == 0:
		s += cur

	pprev = prev
	prev = cur

print(s)