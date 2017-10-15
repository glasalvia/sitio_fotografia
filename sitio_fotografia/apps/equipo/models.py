from __future__ import unicode_literals

from django.db import models


class Camara(models.Model):
	id=models.AutoField(primary_key=True)
	Modelo = models.CharField(max_length=255, blank=True)
	fecha_subida = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.Modelo

class Lente(models.Model):
	id=models.AutoField(primary_key=True)
	Lente = models.CharField(max_length=255, blank=True)
	fecha_subida = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.Lente

class Apertura(models.Model):
	id=models.AutoField(primary_key=True)
	Apertura = models.CharField(max_length=255, blank=True)
	fecha_subida = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.Apertura

class Velocidad(models.Model):
	id=models.AutoField(primary_key=True)
	Velocidad = models.CharField(max_length=255, blank=True)
	fecha_subida = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.Velocidad


class ISO(models.Model):
	id=models.AutoField(primary_key=True)
	ISO = models.CharField(max_length=255, blank=True)
	fecha_subida = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.ISO


