start=int(input("Enter the start number:"))
end=int(input("Enter the end number:"))
print('Armstrong numbers:')
for num in range(start, end+1):
    order=len(str(num))
    s=0
    temp=num 
    while temp > 0:
        digit = temp % 10
        s += digit ** order
        temp //=10
    if s== num:
        print(num,end=' ')