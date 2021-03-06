from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'social_login.views.home', name='home'),
    # url(r'^social_login/', include('social_login.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'home.views.home', name='home'),
    url(r'^login/$', 'home.views.enter', name='enter'),
    url(r'^log-out/$', 'home.views.log_out', name='log-out'),
    url('', include('social.apps.django_app.urls', namespace='social'))
)
