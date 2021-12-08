from django.db import models
from django.contrib.auth.models import User
from main.models import Product
from transaction.models import Transaction
from django.utils.timezone import now

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField(max_length=200)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
  
class Post(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.AutoField
    post_content = models.CharField(max_length=5000)
    timestamp= models.DateTimeField(default=now)
    
class Replie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply_id = models.AutoField
    reply_content = models.CharField(max_length=5000) 
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp= models.DateTimeField(default=now)
