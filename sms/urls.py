from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from sms import views

app_name = 'sms'
urlpatterns = [
    url(r'^$', views.SmsList.as_view()),
    url(r'^(?P<pk>[0-9]+)/', views.SmsDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
