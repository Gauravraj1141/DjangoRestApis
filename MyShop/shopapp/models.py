from django.db import models


class ProductTrali(models.Model):
    pr_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=444)
    product_catagory = models.CharField(max_length=444)
    product_price = models.IntegerField()
