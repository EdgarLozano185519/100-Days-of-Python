from flask import Flask, render_template
import requests
from post import Post

BLOG_URL = "https://api.npoint.io/5abcca6f4e39b4955965"
    
# Populate array of objects
all_posts = requests.get(BLOG_URL).json()
post_objs = []
for post in all_posts:
    post_obj = Post(post["title"], post["subtitle"], post["body"], post["id"])
    post_objs.append(post_obj)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:id>')
def get_post(id):
    post_return = None
    for post in post_objs:
        if post.id == id:
            post_return = post
    return render_template('post.html', post=post_return)

if __name__ == "__main__":
    app.run(debug=True)
