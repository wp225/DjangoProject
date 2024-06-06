from django.db import models

# Create your models here.
from django.db import models

class UserDetails(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
