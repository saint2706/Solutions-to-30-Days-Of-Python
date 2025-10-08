"""Tests for Day 57 recommender system helpers."""

from __future__ import annotations

from Day_57_Recommender_Systems import solutions as day57


def test_user_based_collaborative_filtering_recovers_relevant_items() -> None:
    ratings = day57.build_demo_user_item_matrix(random_state=57)
    scores = day57.user_based_scores(ratings, target_user="A", k_neighbors=2)
    rec = day57.rank_items(scores, top_n=3)
    assert rec.ranked_items[:2] == ["Item3", "Item5"]
    assert rec.scores[0] > rec.scores[1]


def test_svd_factorisation_produces_masked_recommendations() -> None:
    ratings = day57.build_demo_user_item_matrix(random_state=57)
    svd_preds = day57.svd_matrix_factorisation(ratings, n_factors=2)
    masked = day57.mask_known_items(svd_preds.loc["A"], ratings.loc["A"])
    rec = day57.rank_items(masked, top_n=2)
    assert rec.ranked_items == ["Item3", "Item5"]
    assert rec.scores[0] == max(rec.scores)


def test_ranking_metrics_align_across_methods() -> None:
    ratings = day57.build_demo_user_item_matrix(random_state=57)
    target_user = "A"
    user_scores = day57.rank_items(day57.user_based_scores(ratings, target_user, k_neighbors=2), top_n=3)
    svd_scores = day57.rank_items(
        day57.mask_known_items(day57.svd_matrix_factorisation(ratings, 2).loc[target_user], ratings.loc[target_user]),
        top_n=3,
    )
    implicit_scores = day57.rank_items(
        day57.mask_known_items(
            day57.implicit_confidence_matrix((ratings > 3).astype(int)).loc[target_user],
            ratings.loc[target_user],
        ),
        top_n=3,
    )
    relevant = {"Item3", "Item5"}
    precision = day57.precision_at_k(user_scores.ranked_items, relevant, k=3)
    recall = day57.recall_at_k(user_scores.ranked_items, relevant, k=3)
    map_score = day57.mean_average_precision(
        [user_scores.ranked_items, svd_scores.ranked_items, implicit_scores.ranked_items],
        [relevant, relevant, relevant],
        k=3,
    )
    assert precision == recall == 1.0
    assert map_score == 1.0
