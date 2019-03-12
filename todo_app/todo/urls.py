from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

urlpatterns += [
    url(r'^admin$', include(admin.site.urls)),
    url(r'^task$', views.task, name='task'),
]
