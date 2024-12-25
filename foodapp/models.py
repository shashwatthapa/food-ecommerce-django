from django.db import models

# Create your models here.
class PostItem(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')
    price = models.IntegerField()

    def __str__(self):
        return self.name
