from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Tweets(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    picture = models.ImageField(
        _("Profile picture"), upload_to="profile_pics/", null=True, blank=True
    )
    content = models.TextField(blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(
        "self", blank=True, null=True, on_delete=models.CASCADE, related_name="thread"
    )
    reply = models.BooleanField(verbose_name=_("Is a reply?"), default=False)

    class Meta:
        verbose_name = "Tweet"
        verbose_name_plural = "Tweets"
        ordering = ("-timestamp",)

    def __str__(self):
        return str(self.content)

    def get_parent(self):
        if self.parent:
            return self.parent

        else:
            return self

    def get_thread(self):
        parent = self.get_parent()
        return parent.thread.all()

    def count_thread(self):
        return self.get_thread().count()
