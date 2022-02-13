import pandas as pd
import numpy as np
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel 

from sklearn.metrics.pairwise import linear_kernel

pd.set_option("display.max_rows", None, "display.max_columns", None)

import warnings
warnings.filterwarnings('ignore')

posts = pd.DataFrame(list(Post.Objects.all().values()))
posts.rename(columns={'id':'post_id', 'type':'post_type'})
posts.tags.fillna("General", inplace = True)
posts['tags'] = posts['tags'].str.split("|")
posts['tags'] = posts['tags'].fillna("").astype('str')
users = pd.DataFrame(list())

likes = pd.DataFrame(list())

df = likes.merge(posts, on='post_id', how='left')
df = df.merge(users, on='user_id', how='left')

df = df.dropna(thresh=8)

tf = TfidfVectorizer(analyzer='word', sublinear_tf=True, ngram_range=(1, 3), min_df=0, stop_words='english')
tfidf_matrix = tf.fit_transform(posts['tags'] + " " + posts['type'])
tfidf_matrix.shape

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

postid = posts['post_id']
indices = pd.Series(posts.index, index=posts['post_id'])

def get_recommendations(postid, indices):
    idx = indices[postid]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x:x[1], reverse=True)
    sim_scores = sim_scores[1:5] #we can change the number of recommendations on each topic
    indices = [i[0] for i in sim_scores]
    return posts.iloc[indices]