from doctest import master
from django.db import models
from super_types.models import SuperTypes

# Create your models here.
class Super(models.Model):
    name = models.CharField(max_length=255)
    alter_ego = models.CharField(max_length=255)
    primary_ability = models.CharField(max_length=255)
    secondary_ability = models.CharField(max_length=255)
    catchphrase = models.CharField(max_length=255)
    super_type = models.ForeignKey(SuperTypes, on_delete=models.CASCADE)

    def __str__(self):
        # return f'{self.name} {self.alter_ego} {self.primary_ability} {self.secondary_ability} {self.catchphrase} {self.super_type}'
        return self.name