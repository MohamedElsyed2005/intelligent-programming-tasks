# src/recommender.py (نسخة بدون surprise - باستخدام sklearn)

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from collections import defaultdict
import os

def create_user_item_matrix(df):
    """
    Pivot ratings dataframe to user-item matrix.
    Rows = users, Columns = items (movies)
    """
    return df.pivot_table(index='user_id', columns='movie_id', values='rating').fillna(0)

def compute_similarity(matrix, kind='user'):
    """
    Compute cosine similarity between users or items.
    kind: 'user' or 'item'
    """
    if kind == 'user':
        sim = cosine_similarity(matrix)
        return pd.DataFrame(sim, index=matrix.index, columns=matrix.index)
    elif kind == 'item':
        sim = cosine_similarity(matrix.T)
        return pd.DataFrame(sim, index=matrix.columns, columns=matrix.columns)
    else:
        raise ValueError("kind must be 'user' or 'item'")

def predict_rating_user_based(user_id, item_id, ratings_matrix, user_similarity):
    """
    Predict a rating for a given user and item using user-based CF
    """
    if item_id not in ratings_matrix.columns:
        return np.nan

    sims = user_similarity[user_id]
    item_ratings = ratings_matrix[item_id]
    mask = item_ratings > 0
    if mask.sum() == 0:
        return np.nan

    weighted_ratings = (sims[mask] * item_ratings[mask]).sum()
    sim_sum = sims[mask].sum()

    return weighted_ratings / sim_sum if sim_sum != 0 else np.nan

def predict_rating_item_based(user_id, item_id, ratings_matrix, item_similarity):
    """
    Predict a rating for a given user and item using item-based CF
    """
    if item_id not in item_similarity.columns or user_id not in ratings_matrix.index:
        return np.nan

    user_ratings = ratings_matrix.loc[user_id]
    sim_scores = item_similarity[item_id]
    mask = user_ratings > 0

    if mask.sum() == 0:
        return np.nan

    weighted_ratings = (sim_scores[mask] * user_ratings[mask]).sum()
    sim_sum = sim_scores[mask].sum()

    return weighted_ratings / sim_sum if sim_sum != 0 else np.nan

def get_top_n_recommendations(user_id, ratings_matrix, similarity_matrix, kind='user', n=10):
    """
    Generate top-N recommendations for a user
    """
    predictions = {}
    for item_id in ratings_matrix.columns:
        if ratings_matrix.loc[user_id, item_id] == 0:
            if kind == 'user':
                pred = predict_rating_user_based(user_id, item_id, ratings_matrix, similarity_matrix)
            else:
                pred = predict_rating_item_based(user_id, item_id, ratings_matrix, similarity_matrix)
            if not np.isnan(pred):
                predictions[item_id] = pred

    sorted_preds = sorted(predictions.items(), key=lambda x: x[1], reverse=True)
    return sorted_preds[:n]

def save_top_n_all_users(ratings_matrix, similarity_matrix, kind='user', n=10, out_path='../results/top_n_recommendations.csv'):
    """
    Generate top-N recommendations for all users and save to CSV
    """
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    rows = []
    for user_id in ratings_matrix.index:
        top_n = get_top_n_recommendations(user_id, ratings_matrix, similarity_matrix, kind=kind, n=n)
        for item_id, pred_rating in top_n:
            rows.append({"user_id": user_id, "movie_id": item_id, "predicted_rating": pred_rating})

    df_out = pd.DataFrame(rows)
    df_out.to_csv(out_path, index=False)
    print(f"Saved recommendations to {out_path}")
