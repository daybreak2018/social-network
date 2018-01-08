x='mo_the_HS'
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from bootcamp.activities import views as activities_views
from bootcamp.authentication import views as bootcamp_auth_views
from bootcamp.core import views as core_views
from bootcamp.search import views as search_views
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.views.generic import TemplateView
admin.autodiscover()

favicon_view = RedirectView.as_view(url='/static/img/favicon.png')
#TemplateView.as_view(template_name='about.html') , name='about'
urlpatterns = [
    url(r'^about$', core_views.about, name='about' ),
    url(r'^about2$', TemplateView.as_view(template_name='about.html'), name='about2' ),
    url(r'^config_settings/', include('bootcamp.config_settings.urls')),
    url(r'^ticklist/', include('bootcamp.ticklist.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', core_views.home, name='home'),
    url(r'^favicon\.png$', favicon_view),
    url(r'^login', auth_views.login, {'template_name': 'core/cover.html'},
        name='login'),
    url(r'^logout', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^'+x+'/$', bootcamp_auth_views.signup, name='signup'),
    url(r'^settings/$', core_views.settings, name='settings'),
    url(r'^settings/picture/$', core_views.picture, name='picture'),
    url(r'^settings/upload_picture/$', core_views.upload_picture,
        name='upload_picture'),
    url(r'^settings/save_uploaded_picture/$', core_views.save_uploaded_picture,
        name='save_uploaded_picture'),
    url(r'^settings/password/$', core_views.password, name='password'),
    url(r'^network/$', core_views.network, name='network'),
    url(r'^feeds/', include('bootcamp.feeds.urls')),
    url(r'^questions/', include('bootcamp.questions.urls')),
    url(r'^articles/', include('bootcamp.articles.urls')),
    url(r'^messages/', include('bootcamp.messenger.urls')),
    url(r'^notifications/$', activities_views.notifications,
        name='notifications'),
    url(r'^notifications/last/$', activities_views.last_notifications,
        name='last_notifications'),
    url(r'^notifications/check/$', activities_views.check_notifications,
        name='check_notifications'),
    # For autocomplete suggestions
    url(r'^autocomplete/$', search_views.get_autocomplete_suggestions, name='autocomplete'),
    url(r'^search/$', search_views.search, name='search'),
    url(r'^(?P<username>[^/]+)/$', core_views.profile, name='profile'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
