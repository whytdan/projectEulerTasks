def is_divisible(n):
    for i in [3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19]:
        if n%i!=0:
            return False
    return True


def smallest_multiple(n):
    while True:
        if is_divisible(n):
            return n
            break
        n+=20

