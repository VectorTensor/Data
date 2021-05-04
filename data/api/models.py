from django.db import models

# Create your models here.
class Data(models.Model):
    X= models.IntegerField()
    Y=models.IntegerField()

    def __str__(self):
        return f"{self.X} ===> {self.Y}"





