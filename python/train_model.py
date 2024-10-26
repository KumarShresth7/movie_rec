import pandas as pd
import numpy as np
from scipy.sparse.linalg import svds 
import pickle

movies = pd.read_csv('data/tmdb_5000_movies.csv')
cred = pd.read_csv('data/tmdb_5000_credits.csv')

movies = movies.merge(cred,on='title')


movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]
print(movies.head())

import ast
def convert(text):
    L = []
    for i in ast.literal_eval(text):
        L.append(i['name'])
    return L







