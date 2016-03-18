from django.conf.urls import url, include

urlpatterns = [

    url(r'^$', 'data.views.homepage', name='homepage'),
    url(r'^practice/', 'data.views.practice', name='practice')
]
