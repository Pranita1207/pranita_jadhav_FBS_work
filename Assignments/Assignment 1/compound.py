P=int(input("Enter number 1:"))
R=int(input("Enter number 2:"))
T=int(input("Enter number 3:"))

compound= (P*(1 + (R/100)) **T)-P

print(f'Compound intrest is {compound}')