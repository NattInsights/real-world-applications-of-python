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

# sorting
top_5_common = sorted(top_common_words.items(), key=lambda item: item[1], reverse=True)
top_5_common = top_5_common[:5]

print(top_5_common)