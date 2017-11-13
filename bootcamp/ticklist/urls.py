from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ticklist, name='ticklist'),
    #url(r'^edit/(?P<pk>\d+)/$',views.EditTickList.as_view(), name='edit_ticklist'),
]
