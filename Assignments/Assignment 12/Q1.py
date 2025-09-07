##Replace all occurrences of 'a' with '$' in a String

string = "bananas are amazing"

new_string = ""
for ch in string:
    if ch == 'a':
        new_string += '$'
    else:
        new_string += ch

print("Original String:", string)
print("Modified String:", new_string)
