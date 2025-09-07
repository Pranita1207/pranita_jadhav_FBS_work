## Print all numbers divisible by m and n in the list

numbers=[12,18,24,30,45,60]
m=int(input("Enter the value of m:"))
n=int(input("Enter the value of n:"))
result = []

for i in numbers:
    if i % m == 0 and i % n == 0:
        result.append(i)
        
print("Numbers divisible by",m ,'and', n, '=',result)