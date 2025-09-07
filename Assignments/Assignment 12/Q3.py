##Detect if Two Strings are Anagrams

str1 = "listen"
str2 = "silent"

# Sort both strings and compare
if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not Anagram")

