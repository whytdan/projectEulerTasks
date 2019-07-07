import math

def find_factors(n):
    factors = list()
    for factor in range(1, int(math.sqrt(n)) + 1):
        if n%factor == 0:
            factors.append(factor)
            factors.append(n // factor)
    return factors


def is_prime(n):
    return len(find_factors(n)) == 2
    

allFactors = find_factors(600851475143)
largestPrime = 0
for factor in allFactors:
    if is_prime(factor) and factor > largestPrime:
        largestPrime = factor

print(largestPrime)



