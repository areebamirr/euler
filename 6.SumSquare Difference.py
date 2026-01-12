

sumSquare = 0
squareSum = 0

n = 100

for i in range(1, n+1):
    sumSquare += i**2

for i in range(1, n+1):
    squareSum += i

squareSum = squareSum*squareSum

print(squareSum-sumSquare)

# OUTPUT : 25164150
# CORRECT : 25164150
