from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse

monthly_challenges = {
    "january": "Learn how to code",
    "february": "learn about Python.",
    "march": "Learn about C#",
    "april": "Learn about Java",
    "may": "Call it a day"
}

# Create your views here.
def index(request):
    #challenge_items = ""
    #list_items = list(monthly_challenges)
    #for item in list_items:
        #month_path = reverse('monthly_challenge', args=[item])
        #challenge_items += f"<li><a href=\"{month_path}\">{item.capitalize()}</a></li>"
    #response_data = f"<ul>{challenge_items}</ul>"
    return render(request, 'challenges/index.html', {"months": monthly_challenges})

def month_by_number(request, month):
    challenges = list(monthly_challenges.keys())
    if month > len(challenges):
        return HttpResponseNotFound("Invalid month.")
    return HttpResponseRedirect(reverse('monthly_challenge', args=[challenges[month-1]]))

def monthly_challenge(request, month):
    try:
        return render(request, 'challenges/challenge.html', {"title": month, "text": monthly_challenges[month]})
    except:
        return HttpResponseNotFound("Month not supported.")