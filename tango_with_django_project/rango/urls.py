#this urls.py should live in the twd/tango_with_django_project/rango directory

from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
						url(r'^$', views.home_page, name='home'),
						url(r'^about/$', views.about, name='about'),
						url(r'^contact_us/$', views.contact_us, name='contact'),
						url(r'^gallery/$', views.gallery, name='gallery'),
						)
						