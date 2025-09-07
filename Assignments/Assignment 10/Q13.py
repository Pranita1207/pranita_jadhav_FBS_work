## print list after removing even numbers

numbers=[2,3,4,5,6,7,8]
odd_list=[]
for i in numbers:
    if i % 2 != 0:
        odd_list.append(i)
        
print("After removing even numbers",odd_list) 