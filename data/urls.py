from django.conf.urls import url, include

urlpatterns = [
    url(r'^$','data.views.home', name='home'),
    url(r'^Adults/$','data.views.adults', name='adults'),

]
