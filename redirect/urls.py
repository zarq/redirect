from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^_admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^_admin/', include(admin.site.urls)),

    url(r'^$', 'redirect.views.index'),
    url(r'^_a$', 'redirect.views.add'),
    url(r'^_d/(?P<short_key>[a-z0-9]+)$', 'redirect.views.detail'),

    url(r'^(?P<short_key>[a-z0-9]+)$', 'redirect.views.redirect_short'),
    url(r'^l/(?P<long_key>[a-z]+)$', 'redirect.views.redirect_long'),
)
