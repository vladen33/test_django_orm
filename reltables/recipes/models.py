from django.db import models


class Recipe(models.Model):
    name = models.CharField(
        verbose_name='Название рецепта',
        max_length=100
    )
    ingredients = models.ManyToManyField('Ingredient', through='RecipeIngredient')


class Ingredient(models.Model):
    name = models.CharField(
        verbose_name='Ингредиент',
        max_length=100
    )
    unit = models.CharField(
        verbose_name='Единица измерения',
        max_length=10
    )


class RecipeIngredient(models.Model):
    recipe = models.ManyToManyField()
