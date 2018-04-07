from . import views
from django.conf.urls import url
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^remove/(?P<course_id>\d+)$', views.remove),
    url(r'^delete/(?P<course_id>\d+)$', views.delete),
]