from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route('/random')
def random():
    cafes = Cafe.query.all()
    cafe = choice(cafes)
    return jsonify(
        name=cafe.name,
        map_url=cafe.map_url,
        img_url=cafe.img_url,
        location=cafe.location,
        seats=cafe.seats,
        has_toilet=cafe.has_toilet,
        has_wifi=cafe.has_wifi,
        has_sockets=cafe.has_sockets,
        can_take_calls=cafe.can_take_calls,
        coffee_price=cafe.coffee_price
    )

@app.route('/all')
def all():
    cafes = Cafe.query.all()
    all_cafes = []
    for cafe in cafes:
        cafe_dict = {
            "id": str(cafe.id),
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "seats": cafe.seats,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "has_sockets": cafe.has_sockets,
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price
        }
        all_cafes.append(cafe_dict)
    return jsonify(all_cafes)

@app.route('/search')
def search():
    cafes = Cafe.query.filter_by(location=request.args.get('loc')).all()
    if cafes == None:
        return jsonify({"error": {
            "Not Found": "Sorry, we don't have a cafe at that location."
        }})
    else:
        all_cafes = []
        for cafe in cafes:
            cafe_dict = {
                "name": cafe.name,
                "map_url": cafe.map_url,
                "img_url": cafe.img_url,
                "location": cafe.location,
                "seats": cafe.seats,
                "has_toilet": cafe.has_toilet,
                "has_wifi": cafe.has_wifi,
                "has_sockets": cafe.has_sockets,
                "can_take_calls": cafe.can_take_calls,
                "coffee_price": cafe.coffee_price
            }
            all_cafes.append(cafe_dict)
        return jsonify({"cafes": all_cafes})
    # End search function

## HTTP POST - Create Record
@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == "POST":
        cafe = Cafe(
            name=request.form.get('name'),
            map_url=request.form.get('map_url'),
            img_url=request.form.get('img_url'),
            location=request.form.get('location'),
            seats=request.form.get('seats'),
            has_toilet=bool(request.form.get('has_toilet')),
            has_wifi=bool(request.form.get('has_wifi')),
            has_sockets=bool(request.form.get('has_sockets')),
            can_take_calls=bool(request.form.get('can_take_calls')),
            coffee_price=request.form.get('coffee_price')
        )
        db.session.add(cafe)
        db.session.commit()
        return jsonify({"Success.": "Cafe added."})
    return jsonify({"error": "No cafe specified"})

## HTTP PUT/PATCH - Update Record
@app.route('/update/price/<int:cafe_id>', methods=["PATCH"])
def update(cafe_id):
    cafe = Cafe.query.filter_by(id=cafe_id).first()
    if cafe == None:
        return jsonify(error={"Not Found": "A resource with the id was not found."}), 404
    else:
        cafe.coffee_price = request.args.get('price')
        db.session.commit()
        return jsonify({"Success!": "Coffee price updated successfully."}), 200

## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=['DELETE'])
def delete(cafe_id):
    api_key = "sktjejtjiopa_213456"
    key_entered = request.args.get('api_key')
    if key_entered != api_key:
        return jsonify({"Error": "API key not valid."}), 403
    else:
        cafe = Cafe.query.filter_by(id=cafe_id).first()
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify({"Success!": "Cafe deleted from database."}), 200
        else:
            return jsonify(error={"Not Found": "Resource with id not found in database."}), 404
            

if __name__ == '__main__':
    app.run(debug=True)
