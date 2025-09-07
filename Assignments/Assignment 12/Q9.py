##alculate Number of Words and Characters in a String

string = "python is fun"

char_count = 0
for ch in string:
    char_count += 1

word_count = 1
for ch in string:
    if ch == " ":
        word_count += 1

print("Characters:", char_count)
print("Words:", word_count)
