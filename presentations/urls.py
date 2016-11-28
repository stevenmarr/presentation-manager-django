from django.conf.urls import url

from . import views

app_name = 'presentations'
urlpatterns = [
	url(r'^list/$', views.PresentationListView.as_view(), name='list'),
	url(r'^(?P<pk>[0-9]+)/update', views.UpdateView.as_view(), name='update'),
	]
