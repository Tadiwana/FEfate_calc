from django.conf.urls import url, include

urlpatterns = [
    url(r'^$','data.views.home', name='home'),
    url(r'^Adults/$','data.views.adults', name='adults'),
    url(r'^Adults/calc$','data.views.calc', name='calc'),
    url(r'^Adults/child$','data.views.child', name='child'),

]
