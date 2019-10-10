
from django.contrib import admin
from django.urls import path
from cronJob import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="homepage"),
    path('login/', views.userLogin, name='login'),
    path('authentification/', views.userAuthentification, name='authentification'),
]
