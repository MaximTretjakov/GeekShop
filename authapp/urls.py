from django.urls import path, re_path
from authapp.views import LogoutPageView, LoginPageView, RegisterPageView, EditPageView, VerifyPageView

app_name = 'authapp'

urlpatterns = [
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', LogoutPageView.as_view(), name='logout'),
    path('register/', RegisterPageView.as_view(), name='register'),
    path('edit/', EditPageView.as_view(), name='edit'),
    re_path(r'^verify/(?P<email>.+)/(?P<activation_key>\w+)/$', VerifyPageView.as_view(), name='verify'),
]
