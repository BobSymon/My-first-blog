from django.conf.urls import url
from ejemplo1.views import hello_world


urlpatterns = [

	url (
		#expresion regular
		regex=r'^hello-world/$',
		view = hello_world,
		name = 'hello_world'

		)


]