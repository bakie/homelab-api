from django.urls import path
from . import views

urlpatterns = [
    path('recipe/', views.RecipeList.as_view(), name='recipe_list'),
    path('recipe/<int:pk>', views.RecipeDetail.as_view(), name='recipe_detail'),
]
