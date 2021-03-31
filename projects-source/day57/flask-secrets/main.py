from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap

class MyForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(),
        Email(message="Email is not in valid format.")
    ])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=8, message="Password must be at least 8 characters long.")
    ])
    submit = SubmitField('Log In')

app = Flask(__name__)
app.secret_key = "asldktjethiowpa19"
Bootstrap(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = MyForm()
    correct_email = "admin@email.com"
    correct_password = "12345678"
    if form.validate_on_submit():
        if form.email.data == correct_email and form.password.data == correct_password:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)