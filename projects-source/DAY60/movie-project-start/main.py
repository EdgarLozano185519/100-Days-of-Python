from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired
import requests
from decouple import config

# Constants
MOVIE_DATABASE_KEY = config('MOVIE_DATABASE_KEY')
SEARCH_MOVIES_URL = "https://api.themoviedb.org/3/search/movie"
MOVIEDB_DETAILS_URL = "https://api.themoviedb.org/3/movie"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# SQL Alchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(app)
# Movie class to define table
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(500), nullable=True)
    img_url = db.Column(db.String(500), nullable=False)

# Create tables
db.create_all()


# Form class for updating movie review and rating
class UpdateMovie(FlaskForm):
    review = StringField('Updated Review', validators=[DataRequired()])
    rating = FloatField('Updated Rating', validators=[DataRequired()])
    submit = SubmitField()

# Form to add a movie.
class AddForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')

@app.route("/")
def home():
    movies = Movie.query.order_by(Movie.rating).all()
    movies.reverse()
    return render_template("index.html", movies=movies)

@app.route('/update', methods=['POST', 'GET'])
def update():
    movie = Movie.query.filter_by(title=request.args.get('title')).first()
    form = UpdateMovie(review=movie.review, rating=movie.rating)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=form)

@app.route("/delete")
def delete():
    movie = Movie.query.filter_by(title=request.args.get('title')).first()
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))
    
@app.route('/add', methods=['POST', 'GET'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        title = form.title.data
        
        # Make the request with the search query
        query = {
            "api_key": MOVIE_DATABASE_KEY,
            "query": title
        }
        response = requests.get(SEARCH_MOVIES_URL, query)
        results = response.json()['results']
        
        # Loop through results and make array to pass to template
        movies = []
        for movie in results:
            temp = {}
            temp['id'] = movie['id']
            temp['title'] = movie['title']
            temp['release'] = movie['release_date']
            movies.append(temp)
        
        # Render template
        return render_template('select.html', movies=movies)
    return render_template('add.html', form=form)

@app.route('/select')
def select():
    # Make a request to the Movie Database for details
    id = request.args.get('id')
    url = f"{MOVIEDB_DETAILS_URL}/{id}"
    response = requests.get(url, {"api_key": MOVIE_DATABASE_KEY})
    result = response.json()
    
    # Add to database
    movie = Movie(
        title=result['title'],
        description=result['overview'],
        year=result['release_date'].split('-')[0],
        img_url=result['poster_path']
    )
    db.session.add(movie)
    db.session.commit()
    return redirect(url_for('update', title=result['title']))

if __name__ == '__main__':
    app.run(debug=True)
