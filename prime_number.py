def prime_number(num):
    if(number < 2):
        return True
    for i in range(2, num):
        if(num%i == 0):
            return False
    return True 

number = int(input("n = "))

print(number, " -> ", end="")
for i in range(2, number+1):
    if(prime_number(i)):
        print(i,"", end="")
