from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import RecipeDetailView, RecipeCreateView
from . import views


urlpatterns = [
    path('cookbook-create/', views.create_cookbook, name='cookbook_create'),
    # path('recipe-create/', views.create_recipe, name='recipe_create'),
    path('recipe-create/', login_required(RecipeCreateView.as_view()), name='recipe_create'),
    path('recipe-create-ingredient/', login_required(RecipeCreateView.as_view()), name='recipe_create'),
    path('recipe-detail/<slug:pk>', login_required(RecipeDetailView.as_view()), name='recipe-detail'),
    # path('recipe-detail/<slug:pk>/edit', login_required(RecipeEditView.as_view()), name='recipe-edit'),
    path('recipe-detail/<slug:pk>/edit', views.update_recipe, name='recipe-edit'),
]
