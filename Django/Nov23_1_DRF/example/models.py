from django.db import models

class Fruit(models.Model):
    f_no = models.IntegerField(primary_key=True)
    f_name = models.CharField(max_length=10)
    f_price = models.IntegerField()
    f_explanation = models.TextField(default="")
