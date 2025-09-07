##WAP to find the second largest element in list

numbers=[10,20,30,40]

second_largest=numbers[0]
largest=numbers[0]

for i in numbers:
    if i > largest:
        second_largest=largest
        largest=i
    elif i > second_largest:
        second_largest=i
        
print("Second Largest Number is:", second_largest)