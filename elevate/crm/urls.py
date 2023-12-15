from django.urls import path, include
from crm import views

app_name = 'crm'

urlpatterns = [
    path('', views.homepage,name=""),
    path('register/', views.register,name='register'),
    path('my-login/', views.my_login,name='my-login'),
    path('dashboard/', views.dashboard,name='dashboard'),
    path('user-logout/', views.logout_view,name='user-logout')
]