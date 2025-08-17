n=int(input('Enter the number of students:'))
total_avg= 0
for i in range(n):
    print(f'student{i+1}')
    total=0
    for j in range(5):
        marks=int(input(f"Enter marks of subject {j+1}:"))
        total += marks
    percent = total / 5
    print('percentage',{percent})
    total_avg += percent
        
print(f'Average Percentage of class:',{total_avg})