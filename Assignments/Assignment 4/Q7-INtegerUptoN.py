n=int(input("Enter the n:"))
print('Numbers not divisble by 2 and 3')
for i in range(1, n+1):
    if i % 2 != 0 and 1 % 3 != 0:
        print(i, end=' ')
       