# Generated by Django 3.2.9 on 2021-12-02 14:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0017_alter_transaction_purchase_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='purchase_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 2, 14, 28, 51, 925968, tzinfo=utc)),
        ),
    ]
