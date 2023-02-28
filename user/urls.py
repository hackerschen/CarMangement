from django.template.defaulttags import url
from django.urls import re_path

from user import views

urlpatterns = [
    re_path(r'ulogin/', views.ulogin),
    re_path(r'uregist/', views.uregist),
    re_path(r'ulogout/', views.ulogout)
]