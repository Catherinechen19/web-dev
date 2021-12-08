from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Request(models.Model):
    MUSIC = "mu"
    MOVIE = "mo"
    GAME = "ga"
    PRODUCT_CATEGORY = [
        (MUSIC, 'Music'),
        (MOVIE, 'Movie'),
        (GAME, 'Game')
    ]

    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    category = models.CharField(
        max_length=2,
        choices=PRODUCT_CATEGORY,
    )
    image = models.ImageField(upload_to="request")

    def __str__(self):
        return str(self.user)

    @property
    def imageURL(self):
        try:
            url = self.room_img.url
        except:
            url = ''
        return url

class Extention(models.Model):
    reason = models.CharField(max_length=200)
    