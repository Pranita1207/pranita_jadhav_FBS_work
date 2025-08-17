num=int(input("Enter the value of n:"))
a=0
b=1
i=1
while(i<=num):
    c=a+b
    print(c)
    a=b
    b=c
    i+=1