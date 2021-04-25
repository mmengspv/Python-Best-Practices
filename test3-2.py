number = int(input("n = "))

for i in range(number, 0, -1):
    for j in range(1, number+1):
        if(j >= i):
            print("*", end="")
        else:
            print(" ", end="")
    print()