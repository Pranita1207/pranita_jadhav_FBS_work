n=int(input("Enter the number of Passengers:"))
ticket=int(input("Enter per ticket cost:"))
total=0
for i in range(n):
    age=int(input(f"Enter the age of passenger {i+1}:"))
    if age < 12 :
        total += ticket * 0.7
    elif age > 59:
        total += ticket ** 0.5
    else:
        total += ticket
        
print(f'Total ticket amount:',{total})