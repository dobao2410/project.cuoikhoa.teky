from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from. import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.all, name = 'Index'),
    path('<int:id>/', views.Detail, name='Detail'),
    path('category/<int:category_id>/', views.GetAllProductByCategory, name='GetAllProductByCategory'),
    path('register/', views.Register, name='Register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name = 'registration/login.html'), name='Login'),
    path('logout/', views.Logout, name='Logout'),
]