from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from .models import Recipe, RecipeIngredient


class RecipeInrgedientSerializer(ModelSerializer):
    # id = PrimaryKeyRelatedField(queryset=Ingredient.objects.all())
    class Meta:
        model = RecipeIngredient
        fields = ['id', 'amount']

class RecipeSerializer(ModelSerializer):
    # ingredients = RecipeInrgedientSerializer(source='recipe_ingredient', many=True)

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'ingredients']

    def create(self, validated_data):
        if 'tags' in self.validated_data:
            tags = self.validated_data.pop('tags')
        if 'ingredients' in self.validated_data:
            ingredients = self.validated_data.pop('ingredients')

        recipe = Recipe.objects.create(**validated_data)
        return recipe

    def update(self, instance, validated_data):
        pass



