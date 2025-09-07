## WAP Remove duplicates from list

numbers=[1,2,3,1,4,2]

unique_list=[]
for i in numbers:
    if i not in unique_list:
        unique_list.append(i)
        
print("List after removing duplicates",unique_list)
    

