from rest_framework.viewsets import ModelViewSet

from .models import Recipe
from serializer import RecipeSerializer


class RecipeViewSet(ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
