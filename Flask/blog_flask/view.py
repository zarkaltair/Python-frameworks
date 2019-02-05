from app import app
from flask import render_template


@app.route('/')
def index():
    # function that is responsible for displaying content
    return render_template('index.html')


# create castom 404 page
@app.errorhandler(404)
def page_not_found(e):
	# function that is responsible for displaying 404 page
    return render_template('404.html'), 404