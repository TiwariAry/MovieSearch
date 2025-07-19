# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# print(df.columns.values)
# cv = CountVectorizer(max_features=5000, stop_words='english')
# vectors = cv.fit_transform(df['tags']).toarray()
# similarity = cosine_similarity(vectors)
# np.save('similarity.npy', similarity)

import pandas as pd
import numpy as np

import requests

df = pd.DataFrame(pd.read_csv("Finalized_file.csv"))
movie_names = pd.read_csv('movie_names.csv')
similarity = np.load('similarity.npy') # Shape: (4806, 4806)


def getPoster(movie_id):
	response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=941c2d450ca7fc079a6df882a1bbfe26&language=en-US'.format(movie_id))
	return ['https://image.tmdb.org/t/p/w185' + response.json()['poster_path'], response.json()['overview']]


def recommender_function(movie):
	movie = df[df['title'] == movie.lower()]

	if not movie.empty:
		index = movie.index[0]
		# (index, similarity in scale of 0-1)
		movies_info = [i[0] for i in sorted(enumerate(similarity[index]), reverse=True, key=lambda x: x[1])[1: 6]]

		movies_name, movies_id = [df.loc[i, 'title'].capitalize() for i in movies_info], [df.loc[i, 'id'] for i in movies_info]

		movies_poster, movies_description = [], []
		for id in movies_id:
			info = getPoster(id)
			movies_poster.append(info[0])
			movies_description.append(info[1])

		return [movies_name, movies_poster, movies_description]

	return "Movie not found"

print(recommender_function('Batman'))