#WAP to swap two numbers without using third variable

x=int(input("Enter number 1:"))
y=int(input("Enter number 2:"))

print(f'before swap x={x},y={y}')
x=x+y
y=x-y
x=x-y
# trick (x,y=y,x)

print(f'after swap x={x}, y={y}')