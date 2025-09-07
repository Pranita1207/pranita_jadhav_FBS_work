##WAP to reverse a list

numbers=[10,20,30,40,50]
reversed_list= []

for i in range(len(numbers)-1,-1,-1):
    reversed_list.append(numbers[i])
    
print("Reverse list is",reversed_list )