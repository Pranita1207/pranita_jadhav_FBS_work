def sum_factorials(n):
    fact=1
    s=0
    for i in range(1, n+1):
        fact *=i
        s+= fact
        return s
n=int(input("Enter n:"))    
print('Sum of factorials:',sum_factorials(n))