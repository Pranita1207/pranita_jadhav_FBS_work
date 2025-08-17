num=int(input('Enter the number:'))
sum_div=0
for i in range(1, num):
    if num % i == 0:
        sum_div += i
print(num,'is perfect'if sum_div == num else 'Is not perfect')