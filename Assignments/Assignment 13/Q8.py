## python program to count the frequency of words appearing in a string using dictionary:

str="This is bed. That is only for sleeping"

words=str.split()        ## split string into words for counting
word_count={}            ## Create an empty dict for storing result

for word in words:
    if word in word_count:
        word_count[word] +=1
    else:
        word_count[word]=1
print(word_count)