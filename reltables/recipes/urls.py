from django.urls import include, path
from rest_framework import routers

from .views import RecipeViewSet

router = routers.DefaultRouter()

router.register(r'recipes', RecipeViewSet, basename='recipes')


urlpatterns = [
    path('', include(router.urls)),
]
