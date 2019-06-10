from django.conf.urls import include, url
from django.contrib import admin
from case01 import views
from rest_framework import routers

router = routers.SimpleRouter()
router.rigister(r'student',views.studentvs,base_name = 'stu')
urlpatterns = [
    # Examples:
    # url(r'^$', 'tlxydrf.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/',include(router.urls)),
]
