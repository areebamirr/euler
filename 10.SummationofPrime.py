
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

n = 200000  # 2 millions    

sum = 2000000
i = 1
while i < n:
    if prime(i):
        sum += i
    i += 1

print(sum)


