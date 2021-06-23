from django.shortcuts import render

# Create dummy dictionary here
all_posts = [
    {
        "title": "First Blog Entry",
        "text": "This is my first blog here. I can't believe how dumb this blog is to me right now.",
        "excerpt": "My first blog.",
        "slug": "first-blog-entry"
    },
    {
        "title": "Second Blog Entry",
        "text": "Just another entry here. I hope you are enjoying this blog so far. It's really neat!",
        "excerpt": "My second blog entry.",
        "slug": "second-blog-entry"
    }
]

# Create your views here.


def start_page(request):
    return render(request, "blog/index.html", {
        "posts": all_posts
    })


def posts(request):
    return render(
        request,
        "blog/all_posts.html",
        {
            "posts": all_posts
        }
    )


def detail_page(request, slug):
    for post in all_posts:
        if post['slug'] == slug:
            return render(request, "blog/post-details.html", {"current_post": post})
