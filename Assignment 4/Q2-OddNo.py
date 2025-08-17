num=int(input("Enter the number:"))
for num in range(1, num+1,2):
    if(num % 1 == 0):
        print(num, end=' ')
    print(f' is an odd number')