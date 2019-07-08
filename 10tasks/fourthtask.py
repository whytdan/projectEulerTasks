def is_palindrome(n):
    return str(n) == str(n)[::-1]

palindromes=[]

def find_largest_palindrome(hundred1, hundred2, thousand1, thousand2):
    for first_num in range(hundred1, thousand1):
        for second_num in range(hundred2, thousand2):
            item = first_num*second_num
            if is_palindrome(item):
                palindromes.append(item)
    return max(palindromes)
