num=int(input("Enter the terms:"))
a=0
b=1
for i in range(num):
    c=a+b
    print(c,end=' ')
    a=b
    b=c

    