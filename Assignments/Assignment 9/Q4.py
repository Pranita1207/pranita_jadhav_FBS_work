##Sum of n natural numbers using recursion

def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n-1)

n = int(input("Enter n: "))
print("Sum =", sum_n(n))

