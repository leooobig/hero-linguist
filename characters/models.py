from django.db import models

# Create your models here.
class Personagem(models.Model):
    nome = models.CharField(max_length=50)
    afiliacao = models.CharField(max_length=50)
    aliados = models.CharField(max_length=150)
    inimigos = models.CharField(max_length=150)

    def __str__(self):
        return self.nome