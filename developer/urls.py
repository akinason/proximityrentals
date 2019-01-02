from django.contrib.auth import views as auth_views
from django.conf.urls import url


from developer import views

app_name = 'developer'
urlpatterns = [
    url(r'^apps/$', views.AppList.as_view(), name='apps'),
    url(r'^app/$', views.AppDetail.as_view(), name='app'),
]