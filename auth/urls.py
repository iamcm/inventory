from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login$', 'auth.views.login', name='login'),
    url(r'^logout$', 'auth.views.logout', name='logout'),
)
