from django.conf.urls import url, include

urlpatterns = [
    url(r'^$','data.views.home', name='home'),
    url(r'^FEfates$', 'data.views.homepageFE', name='homepageFE'),
    url(r'^practice/', 'data.views.practice', name='practice'),

]
