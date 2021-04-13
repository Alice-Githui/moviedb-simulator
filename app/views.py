from flask import render_template
from app import app
from .request import get_movies

# Views
@app.route('/')
def index():
    '''
    View the root page function that returns the index file and its data
    '''
    #Getting popular movie
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    title = 'Home - welcome to The Best Movie Review Website Online'
    return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie)


@app.route('/movie/<movie_id>')
def movie(movie_id):

    '''
    View movie page function that returns the movie details page and its data
    # '''
    # message = "Hello World"
    return render_template('movie.html', id = movie_id)