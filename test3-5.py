import math
number = int(input("n = "))

row = math.ceil(number/2)
for i in range(row):
    for j in range(1, row+2*i+1):
        if(j >= row-i and j <= row+i):
            print("*", end="")
        else:
            print(" ", end="")
    print()

for i in range(row):
    if(number%2 != 0 and i == 0):
        continue
    for j in range(number-i):
        if(number%2 == 0): number-=1
        if(j >= i and j <= number-i and j < number):
            print("*", end="")
        else:
            print(" ", end="")
    print()
