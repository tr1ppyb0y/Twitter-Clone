from django.urls import path
from . import views

app_name = "tweet"
urlpatterns = [
    path("<username>", views.tweets, name="tweets"),
    path("profile-info/<username>", views.profile_info, name="profile-info"),
    path("tweet-it/<username>", views.post_tweet, name="tweet-it"),
]
