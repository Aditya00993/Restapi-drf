from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    fathername = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        
  