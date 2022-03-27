from email.policy import default
from django.db import models

class Postagem(models.Model):
    id_postagem = models.AutoField(primary_key=True, max_length=6)
    nome_autor = models.CharField(max_length=50)
    titulo_postagem = models.CharField(max_length=50)
    data_postagem = models.DateTimeField(auto_now=True)
    texto_postagem = models.TextField(max_length=500)

    def __str__(self):
        nome_objeto = f'{self.titulo_postagem} - por {self.nome_autor} - ({self.id_postagem})'
        return nome_objeto
