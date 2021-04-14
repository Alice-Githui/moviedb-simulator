from flask import render_template
from app import app

@app.errorhandler(404)
def four_Ouw_four(error):
    '''
    Function to render the 404 error page
    '''

    return render_template('fourOuwfour.html'), 404