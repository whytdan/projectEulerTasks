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

counter = 1
num = 1
while counter < 10001:
    num+=2
    if is_prime(num):
        counter += 1
print(num)