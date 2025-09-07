##Count Occurrences of Each Word

string = "python is easy and python is powerful"
words = string.split()

count_dict = {}
for word in words:
    if word in count_dict:
        count_dict[word] += 1
    else:
        count_dict[word] = 1

print("Word Occurrences:", count_dict)


