gender = input("Enter the Gender (M/F): ")
age = int(input("Enter the Age: "))

if (gender == "M" and age >= 21) or (gender == "F" and age >= 18):
    print(f"Gender is {gender} and age is {age}, Then eligible for marriage")
else:
    print(f"Gender is {gender} and age is {age}, Then not eligible for marriage")