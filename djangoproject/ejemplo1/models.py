from django.db import models

#ESTO ES EL MODELO DE LA TABLA EN SQLITE
# Create your models here.
#importar modulos

from django.contrib.auth import get_user_model #funcion de utilidad para traer el modelo de usuario
from django.core.validators import MaxValueValidator #validador de django para que el valor de cierto campo de modelo no se exceda en el que delimitamos en el validador

User = get_user_model()

class MovieList (models.Model):

	name = models.CharField('Nombre de la Lista', max_length=50, unique=True) #tamaño de la cadena, unique es que sea unico
	owner = models.ForeignKey(User) # es como una llave foranea en sql
	movies = models.ManyToManyField('movies.Movie') #modelo aplicacion

	def __str__(self):
		return "'{list}' de {owner}".format(
			list=self.name,
			owner=self.owner.get_full_name()
			)

	class Movie(models.Model): #Modelo de la pelicula

		name = models.CharField('Nombre de la pelicula', max_length=100)
		release_date = models.DateField('Fecha de estreno')
		rate_count = models.PositiveIntegerField('veces que se ha calificado la pelicula', blank=True, null='True')
		rate = models.PositiveIntegerField('Total de calificacion', blank=True,)
		tags = models.ManyToManyField('movies.Tag')
		studio = models.ForeignKey('movies.Studio')
		director = models.ForeignKey('movies.Director')


		
