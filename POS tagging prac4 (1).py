from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Sample documents
docs = [
    "Natural Language Processing guidelines for students",
    "Department of Computer Science publishes guidelines",
    "NLP models learn from text data"
]

# 1. Initialize TF-IDF Vectorizer
vectorizer = TfidfVectorizer(stop_words='english')

# 2. Fit and transform documents
tfidf_matrix = vectorizer.fit_transform(docs)

# 3. Convert to DataFrame for readability
df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())

print(df)
