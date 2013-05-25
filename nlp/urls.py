from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nlp.views.home', name='home'),
    # url(r'^nlp/', include('nlp.foo.urls')),
    url(r'^', include('home.urls')),
    url(r'^gcd/', 'gcd.views.gcd', name='gcd'),
    url(r'^palindrome_product/', 'palindrome_product.views.palindrome', name='palindrome_product'),
    url(r'^static/', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
) 
