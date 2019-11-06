"""Django"""
from django.http import HttpResponse

def hola_mundo(request):
	"""Hola mundo"""
	return HttpResponse('Hola Mundo')

def saludar(request, nombre, edad):
	if edad > 18:
		mensaje = 'Bienvenido {}, al sitio web'.format(nombre)
	else:
		mensaje = '{}, no estas autorizado'.format(nombre)
	return HttpResponse(mensaje)