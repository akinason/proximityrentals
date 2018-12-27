from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns
from main import views


app_name = 'main'
urlpatterns = [
    url(r'^users/$', views.UserList.as_view(), name='users'),
    url(r'^user/$', views.UserDetail.as_view(), name='user'),
    url(r'^photo/user/$', views.ProfilePictureDetail.as_view(), name='profile_picture'),
    url(r'^username/verify/$', views.VerifyUserName.as_view(), name='verify_username'),
    url(r'^phone/verify/$', views.VerifyPhone.as_view(), name='verify_phone'),
    url(r'^email/verify/$', views.VerifyEmail.as_view(), name='verify_email'),
    url(r'^password/reset/$', views.PasswordReset.as_view(), name='password_reset'),
    url(r'^password/reset/code/verify/$', views.PasswordResetVerifyCode.as_view(), name='verify_reset_code'),
    url(r'^password/reset/confirm/$', views.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    # Authentication URLs
    url(r'^login/$', views.ObtainAuthToken.as_view(), name='login'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
