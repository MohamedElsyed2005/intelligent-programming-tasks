import pandas as pd
import os
"""
================================ from README.md ===============================
u.user     -- Demographic information about the users; this is a tab
              separated list of
              user id | age | gender | occupation | zip code
              The user ids are the ones used in the u.data data set.

u.data     -- The full u data set, 100000 ratings by 943 users on 1682 items.
              Each user has rated at least 20 movies.  Users and items are
              numbered consecutively from 1.  The data is randomly
              ordered. This is a tab separated list of 
	          user id | item id | rating | timestamp. 
              The time stamps are unix seconds since 1/1/1970 UTC  

u.item     -- Information about the items (movies); this is a tab separated
              list of
              movie id | movie title | release date | video release date |
              IMDb URL | unknown | Action | Adventure | Animation |
              Children's | Comedy | Crime | Documentary | Drama | Fantasy |
              Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |
              Thriller | War | Western |
              The last 19 fields are the genres, a 1 indicates the movie
              is of that genre, a 0 indicates it is not; movies can be in
              several genres at once.
              The movie ids are the ones used in the u.data data set.           
"""

def load_data(path):
    """
    u.data  -- The full u data set, 100000 ratings by 943 users on 1682 items.
            Each user has rated at least 20 movies.  Users and items are
            numbered consecutively from 1.  The data is randomly
            ordered. This is a tab separated list of 
	        user id | item id | rating | timestamp. 
            The time stamps are unix seconds since 1/1/1970 UTC 
    """
    data_cols = ["user_id","movie_id","rating","timestamp"]
    return pd.read_csv(os.path.join(path, "u.data"), sep = "\t", names = data_cols,encoding='latin-1')

def load_items(path):
    """
    u.item  -- Information about the items (movies); this is a tab separated
            list of
            movie id | movie title | release date | video release date |
            IMDb URL | unknown | Action | Adventure | Animation |
            Children's | Comedy | Crime | Documentary | Drama | Fantasy |
            Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |
            Thriller | War | Western |
            The last 19 fields are the genres, a 1 indicates the movie
            is of that genre, a 0 indicates it is not; movies can be in
            several genres at once.
            The movie ids are the ones used in the u.data data set.      
    """
    item_cols = ['movie_id', 'movie_title', 'release_date', 'video_release_date', 'IMDb_URL',
                  'unknown', 'Action', 'Adventure', 'Animation', "Children's", 'Comedy', 'Crime',
                  'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical',
                  'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
    return pd.read_csv(os.path.join(path, "u.item"), sep = "|", names = item_cols,encoding='latin-1')

def load_user(path):
    """
    u.user  -- Demographic information about the users; this is a tab
            separated list of
            user id | age | gender | occupation | zip code
            The user ids are the ones used in the u.data data set.
    """
    user_cols = ["user_id", "age","gender","occupation","zip_code"]
    return pd.read_csv(os.path.join(path, "u.user"), sep = "|", names = user_cols,encoding='latin-1')