from django.conf.urls import include, url
from django.contrib import admin
from . import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'oy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^normalmap/',views.do_normalmap),
    url(r'^withparam/(?P<year>[0,9]{4})/(?P<month>[0,1][0,9])',views.withparam),
    url(r'lily/',views.do_app)
]
