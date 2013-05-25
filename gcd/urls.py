from django.conf.urls import patterns, url
from gcd import views

urlpatterns = patterns('',
    url(r'^$', views.gcd)
)
