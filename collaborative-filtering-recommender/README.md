# 📌 Collaborative Filtering Recommendation System

This project implements a **Collaborative Filtering-based Movie Recommendation System** using the **MovieLens 100K** dataset. It supports both **User-Based** and **Item-Based** filtering using **scikit-learn** instead of the Surprise library (to avoid compatibility issues).

---

## ✅ Features

- User-Item ratings preprocessing
- User-Based Collaborative Filtering
- Item-Based Collaborative Filtering
- Evaluation with **RMSE**, **Precision@K**, and **Recall@K**
- Top-N Recommendations per user
- Basic visualizations for evaluation results

---

## 📂 Project Structure

```
collaborative-filtering-recommender/
│
├── README.md
├── requirements.txt
│
├── data/
│   ├── u.data
│   ├── u.item
│   ├── u.user
│   └── ratings_merged.csv
│
├── notebooks/
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_user_based_cf.ipynb
│   ├── 03_item_based_cf.ipynb
│   └── 04_evaluation_and_visualization.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── recommender.py
│   └── evaluation.py
│
└── results/
    ├── top_n_recommendations.csv
    └── evaluation_metrics.json
```

---

## 🔧 Installation & Setup

### 1. Clone the repository
```bash
git clone <repo-url>
cd collaborative-filtering-recommender
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Download the dataset
- [MovieLens 100K Dataset on Kaggle](https://www.kaggle.com/datasets/prajitdatta/movielens-100k-dataset)
- Extract the `u.data`, `u.item`, `u.user` files to the `data/` directory.

---

## 🧪 Notebooks Overview

| Notebook                        | Purpose                                |
|---------------------------------|----------------------------------------|
| 01_data_preprocessing.ipynb     | Load and merge rating/user/item data   |
| 02_user_based_cf.ipynb          | User-based CF training & prediction    |
| 03_item_based_cf.ipynb          | Item-based CF training & prediction    |
| 04_evaluation_and_visualization | Evaluation with RMSE/visualizations    |

---

## 🧠 Core Algorithms

Implemented manually using `pandas` + `scikit-learn`:

- Cosine similarity for users and items
- Predict rating based on neighbors
- Top-N filtering per user

---

## 📈 Evaluation Metrics

- RMSE: Root Mean Squared Error
- Precision@K / Recall@K: based on sampled users

---

## 📦 Outputs

- `top_n_recommendations.csv`: top 10 movie predictions per user
- `evaluation_metrics.json`: stores RMSE values

---

## 🧩 Future Improvements
- Add implicit feedback handling
- Integrate hybrid recommendations
- Use LightFM or matrix factorization

---

## 👨‍💻 Author
This project is implemented for educational purposes as part of an Intelligent Programming course assignment.

