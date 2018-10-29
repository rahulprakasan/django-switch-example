from django.db import models

# Create your models here.
from django.db import models

class button(models.Model):
    button = models.CharField(max_length=264,unique=False)
    date = models.DateField()
    def __str__(self):
        return self.button


