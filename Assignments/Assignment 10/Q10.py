 ##Remove all occurences of a given element
  
numbers=[10,20,30,40,50]
x=int(input("Enter the number to remove:"))
new_list=[]
for i in numbers:
    if i != x:
        new_list.append(i)
        
print("List after removing", x, "=", new_list)
        