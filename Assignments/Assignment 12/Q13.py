##Count Number of Digits and Letters

string = "Python123"

letters = 0
digits = 0
for ch in string:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1

print("Letters:", letters)
print("Digits:", digits)
