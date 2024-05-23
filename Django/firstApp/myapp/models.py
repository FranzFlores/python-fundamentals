from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    content = models.TextField(verbose_name='Contenido')
    public = models.BooleanField(verbose_name='Publicado')
    image = models.ImageField(default='null', verbose_name='Imagen', upload_to='articles')
    created_at = models.DateField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'
        ordering = ['id']

    #Para mostrar el nombre del modelo en lugar del id
    def __str__(self):
        return f"{self.title} creado el {self.created_at}"

class Category(models.Model):
    name = models.CharField(max_length=110)
    description = models.CharField(max_length=250)
    created_at = models.DateField()

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
