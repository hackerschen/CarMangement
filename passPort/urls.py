from django.urls import path, re_path, include

from passPort import views

urlpatterns = [
    re_path(r'get/', views.hello),
    re_path(r'getAll/', views.GetAllPassPort),
    re_path(r'add/', views.AddPassPort),
    re_path(r'update/', views.UpdatePassPort),
    re_path(r'delete/', views.DeletePassPort),
    re_path(r'search/', views.Search),
    re_path(r'geta/', views.GetAPassPort),
]
