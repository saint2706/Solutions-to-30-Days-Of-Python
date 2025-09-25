# Day 49: Natural Language Processing (NLP)

Welcome to Day 49! Today, we focus on **Natural Language Processing (NLP)**, a field of AI that enables computers to understand, interpret, and generate human language. We will cover some fundamental concepts and techniques for turning text into numerical data that machine learning models can process.

## Key Concepts

### What is NLP?
NLP is all about the interaction between computers and human language. It involves tasks like sentiment analysis (which we saw with RNNs), language translation, text summarization, and question answering. A key challenge in NLP is converting unstructured text data into a structured numerical format.

### 1. Text Preprocessing
Before feeding text to a model, it needs to be cleaned and standardized. Common steps include:
-   **Tokenization:** Breaking down text into individual words or subwords (tokens).
-   **Lowercasing:** Converting all text to lowercase.
-   **Stop Word Removal:** Removing common words (like "the", "is", "a") that don't carry much meaning.
-   **Stemming/Lemmatization:** Reducing words to their root form (e.g., "running" -> "run").

### 2. Text Vectorization
This is the process of converting text tokens into numerical vectors.

-   **Bag-of-Words (BoW):** Represents text by the frequency of words it contains. It ignores grammar and word order.
    -   **CountVectorizer:** A simple BoW approach that counts the occurrences of each word.

-   **TF-IDF (Term Frequency-Inverse Document Frequency):** An improvement over BoW. It weighs words not only by their frequency in a document but also by how rare they are across all documents in the corpus. This gives higher importance to words that are more specific to a document.
    -   **Term Frequency (TF):** `(Number of times term appears in a document) / (Total number of terms in the document)`
    -   **Inverse Document Frequency (IDF):** `log(Total number of documents / Number of documents with term)`
    -   **TF-IDF Score:** `TF * IDF`

-   **Word Embeddings (like Word2Vec, GloVe):** Dense vector representations of words where similar words have similar vector representations. We saw this in action with the `Embedding` layer in the previous lesson. These are powerful because they capture semantic relationships between words.

---

## Practice Exercise

-   The `solutions.py` file demonstrates how to use `scikit-learn` to perform basic text vectorization.
-   The code covers:
    1.  Creating a small corpus of text documents.
    2.  Using `CountVectorizer` to create a Bag-of-Words representation of the text.
    3.  Using `TfidfVectorizer` to create a TF-IDF representation.
    4.  Showing the resulting document-term matrices and feature names (the vocabulary).

Review the code to understand these fundamental techniques for converting text into a machine-readable format.