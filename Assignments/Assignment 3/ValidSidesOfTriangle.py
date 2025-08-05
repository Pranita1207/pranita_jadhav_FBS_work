##WAP to input all sides of triangle and check wheteher triangle is valid or not.

S1=int(input("Enter the side 1:"))
S2=int(input("Enter the side 2:"))
S3=int(input("Enter the side 3:"))

if(S1+S2>S3)and(S2+S3>S1)and(S3+S1<S2):
  print(f'Triangle is valid')
  
else:
    print(f'Triangle is not valid')