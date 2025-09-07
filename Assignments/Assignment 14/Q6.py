numbers = [2, 5, 1, 7, 3, 9]

max_product = float('-inf')
pair = ()

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        product = numbers[i] * numbers[j]
        if product > max_product:
            max_product = product
            pair = (numbers[i], numbers[j])

print("Pair with maximum product:", pair, "Product:", max_product)

