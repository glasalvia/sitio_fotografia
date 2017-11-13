from django.conf.urls import url, include
from apps.api.views import api_leo


urlpatterns = [
	url(r'^leo/$', api_leo),
]

