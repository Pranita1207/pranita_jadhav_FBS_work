##Replace Every Blank Space with Hyphen

string = "welcome to python programming"

new_string = ""
for ch in string:
    if ch == " ":
        new_string += "-"
    else:
        new_string += ch

print("Original:", string)
print("Modified:", new_string)

