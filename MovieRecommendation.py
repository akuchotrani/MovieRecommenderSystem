# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 14:51:34 2017

@author: aakash.chotrani
"""

import pandas as pd


r_cols = ['user_id','movie_id','rating']
ratings = pd.read_csv('C:/Users/aakash.chotrani/Desktop/DataScience-Python3/ml-100k/u.data', sep = '\t', names = r_cols, usecols = range(3))


m_cols = ['movie_id','title']
movies = pd.read_csv('C:/Users/aakash.chotrani/Desktop/DataScience-Python3/ml-100k/u.item', sep = '|', names = m_cols, usecols = range(2), encoding = 'latin-1')

ratings = pd.merge(movies,ratings)

movieRatings = ratings.pivot_table(index = ['user_id'], columns = ['title'], values = 'rating')

starWarsRatings = movieRatings['Star Wars (1977)']


similarMovies = movieRatings.corrwith(starWarsRatings)
similarMovies = similarMovies.dropna()
df = pd.DataFrame(similarMovies)
df.head(10)


similarMovies.order(ascending = False)