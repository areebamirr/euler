

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
n = 20
min_multiple = 0
while n >= 1:
    if all(n % i == 0 for i in range(1,21)):
        min_multiple = n
        break
    n += 1

print(min_multiple)

# OUTPUT: 232792560
# ANSWER: 232792560
