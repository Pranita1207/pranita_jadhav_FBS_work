words = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagram_groups = {}

for word in words:
    key = ''.join(sorted(word))
    
    if key not in anagram_groups:
        anagram_groups[key] = []
    anagram_groups[key].append(word)
    
result = list(anagram_groups.values())
print("Grouped Anagrams:",result)