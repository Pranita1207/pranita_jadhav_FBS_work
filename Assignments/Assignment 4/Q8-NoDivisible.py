start=int(input("Enter the start no:"))
end=int(input("Enter the end no:"))
print('number divisble by 7 and multiple by 5')
for i in range(start, end+1):
    if i % 7 == 0 and i % 5 == 0:
        print(i, end=' ')