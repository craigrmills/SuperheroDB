from django.db import models


class Superhero(models.Model):
    name = models.CharField(max_length=50)
    alter_ego = models.CharField(max_length=50)
    prim_superpower = models.CharField(max_length=50)
    secon_superpower = models.CharField(max_length=50)
    catchphrase = models.CharField(max_length=200)

    def __str__(self):
        return self.name
