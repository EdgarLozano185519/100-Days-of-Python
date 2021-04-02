from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

db.create_all()

@app.route('/')
def home():
    all_books = Book.query.all()
    return render_template('index.html', books=all_books, text="")

@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == "POST":
        new_book = Book(title=request.form['title'], author=request.form['author'], rating=request.form['rating'])
        db.session.add(new_book)
        db.session.commit()
        #all_books.append(book_dict)
    return render_template('add.html')

@app.route('/rating', methods=['POST', 'GET'])
def rating():
    title = request.args.get('title')
    book = Book.query.filter_by(title=title).first()
    text = "Update Rating"
    if request.method == "POST":
        book.rating = request.form['rating']
        db.session.commit()
        book = Book.query.filter_by(title=title).first()
        text = "Rating Updated"
    return render_template("update_rating.html", book=book, text=text)

@app.route('/delete')
def delete():
    title = request.args.get('title')
    book = Book.query.filter_by(title=title).first()
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

