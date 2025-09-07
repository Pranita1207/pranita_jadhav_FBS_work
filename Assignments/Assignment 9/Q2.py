##Check Armstrong number using recursion

def power(x, y):
    if y == 0:
        return 1
    return x * power(x, y-1)

def armstrong(num, digits):
    if num == 0:
        return 0
    return power(num % 10, digits) + armstrong(num // 10, digits)

n = int(input("Enter number: "))
digits = len(str(n))

if n == armstrong(n, digits):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
