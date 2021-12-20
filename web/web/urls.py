from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('accounts/login/', views.login_view),
    path('accounts/register/', views.register_view),
    path('accounts/logout/', views.logout_view),
]
