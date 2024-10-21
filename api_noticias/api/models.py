from django.db import models

class Noticia(models.Model):
    idNoticia = models.IntegerField.auto_creation_counter
    titulo = models.CharField(max_length=100)
    image = models.ImageField()
    texto = models.CharField(max_length=1000)
