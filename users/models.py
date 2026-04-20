# from django.db import models

# Create your models here.
from django.db import models

class Player(models.Model):
    username = models.CharField(max_length=100, unique=True)
    key = models.CharField(max_length=100)
    high_score = models.IntegerField(default = 0)
    def __str__(self):
        return self.username