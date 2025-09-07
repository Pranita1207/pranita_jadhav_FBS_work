##Remove Characters of Odd Index Values

string = "python"

new_string = ""
for i in range(len(string)):
    if i % 2 == 0:  
        new_string += string[i]

print("Original String:", string)
print("Modified String:", new_string)
