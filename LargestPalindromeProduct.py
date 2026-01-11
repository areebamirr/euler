
# 11/01/2026

def palindrome(n):
    temp = n
    rev = 0
    remainder = 0

    while n > 1:
        remainder = int(n % 10)
        rev = rev*10 + remainder
        n /= 10

    if rev == temp:
        return True
    else:
        return False

max_Palindrome = 100 * 100
for i in range(100, 1000):
    for j in range(100, 1000):
        if palindrome(i*j):
            max_Palindrome = max(max_Palindrome, i*j)

print(max_Palindrome)

# OUTPUT: 906609
# Correct: 906609






