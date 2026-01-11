
# 11/01/2026
n = 4000000  # uptil 4 millions 

first = 1
second = 2
third = 0  # Think it as none or we jsut initialized it.

sum = 2

while third < n:
    third = first + second
    if third % 2 == 0:
        sum += third
    first = second
    second = third

print(sum)

# OUPUT : 4613732
# Answer : 4613732
