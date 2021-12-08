from django.db import models
from django.contrib.auth.models import User
# from .models import Categories

# Create your models here.
class Product(models.Model):
    MUSIC = "mu"
    MOVIE = "mo"
    GAME = "ga"
    PRODUCT_CATEGORY = [
        (MUSIC, 'Music'),
        (MOVIE, 'Movie'),
        (GAME, 'Game')
    ]
    name = models.CharField(max_length=200)
    qty = models.IntegerField()
    description = models.TextField()
    category = models.CharField(
        max_length=2,
        choices=PRODUCT_CATEGORY,
    ) 
    # category =  models.ForeignKey(Categories, on_delete=models.CASCADE)
    price = models.IntegerField()
    image = models.ImageField(upload_to="menu", default="request/default.png")

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.media.url
        except:
            url = ''
        return url

# class Categories(models.Model):
#     MUSIC = "mu"
#     MOVIE = "mo"
#     GAME = "ga"
#     PRODUCT_CATEGORY = [
#         (MUSIC, 'Music'),
#         (MOVIE, 'Movie'),
#         (GAME, 'Game')
#     ]

#     category = models.CharField(
#         max_length=2,
#         choices=PRODUCT_CATEGORY,
#     ) 

#     user = models.ForeignKey(User, on_delete=models.CASCADE)