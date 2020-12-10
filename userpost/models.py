from django.db import models
from django.conf import settings


# Create your models here.


class UserPost(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False, blank=False)
    time = models.DateTimeField(auto_now_add=True, null=True)