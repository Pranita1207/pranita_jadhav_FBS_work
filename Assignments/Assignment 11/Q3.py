##Sort the List According to the Second Element in Sublist

list1 = [[1, 2], [3, 3], [2, 1]]
list1.sort(key=lambda x: x[1])

print("Sorted List:", list1)
