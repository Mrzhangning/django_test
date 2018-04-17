

from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django_web.views import index
from django_web import views

app_name = 'admin'

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    #url(r'^index/$', views.index),
    #url('^usr/',include('django_web.urls')),
    url(r'^index/$', views.index),
    url(r'^index/chart/$',views.chart),

]

