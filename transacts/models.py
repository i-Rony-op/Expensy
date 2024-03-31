from django.db import models


class Transactions(models.Model):
    item = models.CharField(max_length=20)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    date = models.DateField()

    class Meta:
        db_table = "transactions"
