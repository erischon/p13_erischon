from django.urls import path
from . import views

urlpatterns = [
    path('cookbook-create/', views.create_cookbook, name='cookbook_create'),
    path('recipe-create/', views.create_recipe, name='recipe_create'),
]
