from rest_framework import serializers
from Recipenext.models import User, Recipe


class UserSerializer(serializers, ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "img_url", "created_at", "updated_at")


class RecipeSerializer(serializers, ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            "id",
            "title",
            "instructions",
            "image",
            "ingredients",
            "user_id",
            "created_at",
            "updated_at",
        )
