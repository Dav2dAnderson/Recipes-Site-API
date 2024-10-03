from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title


class Ingredient(models.Model):
    title = models.CharField(max_length=250)
    quantity = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.title


class Recipe(models.Model):
    title = models.CharField(max_length=250)
    cooking_time = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self) -> str:
        return self.title

