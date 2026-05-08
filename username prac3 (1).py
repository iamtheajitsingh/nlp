import re
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Sample text
text = "Natural Language Processing is amazing. Language models learn patterns from text data."

# 1. Tokenize words (only alphabetic)
tokens = word_tokenize(text.lower())
words = [w for w in tokens if w.isalpha()]

# 2. Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [w for w in words if w not in stop_words]

# 3. Count frequencies
freq = Counter(filtered_words)

# 4. Show most common words
print(freq.most_common())
