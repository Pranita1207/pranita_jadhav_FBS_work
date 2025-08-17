x=int(input("Enter value of x:"))
n=int(input("Enter number of terms:"))
s=0
sign=1
for i in range(1, n+1):
    s += sign * (x**i)/i
    sign *= -1
    print('Sum =',s)