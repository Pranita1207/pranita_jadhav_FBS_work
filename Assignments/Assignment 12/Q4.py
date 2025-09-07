##Form a New String by Exchanging First and Last Character

string = "python"

# If string length > 1
new_string = string[-1] + string[1:-1] + string[0]

print("Original String:", string)
print("Modified String:", new_string)
