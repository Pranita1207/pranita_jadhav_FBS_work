n=int(input("Enter number of terms:"))
s=0
for i in range(n):
    s += 2**i
print('Sum is=',s)