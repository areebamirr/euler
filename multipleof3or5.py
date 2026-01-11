
# 11/01/2026
n = int(input().strip())

sum = 0
for i in range(n):
    if (i % 5 == 0) or (i % 3 == 0):
        sum += i
    
print(sum)
# INPUT :1000
# OUTPUT :233168
# Answer :233168