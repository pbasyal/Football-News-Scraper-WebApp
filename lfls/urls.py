from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.main_view),
    url(r'^register/$', views.register),
    url(r'^news/([0-9]+)/', views.news_id, name="news_detail"),
    url(r'^about/$', views.about)
]
