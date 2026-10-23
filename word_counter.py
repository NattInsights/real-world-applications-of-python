import re
paragraph = input("Enter your paragraph: ")

word_count = len(paragraph.split())
unique_words = {word for word in re.split(r'[\s.,!?;:]+', paragraph.lower().strip()) if word}
top_common_words = [word for word in re.split(r'[\s.,!?;:]+', paragraph.lower().strip()) if word]
print(unique_words)