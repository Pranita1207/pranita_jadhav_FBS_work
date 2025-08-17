num=int(input("Enter the number:"))
temp=num
sum_fact=0
while temp > 0:
    d=temp % 10
    fact = 1
    for i in range (1, d+1):
        fact *= i
    sum_fact += fact
    temp //=10
print(num,'is strong' if sum_fact == num else 'is not strong')