words = ["apple", "banana", "apple", "orange", "banana", "apple"]

unique_words = set(words)  
print("Unique words:", unique_words)

for word in unique_words:
    print(word, "occurs", words.count(word), "times")
