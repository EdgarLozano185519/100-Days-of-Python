from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    return f"Name: {request.form['name']}\nPassword: {request.form['password']}"
  else:
    return render_template('index.html')

app.run(debug=True)