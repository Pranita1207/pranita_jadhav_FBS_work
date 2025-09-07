## python program to generate a dictionary that contains numbers (between 1 and n) in the foem(x,x*x)

n=int(input("Enter the number:"))

squares={x:x*x for x in range(1,n+1)}
print(squares)