from django.conf.urls import include, url

from people import views as pv
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'ly.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^normalmap/', pv.do_normalmap),
    url(r'^withparam/(?P<year>[0-9]{4})/(?P<month>[0,1][0-9])',pv.withparam),
    url(r'^oy/',views.do_app),
]
