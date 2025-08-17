num=int(input("Enter the number:"))
s=str(num)
power=len(s)
total=sum(int(digit)** power for digit in s)
if total ==num:
    print(num,' is an Armstrong Number.')
else:
    print(num,'is not an Armstrong Number.')