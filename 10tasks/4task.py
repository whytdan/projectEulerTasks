def is_palindrome(n):
    return str(n) == str(n)[::-1]

palindromes=[]

for first_num in range(100,1000):
    for second_num in range(100,1000):
        item = first_num*second_num
        if is_palindrome(item):
            palindromes.append(item)

print(max(palindromes))