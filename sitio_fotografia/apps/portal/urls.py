from django.conf.urls import url, include
from apps.portal.views import index_portal, index_contacto, index_sobre_mi, success


urlpatterns = [
	url(r'^$', index_portal, name='index'),
	url(r'^contacto/$', index_contacto, name='contacto'),
	url(r'^sobre_mi/$', index_sobre_mi, name='sobre_mi'),
	url(r'^success/$', success, name='success'),
]

