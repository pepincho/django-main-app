from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^register/$', views.register, name="register"),
    url(r"^logout/$", views.user_logout, name="logout"),
    url(r"^login/$", views.log, name="log"),
]
