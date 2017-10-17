from django.http import HttpResponse

#funcion de python con un parametro request
def hello_world (request): 
	#ejemplo de un VIEWS que solo muestra un hola mundo en el navegador
	return HttpResponse ("<h1>hola mundo! desde Django , esto es un view </h1> con una etiqueta h1")

