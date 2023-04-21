#importing flask as a framewrork

from flask import Flask, request
import csv
import json

app = Flask(__name__)

def movie_filter(genre):
    fname = 'imdb-movie-data.csv'
    genre_list = []
    with open(fname) as csvfile:
        csv_reader = csv.DictReader(csvfile)
        if genre == None:
           for movie in csv_reader:
               genre_list.append(movie)

        for movie in csv_reader:
            genres = movie['Genre'].split(',')
            if genre.lower() in [item.lower() for item in genres]:
                genre_list.append(movie)
    return genre_list

@app.route('/<genre>')
def movies_by_genre(genre):
    genre_param = genre
    movies = movie_filter(genre_param)
    return json.dumps(movies)

@app.route('/')
def get_genre():
    genre = request.args.get('genre')
    movies= movie_filter(genre)
    return json.dumps(movies)

if __name__ == '__main__':
    app.run('0.0.0.0', port=8080)
  

