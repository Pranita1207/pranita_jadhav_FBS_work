##Count the Number of Vowels in a String

string = "hello world"
vowels = "aeiouAEIOU"

count = 0
for ch in string:
    if ch in vowels:
        count += 1

print("String:", string)
print("Number of vowels:", count)

