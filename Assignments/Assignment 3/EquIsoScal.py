## WAP to check whether the triangle is equilateral, isosceles or scalene.

side1=int(input("Enter the angle 1:"))
side2=int(input("Enter the angle 2:"))
side3=int(input("Enter the angle 3:"))

if(side1==side2)and(side2==side3)and(side3==side1):
   print(f'triangle is equilateral')

elif(side1==side2):
   print(f'Triangle is Isoscales')

else:
   print(f'triangle is scalene')