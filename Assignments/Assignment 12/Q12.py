##Count Number of Lowercase Characters

string = "PyThon ProGram"

count = 0
for ch in string:
    if ch.islower():
        count += 1

print("Lowercase characters:", count)


