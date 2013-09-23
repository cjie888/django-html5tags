from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'html5tags.views.home', name='home'),
    # url(r'^html5tags/', include('html5tags.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'example_app.views.home'),
    url(r'^form/tag/$', 'example_app.views.form_tag'),
    url(r'^rewrite/form/$', 'example_app.views.rewrite_form'),
)
