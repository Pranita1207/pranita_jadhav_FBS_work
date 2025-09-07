##Find the Second Largest Number in a List Using Bubble Sort

numbers = [10, 20, 4, 45, 99, 65]

for i in range(len(numbers)):
    for j in range(len(numbers)-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print("Sorted List:", numbers)
print("Second Largest Number:", numbers[-2])

