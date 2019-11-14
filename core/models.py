from django.db import models

class Series (models.Model):
    nome = models.CharField(verbose_name = 'Nome da série', null=False, blank=False, max_length=50)
    nota = models.DecimalField(verbose_name= 'Nota', blank=False, null=False, max_digits=2, decimal_places=1)
    descricao = models.TextField(verbose_name = 'Descrição', null=True, blank=True)
    imagem = models.ImageField(verbose_name = 'Imagem', upload_to = 'image_series/', null = True, blank = True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Série'
        verbose_name_plural = 'Séries'

    def __str__ (self):
        return self.nome
    
