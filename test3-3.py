number = int(input("n = "))

for i in range(number):
    for j in range(1, 2*number):
        if(j == number-i or j == number+i):
            print("*", end="")
        else:
            print(" ", end="")
    print()