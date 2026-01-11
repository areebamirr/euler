
# 11/01/2026
# Sum of odd square number
n = int(input().strip())

sum = 0
for i in range(n):
    if (i**2) % 2 != 0:
        sum += i**2

print(sum)
