from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Recipenext.models import User, Recipe
from Recipenext.serializers import UserSerializer, RecipeSerializer


# Create your views here.


@csrf_exempt
def userApi(request, id=0):
    if request.method == "GET":
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
    elif request.method == "POST":
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("User Created Successfully", safe=False)
        return JsonResponse("Failed to create", safe=False)
    elif request.method == "PUT":
        user_data = JSONParser().parse(request)
        user = User.objects.get(id=user_data["id"])
        user_serializer = UserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed To update", safe=False)
    elif request.method == "DELETE":
        user = User.objects.get(id=id)
        user.delete()
        return JsonResponse("Deleted successfully", safe=False)
    return JsonResponse("Failed to delete", safe=False)


def recipeApi(request, id=0):
    if request.method == "GET":
        recipes = Recipe.objects.all()
        recipe_serializer = RecipeSerializer(recipes, many=True)
        return JsonResponse(recipe_serializer.data, safe=False)
    elif request.method == "POST":
        recipe_data = JSONParser().parse(request)
        recipe_serializer = RecipeSerializer(data=recipe_data)
        if recipe_serializer.is_valid():
            recipe_serializer.save()
            return JsonResponse("Recipe Successfully Created", safe=False)
        return JsonResponse("Failed to create", safe=False)
    elif request.method == "PUT":
        recipe_data = JSONParser().parse(request)
        recipe = Recipe.objects.get(id=recipe_data["id"])
        recipe_serializer = RecipeSerializer(recipe, data=recipe_data)
        if recipe_serializer.is_valid():
            recipe_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed To update", safe=False)
    elif request.method == "DELETE":
        recipe = Recipe.objects.get(id=id)
        recipe.delete()
        return JsonResponse("Deleted successfully", safe=False)
    return JsonResponse("Failed to delete", safe=False)
