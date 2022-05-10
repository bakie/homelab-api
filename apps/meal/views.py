from rest_framework import generics
from apps.meal.models import Recipe
from apps.meal.serializers import RecipeSerializer


class RecipeList(generics.ListCreateAPIView):
    """
    API endpoint that allows recipes to be viewed.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
