from django.db import models

# Create your models here.

class StudentsPost(models.Model):
    matricula = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=300)
    serie = models.CharField(max_length=30)
    data_presença = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome