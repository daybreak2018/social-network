from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.config_settings, name='config_settings'),
    url(r'^change_signup/$',views.change_signup, name='change_signup'),
    url(r'^reset_list/$',views.reset_list, name='reset_list'),
    url(r'^change_menu/$',views.change_menu, name='change_menu'),
    url(r'^edit_bill/$',views.edit_bill, name='edit_bill'),
    url(r'^show_bill/$',views.show_bill, name='show_bill')
]
