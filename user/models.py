from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.


class User(AbstractUser):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=100, unique=True)
    picture = models.ImageField(
        _("Profile picture"), upload_to="profile_pics/", null=True, blank=True
    )
    bio = models.CharField(max_length=500, blank=True)
    location = models.CharField(max_length=200, blank=True)
    website = models.URLField()
    date_joined = models.DateTimeField(auto_now_add=True)
    dob = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Friends(models.Model):
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="follower"
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="following"
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-timestamp",)
        verbose_name = "Friend"
        verbose_name_plural = "Friends"
