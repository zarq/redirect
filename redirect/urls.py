from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'redirect.views.home', name='home'),
    # url(r'^redirect/', include('redirect.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'redirect.views.index'),
    url(r'^add$', 'redirect.views.add'),
    url(r'^detail/(?P<short_key>[a-z0-9]+)$', 'redirect.views.detail'),

    url(r'^(?P<short_key>[a-z0-9]+)$', 'redirect.views.redirect'),
)
