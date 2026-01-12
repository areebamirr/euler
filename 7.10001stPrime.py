
def prime(n):
    if n <= 1:
        return False
    factor = 0
    for i in range(1, n + 1):
        if n % i == 0:
            factor += 1
    if factor == 2:
        return True
    else:
        return False

number = 1
i = 0
while True:
    number += 1
    if prime(number):
        print(i)
        i += 1
        if i == 10001:
            print(number)
            break
# OUTPUT: 104743
# CORRECT: 104743
