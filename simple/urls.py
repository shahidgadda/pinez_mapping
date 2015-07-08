from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^upload/$', views.UploadView.as_view(),name='upload'),
    url(r'^done/$', views.DoneView.as_view()),  
]
