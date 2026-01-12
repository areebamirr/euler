# Special Pythagorean Triplet

# My solutions TC: O(n^3)
for c in range(1000):
    for b in range(c):
        for a in range(b):
            if a**2 + b**2 == c**2:
                if a+b+c == 1000:
                    print(a*b*c)
                    break

# Better Optimized Solutions TC: O(n^2)
for a in range(1, 1000):
    for b in range(a+1, 1000-a):
        c = 1000 -a-b
        if c <= b:
            continue
        if a*a + b*b == c*c:
            print(a*b*c)
            break

# Mathematical optimization TC: O(n)   This is alittle bit complex
for m in range(2, int(500**0.5)+1):
    if 500 % m == 0:
        n = 500 // m - m
        if n > 0 and n < m:
            a = m*m - n*n
            b = 2*m*n
            c = m*m + n*n
            print(a*b*c)

# OUTPUT : 31875000
# ANSWER : 31875000


