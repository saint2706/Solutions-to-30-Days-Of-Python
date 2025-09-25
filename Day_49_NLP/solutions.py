import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# --- NLP Text Vectorization Example ---

# 1. Sample Corpus
# A corpus is a collection of text documents.
corpus = [
    "The quick brown fox jumped over the lazy dog.",
    "The dog was not lazy.",
    "The fox is quick."
]

print("--- NLP Vectorization Demo ---")
print("Sample Corpus:")
for doc in corpus:
    print(f"- '{doc}'")
print("-" * 30)


# --- Method 1: Bag-of-Words with CountVectorizer ---
print("\n--- 1. Bag-of-Words (CountVectorizer) ---")
# Create an instance of CountVectorizer
# It automatically handles tokenization and lowercasing.
count_vectorizer = CountVectorizer()

# Fit the vectorizer to the corpus and transform the corpus into a document-term matrix
X_count = count_vectorizer.fit_transform(corpus)

# The vocabulary (the set of unique words)
print("Vocabulary (Feature Names):")
print(count_vectorizer.get_feature_names_out())

# The resulting document-term matrix (in a dense format for readability)
# Each row is a document, each column is a word in the vocabulary.
# The values are the word counts.
df_count = pd.DataFrame(X_count.toarray(), columns=count_vectorizer.get_feature_names_out())
print("\nDocument-Term Matrix (Counts):")
print(df_count)
print("This matrix shows the count of each word in each document.")
print("-" * 30)


# --- Method 2: TF-IDF with TfidfVectorizer ---
print("\n--- 2. TF-IDF (TfidfVectorizer) ---")
# Create an instance of TfidfVectorizer
# It also handles tokenization and lowercasing.
tfidf_vectorizer = TfidfVectorizer()

# Fit and transform the corpus
X_tfidf = tfidf_vectorizer.fit_transform(corpus)

# The vocabulary is the same as before
print("Vocabulary (Feature Names):")
print(tfidf_vectorizer.get_feature_names_out())

# The resulting TF-IDF matrix
# The values are the TF-IDF scores, not raw counts.
# Notice how common words like 'the' have lower scores than more specific words.
df_tfidf = pd.DataFrame(X_tfidf.toarray(), columns=tfidf_vectorizer.get_feature_names_out())
print("\nTF-IDF Matrix:")
print(df_tfidf.round(2)) # Round for better readability
print("This matrix shows the TF-IDF score for each word, highlighting important words.")
print("-" * 30)