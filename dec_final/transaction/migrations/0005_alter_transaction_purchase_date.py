# Generated by Django 3.2.9 on 2021-11-23 12:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0004_transaction_purchase_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='purchase_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 23, 12, 10, 55, 735538, tzinfo=utc)),
        ),
    ]
