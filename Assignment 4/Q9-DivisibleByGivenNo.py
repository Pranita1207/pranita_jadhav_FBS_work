start=int(input('Enter the start number:'))
end=int(input('Enter the end number:'))
div=int(input('Enter the divisor'))
print('Numbers divisible by',{div} )
for i in range(start,end+1):
    if i % div == 0:
        print(i, end=' ')