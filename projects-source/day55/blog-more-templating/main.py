from flask import Flask, render_template
import requests

app = Flask(__name__)

BLOG_URL = "https://api.npoint.io/5abcca6f4e39b4955965"
all_posts = requests.get(BLOG_URL).json()

@app.route('/')
def home():
  return render_template('index.html', posts=all_posts, title_name="Home")

@app.route('/about')
def about():
  return render_template('about.html', title_name="About")

@app.route('/contact')
def contact():
  return render_template('contact.html', title_name="Contact Me")

@app.route('/post/<int:id>')
def get_post(id):
  requested_post = None
  for post in all_posts:
    if id == post['id']:
      requested_post = post
  return render_template('post.html', post=requested_post, title_name=requested_post['title'])

app.run(debug=True)
