from django.conf.urls import include, url
from django.contrib import admin
from people import views as pv
from people import people_urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'ly.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^normalmap/', pv.do_normalmap),
    url(r'^withparam/(?P<year>[0-9]{4})/(?P<month>[0,1][0-9])',pv.withparam),
    url(r'^people/',include(people_urls)),
    url(r'^book/(?:page-(?P<pn>\d+)/)$',pv.pg),
    url(r'^myn/$',pv.myname,{'name':"hacker"}),
    url(r'^yourname/$',pv.revparse,name="askname"),
    url(r'^v10_1/',pv.v10_1),
    url(r'^v10_2/',pv.v10_2),
    url(r'^v11/',pv.v11,name="v11"),
    url(r'^exception/',pv.v2_exception),
    url(r'^v8_get/',pv.v8_get),
    url(r'^v9_get/',pv.v9_get),
    url(r'^v9_post/',pv.v9_post),
    url(r'^render1/',pv.render_test),
    url(r'^render2/',pv.render_test2),
    url(r'^render3',pv.render_test3),
    url(r'^render4',pv.render_test4),
    url(r'^two/',pv.two),
    url(r'^three/',pv.three),
    url(r'^four/',pv.four),
    url(r'^five_post/',pv.five_post),
    url(r"^mysess/",pv.mysess),
    url(r'^page/',pv.student),
]
