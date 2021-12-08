from django.db import models
from django.contrib.auth.models import User
from main.models import Product
from transaction.models import Transaction

# Create your models here.
class Refund(models.Model):
    PROCESS = "PC"
    SUCCESS = "SC"
    DENIED = "DN"
    TRANSACTION_STATUS = [
        (PROCESS, 'Process'),
        (SUCCESS, 'Success'),
        (DENIED, 'Denied')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(
        max_length=2,
        choices=TRANSACTION_STATUS,
    )
    image = models.ImageField(upload_to="tf")

    def __str__(self):
        return str(self.user)

    @property
    def imageURL(self):
        try:
            url = self.room_img.url
        except:
            url = ''
        return url
