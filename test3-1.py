number = int(input("n = "))

for i in range(1, number+1):
    for j in range(i):
        print("*", end="")
    print()