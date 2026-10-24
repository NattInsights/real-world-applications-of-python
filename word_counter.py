import re
paragraph = input("Enter your paragraph: ")

word_count = len(paragraph.split())
words = [word for word in re.split(r'[\s.,!?;:]+', paragraph.lower().strip()) if word]
unique_words = set(words)
top_common_words = {}

# counting each unique word from filtered words
for word in words:
    if word in top_common_words:
        top_common_words[word] += 1
    else:
        top_common_words.update({word: 1})

# sorting in descending order and selecting top 5
top_5_common = sorted(top_common_words.items(), key=lambda item: item[1], reverse=True)[0:5]
# line not needed, filtered above top_5_common = top_5_common[:5]

unique_words_str = ", ".join(sorted(unique_words))
top_5_str = ", ".join(x[0] for x in top_5_common)
final_output = f"Word count: {word_count}\n" + f"Unique words: {unique_words_str}\n" + f"Top 5 common words: {top_5_str}"
print(final_output)
# numbering left for top 5 in final output..