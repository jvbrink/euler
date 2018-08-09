"""
Largest prime factor

https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

def prime_factors(n):
	factors = []
	while n > 1:
		for d in range(2, n+1):
			if n % d == 0:
				factors.append(d)
				n //= d
				break

	return factors

print(prime_factors(13195))
print(prime_factors(600851475143))
