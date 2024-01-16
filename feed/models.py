from django.db import models
from sorl.thumbnail import ImageField

# Create your models here.
class Post(models.Model):
    text = models.CharField(max_length=140, blank=False, null=False)
    image = ImageField()
    # then make a migration

    # updating Data name in Database View Django
    def __str__(self):
        return self.text