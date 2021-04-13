from flask import render_template
from app import app

# Views
@app.route('/')
def index():
    '''
    View the root page function that returns the index file and its data
    '''
    title = 'Home - welcome to The Best Movie Review Website Online'
    message = "Hello World"
    return render_template('index.html', message = message, title = title)


@app.route('/movie/<movie_id>')
def movie(movie_id):

    '''
    View movie page function that returns the movie details page and its data
    # '''
    # message = "Hello World"
    return render_template('movie.html', id = movie_id)