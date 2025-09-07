##Reverse a number using recursion (same as Q3)

def reverse_num(n, rev=0):
    if n == 0:
        return rev
    return reverse_num(n // 10, rev * 10 + n % 10)

n = int(input("Enter number: "))
print("Reversed number:", reverse_num(n))

