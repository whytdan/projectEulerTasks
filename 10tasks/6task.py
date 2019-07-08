sum_of_the_squares = [i**2 for i in range(1, 101)]
square_of_the_sum = [i for i in range(1, 101)]

ans1 = sum(sum_of_the_squares)
ans2 = (sum(square_of_the_sum)) ** 2

print(ans2-ans1)
