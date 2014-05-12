from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dbProject.views.home', name='home'),
    # url(r'^dbProject/', include('dbProject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}, name='static'),
)

urlpatterns += patterns('demo.views',
    url(r'^test/$', 'test'),
    url(r'^home/$', 'home'),
    url(r'^myAccount/$', 'myAccount'),
    url(r'^myRestaurant/$', 'myRestaurant'),
    url(r'^listDisplay/$', 'listDisplay'),
    url(r'^register/$', 'register'),
    url(r'^restaurantDetail/$', 'restaurantDetail'),
    url(r'^login/$', 'login'),
    url(r'^logout/$', 'logout'),
)
