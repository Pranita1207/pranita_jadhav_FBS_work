## WAP to find maximum and minimum element of list

numbers=[10,20,30,40]

maximum=numbers[0]
minimum=numbers[0]

for i in numbers:
    if i > maximum:
        maximum=i
    if i < minimum:
        mimimum=i

print("Maximum number",maximum)
print("Minimum Number",minimum)