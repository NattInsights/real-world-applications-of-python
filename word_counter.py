import re
paragraph = input("Enter your paragraph: ")

word_count = len(paragraph.split())
unique_words = {word for word in re.split(r'[\s.,!?;:]+', paragraph.lower().strip()) if word}
words = [word for word in re.split(r'[\s.,!?;:]+', paragraph.lower().strip()) if word]

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

final_output = f"Word count: {word_count}\n" + f"Unique words: {unique_words}\n" + f"Top 5 common words: {[x[0] for x in top_5_common]}"
print(final_output)
# OUTPUT CAN BE CLEANER, REMOVE TYPE INCLUSION