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


summ = 0

for i in range(1, 2000001):
    if is_prime(i):
        summ+=i

print(summ)
