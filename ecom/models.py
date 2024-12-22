from django.db import models

# Create your models here.
class FoodItems(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField()

    def __str__(self):
        return self.name