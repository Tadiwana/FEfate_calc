from django.conf.urls import url, include

urlpatterns = [

    url(r'^$', 'totalWar.views.homepageTW', name='homepageTW'),
    url(r'^GreatBritian/', 'totalWar.views.GreatBritian', name='GreatBritian')

]
