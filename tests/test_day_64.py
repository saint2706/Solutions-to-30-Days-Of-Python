import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day_64_Modern_NLP_Pipelines import solutions as day64


@pytest.fixture
def mini_corpus():
    corpus = [
        "Responsible AI requires transparency in deployments.",
        "Contemporary NLP leverages transformers and retrieval.",
        "Classical pipelines rely on deterministic tokenization.",
    ]
    labels = [1, 1, 0]
    tokens = day64.tokenize_corpus(corpus)
    embeddings = day64.build_embedding_table(tokens, embedding_dim=4)
    doc_vectors = day64.document_embeddings(tokens, embeddings)
    return {
        "corpus": corpus,
        "labels": labels,
        "tokens": tokens,
        "embeddings": embeddings,
        "doc_vectors": doc_vectors,
    }


def test_tokenization_and_embeddings_are_deterministic(mini_corpus):
    tokens = mini_corpus["tokens"]
    assert tokens[0][0] == "responsible"
    embeddings_again = day64.build_embedding_table(tokens, embedding_dim=4)
    for token in {tok for doc in tokens for tok in doc}:
        np.testing.assert_allclose(mini_corpus["embeddings"][token], embeddings_again[token])


def test_fine_tune_transformer_learns_signal(mini_corpus):
    doc_vectors = mini_corpus["doc_vectors"]
    labels = mini_corpus["labels"]
    model, history = day64.fine_tune_transformer(doc_vectors, labels, epochs=150, lr=0.2)
    assert history.losses[0] > history.losses[-1]
    predictions = model.predict(doc_vectors)
    assert predictions.sum() >= 2


def test_rag_and_evaluation_use_retrieved_docs(mini_corpus):
    corpus = mini_corpus["corpus"]
    doc_vectors = mini_corpus["doc_vectors"]
    embeddings = mini_corpus["embeddings"]
    rag_output = day64.rag_generate("transparency transformers", corpus, doc_vectors, embeddings, top_k=2)
    assert "Sources" in rag_output
    metrics = day64.evaluate_generation(corpus[0], rag_output)
    assert metrics["overlap"] > 0
    assert metrics["f1"] <= 1.0
