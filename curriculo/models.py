from django.db import models

# Create your models here.
class Certificados(models.Model):
    instituicao = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_final = models.DateField()
    categoria = models.CharField(max_length=100)

class Experiencias(models.Model):
    instituicao = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_final = models.DateField()
    categoria = models.CharField(max_length=100)

    @property
    def bullets(self):
        return [p.strip() for p in self.descricao.split(";") if p.strip()]

class Skills(models.Model):
    titulo = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
