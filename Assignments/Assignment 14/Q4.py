numbers = [2, 4, 3, 5, 7, 8, 1]
target = 9

pairs = set()

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            pairs.add((numbers[i], numbers[j]))

print("Pairs with sum", target, ":", pairs)
