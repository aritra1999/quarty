# Importing Libraries
import pandas as pd
import numpy as np
import os

import warnings
warnings.filterwarnings('ignore')

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import linear_kernel
# Reading datasets into dataframes
df = pd.DataFrame(list())

friends = pd.DataFrame(list)

# Adding Movie, Sport , Song and Book interests in Interests columns
df["Interests"] = df["Movie_Tags"].astype(str) +"|"+ df["Sports_Tags"] +"|"+ df["Song_Tags"] +"|"+ df["Book_Tags"]
# Dropping Movie, Sport , Song and Book tags after adding them into interests
df = df.drop(columns=['Movie_Tags', 'Sports_Tags', 'Song_Tags', 'Book_Tags'])
# Converitng '|' seperated values into a list
df['Interests'] = df['Interests'].str.split("|")
df['Interests'] = df['Interests'].fillna("").astype('str')
# Converting location into a list
df['Location'] = df['Location'].str.split("|")
df['Location'] = df['Location'].fillna("").astype('str')

# Applying Tfidf
tf = TfidfVectorizer(analyzer='word',ngram_range=(1,2), min_df=0, stop_words='english')
tfidf_matrix = tf.fit_transform(df['Interests'] + " " + df['Location'])

# Finding cosine similarities
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

users = df['name']
indices = pd.Series(users.index, index=df['name'])


# Function to be called to get user_recommendations
def user_recommendations(name):
    idx = indices[name]
    sim_scores = list(enumerate(cosine_sim[idx]))
    # Removing friends from the sim_score list so that only those users are recommended which aren't friends
    for i in range(friends.shape[0]):
        if friends.User1[i] == indices[name]:
            del sim_scores[friends.User2[i]]
        elif friends.User2[i] == indices[name]:
            del sim_scores[friends.User1[i]]
    sim_scores = sorted(sim_scores, key=lambda x:x[1], reverse=True)
    sim_scores = sim_scores[1:21]
    user_indices = [i[0] for i in sim_scores]
    return df.iloc[user_indices]['name']