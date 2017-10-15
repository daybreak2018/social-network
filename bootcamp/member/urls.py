from django.conf.urls import include, url
from bootcamp.member import views
urlpatterns = [
    url(r'^$', views.member, name='member'),
    url(r'^feeds/', include('bootcamp.feeds.urls')),
]