from django.db import models
from django.contrib.auth.models import User
from main.models import Product
import random
from django.utils import timezone

def generate_pk():
    number = random.randint(1000, 9999)
    return 'AA{}{}'.format(timezone.now().strftime('%y%m%d'), number)

# Create your models here.
class Transaction(models.Model):
    BUY = "B"
    RENT = "R"
    TRANSACTION_STATUS = [
        (BUY, 'Buy'),
        (RENT, 'Rent'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=1,
        choices=TRANSACTION_STATUS,
    )
    id = models.CharField(default=generate_pk, max_length=255, primary_key=True)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(default=timezone.now())
    # due_date = models.DateTimeField(null=True)
    
    def __str__(self):
        return str(self.user)

    

