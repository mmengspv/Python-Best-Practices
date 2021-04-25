number = int(input("n = "))

for i in range(number):
    for j in range(number):
        if(j == i or j == number-i-1):
            print("*", end="")
        else:
            print(" ", end="")
    print()