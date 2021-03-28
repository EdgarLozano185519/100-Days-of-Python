from flask import Flask, render_template
from datetime import datetime
import requests

# Constants
GENDERIZE_URL = "https://api.genderize.io"
AGIFY_URL = "https://api.agify.io"

app = Flask(__name__)
dt = datetime.now()

@app.route('/')
def home():
  return render_template('index.html', year=dt.year)

@app.route('/guess/<name>')
def guess(name):
  gender = requests.get(GENDERIZE_URL, {"name": name}).json()['gender']
  age = requests.get(AGIFY_URL, {"name": name}).json()['age']
  return render_template("guess.html", name=name, age=age, gender=gender)

if __name__ == "__main__":
    app.run(debug=True)


