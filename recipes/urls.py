from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='recipes-home'),
    path('recipes/<int:jorge>/', views.recipes, name='recipes-recipe')
]