# src/evaluation.py

import numpy as np
import pandas as pd

def precision_at_k(recommended_items, relevant_items, k):
    """
    Precision@K = (# of relevant recommended in top K) / K
    """
    recommended_at_k = recommended_items[:k]
    relevant_set = set(relevant_items)
    hit_count = sum([1 for item in recommended_at_k if item in relevant_set])
    return hit_count / k

def recall_at_k(recommended_items, relevant_items, k):
    """
    Recall@K = (# of relevant recommended in top K) / total # of relevant
    """
    relevant_set = set(relevant_items)
    if not relevant_set:
        return 0.0
    recommended_at_k = recommended_items[:k]
    hit_count = sum([1 for item in recommended_at_k if item in relevant_set])
    return hit_count / len(relevant_set)

def evaluate_precision_recall(df, ratings_matrix, similarity_matrix, kind='user', k=10, n_users=100,
                               get_top_n_func=None):
    """
    Evaluate average precision@k and recall@k over sample of users
    """
    from random import sample
    users = list(ratings_matrix.index)
    sampled_users = sample(users, min(n_users, len(users)))

    precision_scores = []
    recall_scores = []

    for user_id in sampled_users:
        user_rated_items = df[df['user_id'] == user_id]['movie_id'].tolist()
        if len(user_rated_items) < 5:
            continue

        train_items = user_rated_items[:len(user_rated_items)//2]
        test_items = user_rated_items[len(user_rated_items)//2:]

        # simulate removing test_items from the matrix
        ratings_matrix_copy = ratings_matrix.copy()
        ratings_matrix_copy.loc[user_id, test_items] = 0

        top_n = get_top_n_func(user_id, ratings_matrix_copy, similarity_matrix, kind=kind, n=k)
        recommended_items = [item for item, _ in top_n]

        precision = precision_at_k(recommended_items, test_items, k)
        recall = recall_at_k(recommended_items, test_items, k)

        precision_scores.append(precision)
        recall_scores.append(recall)

    avg_precision = np.mean(precision_scores)
    avg_recall = np.mean(recall_scores)

    return avg_precision, avg_recall
