# IMDB-API
A backend API that allows a user to search for a movie by genre.
# Welcome to My Imdb Api
*** Welcome to my Imdb Api project ***

## Task
***Create a backend app with a light web framework, for python we recommend using flask.It will listen on port 8080***

## Description
***I imported flask as a framework, I also imported json and request.***

## Installation
***my project runs on the qwasar server so it does not need to be installed to run***


## Usage
```python
@app.route('/')
def movies_by_genre(genre):
    genre = request.args.get('genre')
    movies = movie_filter(genre)
    return json.dumps(movies)
```

### The Core Team
<p>
<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px'></span>
</p>