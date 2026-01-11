# 11/01/2026

# What is the largest prime factor of the number 600851475143 ?

n = 600851475143

factors = []
divisor = 2

while n > 1:
    while n % divisor == 0:
        if divisor not in factors:
            factors.append(divisor)
        n /= divisor
    divisor = divisor + 1
    
max_factor = int(factors[0])
for i in factors:
    max_factor = max(max_factor, int(i))

print(max_factor)

# OUTPUT : 6857
# ANSWER : 6857


