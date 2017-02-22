sentence = input("enter a sentence")
list_of_words = sentence.split()
print("there are", len(list_of_words), "words.")
print(list_of_words)
sum = 0
for word in list_of_words:
    sum = sum + len(word)

print("the average word length is", sum/len(list_of_words) )