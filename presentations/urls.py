from django.conf.urls import url

from . import views

app_name = 'presentations'
urlpatterns = [
	url(r'^(?P<conference_id>[0-9]+)/$', views.index, name='index'),
	]