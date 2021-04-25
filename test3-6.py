number = int(input("n = "))

row = 2*number-1

for i in range(number):
    print("A"*(number-1-i), end="")
    print("+", end="")
    remain = row-2*(number-1-i)-1
    if(remain > 0):
        print("E"*(remain-1), end="")
        print("+", end="")
    print("B"*(number-1-i), end="")
    print()

for i in range(1, number+1, 1):
    if(i == 1): continue
    print("C"*(i-1), end="")
    print("+", end="")
    remain = row-(2*i-1)
    if(remain > 0):
        print("E"*(remain-1), end="")
        print("+", end="")
    print("D"*(i-1), end="")
    print()

