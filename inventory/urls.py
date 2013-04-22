from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from core.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'inventory.views.home', name='home'),
    # url(r'^inventory/', include('inventory.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', login_required(IndexView.as_view())),
    url(r'^collection$', login_required(CollectionCreateView.as_view())),
    url(r'^collection/edit/(?P<pk>\d)$', login_required(CollectionUpdateView.as_view())),
    url(r'^item$', login_required(ItemCreateView.as_view())),
    url(r'^item/edit/(?P<pk>\d)$', login_required(ItemUpdateView.as_view())),
    url(r'^auth/', include('auth.urls')),


)
