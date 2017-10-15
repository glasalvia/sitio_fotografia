from __future__ import unicode_literals

from django.db import models
from apps import equipo

class Album(models.Model):
	id=models.AutoField(primary_key=True)
	titulo = models.CharField(max_length=255, blank=True)
	fecha_subida = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.titulo


class Fotografia(models.Model):
	id=models.AutoField(primary_key=True)
	fk_album = models.ForeignKey('Album', default=True)
	fk_camara = models.ForeignKey(equipo.models.Camara, default=True)
	fk_lente = models.ForeignKey(equipo.models.Lente, default=True)
	fk_apertura = models.ForeignKey(equipo.models.Apertura, default=True)
	fk_velocidad = models.ForeignKey(equipo.models.Velocidad, default=True)
	fk_ISO = models.ForeignKey(equipo.models.ISO, default=True)
	Archivo = models.FileField(upload_to='documents/')
	fecha_subida = models.DateTimeField(auto_now_add=True)
	Titulo = models.CharField(max_length=255, blank=True)
	Descripcion = models.CharField(max_length=255, blank=True)
	def __str__(self):
		return self.Titulo


