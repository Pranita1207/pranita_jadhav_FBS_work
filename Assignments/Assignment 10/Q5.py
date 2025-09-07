## Accept the number from the user and check if this element is present in the list or not. also tell how many times it presnet in alist

numbers=[2,4,6,8,2,10,2]
n=int(input("Enter the number:"))

count=0
for i in numbers:
    if i == n:
        count += 1
        
if count > 0:
    print(n,"is present", count,"times")
else:
    print(n," is not present")