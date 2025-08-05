age1 = int(input("Enter the age of 1st person: "))
age2 = int(input("Enter the age of 2nd person: "))
age3 = int(input("Enter the age of 3rd person: "))
age4 = int(input("Enter the age of 4th person: "))
age5 = int(input("Enter the age of 5th person: "))

ticket_amt = int(input("Enter the amount of ticket: "))

if age1 <= 12:
    dis_amt = ticket_amt * 0.3
    amt1 = ticket_amt - dis_amt
elif age1 >= 59:
    dis_amt = ticket_amt * 0.5
    amt1 = ticket_amt - dis_amt
else:
    amt1 = ticket_amt
print(f'The money need to pay for 1st person: {amt1}')

if age2 <= 12:
    dis_amt = ticket_amt * 0.3
    amt2 = ticket_amt - dis_amt
elif age2 >= 59:
    dis_amt = ticket_amt * 0.5
    amt2 = ticket_amt - dis_amt
else:
    amt2 = ticket_amt
print(f'The money need to pay for 2nd person: {amt2}')

if age3 <= 12:
    dis_amt = ticket_amt * 0.3
    amt3 = ticket_amt - dis_amt
elif age3 >= 59:
    dis_amt = ticket_amt * 0.5
    amt3 = ticket_amt - dis_amt
else:
    amt3 = ticket_amt
print(f'The money need to pay for 3rd person: {amt3}')

if age4 <= 12:
    dis_amt = ticket_amt * 0.3
    amt4 = ticket_amt - dis_amt
elif age4 >= 59:
    dis_amt = ticket_amt * 0.5
    amt4 = ticket_amt - dis_amt
else:
    amt4 = ticket_amt
print(f'The money need to pay for 4th person: {amt4}')

if age5 <= 12:
    dis_amt = ticket_amt * 0.3
    amt5 = ticket_amt - dis_amt
elif age5 >= 59:
    dis_amt = ticket_amt * 0.5
    amt5 = ticket_amt - dis_amt
else:
    amt5 = ticket_amt
print(f'The money need to pay for 5th person: {amt5}')