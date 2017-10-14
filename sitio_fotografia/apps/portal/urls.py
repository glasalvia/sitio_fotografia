from django.conf.urls import url
from apps.portal.views import index_portal


urlpatterns = [
	url(r'^$', index_portal),
]
