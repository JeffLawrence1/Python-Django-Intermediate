from django.conf.urls import url
from django.contrib import admin
from . import views

# def test(request):
#     print " apps urls"

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^$', test),
    url(r'^$', views.index),
]