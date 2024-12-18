from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('post/<str:pk>/', views.post, name='post'),
    path('post_form/', views.formulario, name='post_form'),
    path('eliminar_post/<str:pk>/', views.eliminar_post, name='eliminar_post'),
    path('editar_post/<str:pk>/', views.editar_post, name='editar_post'),
]