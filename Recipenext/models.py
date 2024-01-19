from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.TextField()
    img_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    instructions = models.TextField()
    image = models.BinaryField(null=True, blank=True)
    ingredients = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
