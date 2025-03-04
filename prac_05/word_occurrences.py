"""
Word Occurrences
Estimate: 20 minutes
Actual:   25 minutes
"""

# Ask the user for a string input
text = input("Enter a string: ")

# Split the text into words (split by spaces)
words = text.split()

# Dictionary to store word counts
word_counts = {}

# Count the occurrences of each word
for word in words:
    word = word.lower()  # Make the word lowercase to be case-insensitive
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Find the longest word for formatting
max_word_length = max(len(word) for word in word_counts)

# Print the word counts, aligned properly
for word in sorted(word_counts.keys()):
    print(f"{word:{max_word_length}} : {word_counts[word]}")
