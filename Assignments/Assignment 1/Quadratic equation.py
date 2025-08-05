a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
c=int(input("Enter number 3:"))

sqrt=((b**2) - (4*a*c))**0.5

res1=(-b+sqrt) / 2*a
res2=(-b-sqrt) / 2*a

print(f'Roots of Quadratic Equation {res1} & {res2}')
