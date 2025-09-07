##Remove the nth Index Character from a Non-Empty String

string = "python"
n = 2  

new_string = ""
for i in range(len(string)):
    if i != n:
        new_string += string[i]

print("Original String:", string)
print("After removing index", n, ":", new_string)

