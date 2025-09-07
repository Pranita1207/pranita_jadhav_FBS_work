## Seprate even and odd element into two lists

numbers=[1,2,3,4,5,6]

even_list=[]
odd_list=[]

for i in numbers:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
        
print("Even numbers",even_list)
print("Odd Numbers:",odd_list)