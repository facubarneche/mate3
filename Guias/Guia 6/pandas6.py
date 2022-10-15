"""
6.La carpeta dataset contiene 3 archivos referentes a usuarios, votos y películas:
a. Genera el código de agrupamiento y agregación necesario para calcular: suma, cuenta,
utilizando las funciones de numpy (ej: np.sum)
"""

import pandas as pd
import numpy as np

def main():

    # Obtengo los datos de los .txt
    userHeader = ['user_id', 'gender', 'age', 'ocupation', 'zip']
    users = pd.read_table('Clases/Unsam.Clase.6/dataset/users.txt', engine='python', sep='::', header=None, names=userHeader)

    ratingHeader = ['user_id', 'movie_id', 'rating', 'timestamp']
    ratings = pd.read_table('Clases/Unsam.Clase.6/dataset/rating.txt', engine='python', sep='::', header=None, names=ratingHeader)

    movieHeader = ['movie_id', 'title', 'genders']
    movies = pd.read_table('Clases/Unsam.Clase.6/dataset/movies.txt', engine='python', sep='::', header=None, names=movieHeader, encoding='latin-1')

    # Impresion de los archivos ya en dataframe
    print(users.head())
    print(ratings.head())
    print(movies.head())

    # Agrupo los siguientes dataFrames
    mergeRatings = pd.merge(users, ratings, on='user_id')
    
    
    ##df = pd.DataFrame(users, ratings, movies, columns=['usuarios', 'calificaciones', 'peliculas'])
    ##print('\n=========================================\n')
    ##print('Agrupo los usuarios, ratings y peliculas\n')
    #print(df.head())
    print(mergeRatings.head())


if __name__ == '__main__':
    main()


