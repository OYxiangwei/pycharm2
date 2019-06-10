from django.conf.urls import include, url
from django.contrib import admin
from xw import views
from xw import xw_urls



urlpatterns = [
    # Examples:
    # url(r'^$', 'oy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^normalmap/',views.do_normalmap),
    url(r'^withparam/(?P<year>[0,9]{4})/(?P<month>[0,1][0,9])',views.withparam),
    url(r'^xw/',include(xw_urls)),
    url(r'^book/(?:page-(?P<pn>\d+)/)$',views.showpg),
    url(r'^youname/',views.extremparam,{"name":"欧阳祥伟"}),
    url(r'^your/',views.revparse,name="askname"),
    url(r'^exception/',views.exception),
    url(r'v8/',views.v8),
    url(r'v9/',views.v9_get),
    url(r'v9_post/',views.v9_post),
    url(r'render1/',views.render1),
    url(r'render2/',views.render2),
    url(r'render3/',views.render3),
    url(r'404/',views.get404)
]
