from django.shortcuts import render
from tweet.models import Tweets
from user.models import User, Friends
from django.http.response import JsonResponse
from django.core import serializers
import json
from user.forms import SearchForm
from django.views.decorators.csrf import ensure_csrf_cookie
import datetime
from django.http import HttpResponse


def tweets(request, username):
    if request.method == "GET":
        user = User.objects.filter(username=username)
        search = SearchForm()
        if len(user) == 1:
            tweets = Tweets.objects.filter(user__username=username, reply=False)
            return render(
                request,
                "tweet/tweets.html",
                {"tweets": tweets, "username": username, "form": search},
            )
        else:
            return render(request, "tweet/error.html", {"form": search})
    elif request.method == "POST":
        user = User.objects.filter(username=username)
        search = SearchForm()
        tweets = Tweets.objects.filter(user__username=username, reply=False)
        print(type)
        request = request.get_full_path().split("/")
        request[-1] = username
        request = "/".join(request)
        return render(
            request,
            "tweet/tweets.html",
            {"tweets": tweets, "username": username, "form": search},
        )


@ensure_csrf_cookie
def post_tweet(request, username):
    if request.method == "POST":
        tweet = Tweets()
        tweet.timestamp = datetime.datetime.now()
        user = User.objects.filter(username=request.user)
        tweet.user = user[0]
        tweet.picture = None
        tweet.content = request.POST.get("sent")
        tweet.parent = None
        tweet.reply = False
        tweet.save()
        return HttpResponse(status=200)


def profile_info(request, username):
    if request.method == "GET":
        user = User.objects.filter(username=username)
        sq = serializers.serialize("json", user)
        sq = json.loads(sq)
        sq = dict(sq[0])
        sq = delete_extra(sq)
        return JsonResponse(sq, safe=False)


def feeds(request):
    queryset = Friends.objects.none()
    feeds_for = Friends.objects.filter(follower=request.user)
    for following in feeds_for:
        queryset = queryset | Tweets.objects.filter(
            user__username=following.following, reply=False
        )
    return render(
        request,
    )


def delete_extra(user_dict):
    del user_dict["fields"]["is_active"]
    del user_dict["fields"]["is_staff"]
    del user_dict["fields"]["user_permissions"]
    del user_dict["fields"]["groups"]
    del user_dict["fields"]["is_superuser"]
    del user_dict["model"]
    user_dict["fields"]["date_joined"] = formatDate(user_dict["fields"]["date_joined"])
    user_dict["fields"]["password"] = "Are you smart enough?! ;)"
    return user_dict


def formatDate(date):
    if date[5:7] == "01":
        date = "January " + date[:4]
    elif date[5:7] == "02":
        date = "Febuarary " + date[:4]
    elif date[5:7] == "03":
        date = "March " + date[:4]
    elif date[5:7] == "04":
        date = "April " + date[:4]
    elif date[5:7] == "05":
        date = "May " + date[:4]
    elif date[5:7] == "06":
        date = "June " + date[:4]
    elif date[5:7] == "07":
        date = "July " + date[:4]
    elif date[5:7] == "08":
        date = "August " + date[:4]
    elif date[5:7] == "09":
        date = "September " + date[:4]
    elif date[5:7] == "10":
        date = "October " + date[:4]
    elif date[5:7] == "11":
        date = "November " + date[:4]
    else:
        date = "December " + date[:4]
    return date
