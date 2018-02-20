from django.db import models


class Categoria(models.Model):
    
    titulo = models.CharField('Titulo', max_length=100)
    descricao = models.TextField('Descrição', max_length=255)
    
    def __str__(self):
        return "Titulo: {}".format(self.titulo)

    class Meta:
        db_table = 'categoria'
        
class Noticia(models.Model):
    
    titulo = models.CharField('Titulo', max_length=100)
    categoria = models.ForeignKey(
        Categoria, models.SET_NULL, verbose_name='Categoria', null=True
    )
    publicacao = models.DateField('Publicacao', null=True, blank=True)
    conteudo = models.TextField('Conteúdo')
    criado_em = models.DateTimeField('Criado em')
    modificado_em = models.DateTimeField('Modificado em', blank=True, null=True)

    def __str__(self):
        return "Titulo: {}".format(self.titulo)

    class Meta:
        db_table = 'core_noticias'
        
