from __future__ import unicode_literals

from django.db import models
from . import choices


class Estado(models.Model):
    uf =  models.CharField(max_length=2)
    estado = models.CharField(max_length=100)
    
    def __str__(self):
        return self.uf

class Comarca(models.Model):
    descricao = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.descricao


class Decisao_dec(models.Model):
    id_tipodecisao = models.IntegerField()
    id_decisao = models.IntegerField()
    descricao = models.CharField(max_length=200)
    ativo = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['descricao']
    
    def __str__(self):
        return self.descricao


class Motivo_Decisao(models.Model):
    id_tipodecisao = models.IntegerField()
    id_decisao = models.IntegerField()
    id_motivo = models.IntegerField()
    descricao = models.CharField(max_length=200)
    ativo = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['descricao']
        
    def __str__(self):
        return self.descricao
        
    def __unicode__(self):
        return self.descricao

class Decisao_01(models.Model):
    data_inicial = models.DateField(null=True, blank=True)
    data_final = models.DateField(null=True, blank=True)
    tipo_decisao = models.CharField(max_length=100)
    decisao = models.CharField(max_length=100)
    estado = models.CharField(max_length=100, choices=choices.ESTADOS_CHOICES)

    class Meta:
        abstract = True     



class Tipo_Dec(models.Model):
    id_tipodecisao = models.IntegerField()
    descricao = models.CharField(max_length=200)
    ativo = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['descricao']
        
    def __str__(self):
        return self.descricao
        
    def __unicode__(self):
        return self.descricao
        
        
    class Meta:
        ordering = ('descricao',)       


class Resultado(models.Model):
    id_resultado = models.IntegerField()
    descricao = models.CharField(max_length=200)

    class Meta:
        ordering = ['descricao']
        
    def __str__(self):
        return self.descricao
        
    def __unicode__(self):
        return self.descricao



class Documento(models.Model):
    id_documento = models.AutoField(primary_key=True)
    nome_do_arquivo = models.CharField(max_length=150, null=False)
    tipo = models.CharField(max_length=30, null=False)    
    id_user = models.IntegerField(null=False,default=0)
    created_at = models.DateTimeField(auto_now_add=True,null=True)    

    def __str__(self):
        return self.nome_do_arquivo

    class Meta:
        db_table = 'documentos'

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE {}'.format(cls._meta.db_table))

