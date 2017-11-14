from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ticklist, name='ticklist'),
    url(r'^edit/$',views.edit, name='edit'),
    url(r'^editSelective/$',views.editSelective, name='editSelective'),
    url(r'^viewAll/$',views.viewAll, name='viewAll')
]
