strings = ["flower", "flow", "flight"]

prefix = strings[0]

for s in strings[1:]:
    while not s.startswith(prefix):
        prefix = prefix[:-1] 
        if prefix == "":
            break

print("Longest common prefix:", prefix)

