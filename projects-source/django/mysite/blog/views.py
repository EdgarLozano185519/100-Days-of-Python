from django.shortcuts import render

# Create dummy dictionary here
all_posts = [
    {
        "title": "First Blog Entry",
        "text": "This is my first blog here. I can't believe how dumb this blog is to me right now."
    }
]

# Create your views here.


def start_page(request):
    return render(request, "blog/index.html", {
        "posts": all_posts
    })


def posts(request):
    pass


def detail_page(request):
    pass
