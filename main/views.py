from django.shortcuts import render

from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response

from .models import Category, Recipe, Ingredient
from .serializers import RecipeSerializer, CategorySerializer, IngredientSerializer
# Create your views here.



class CategoryViewSet(ViewSet):
    def list(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response({"message": f"Category with {pk}-ID not found!"})
        
    def create(self, request, pk=None):
        if not pk:
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.errors)
        return Response({"message": "CREATE object does not require an ID!"})
    
    def update(self, request, pk=None):
        if pk:
            try:
                category = Category.objects.get(pk=pk)
                serializer = CategorySerializer(category, data=request.data)
                return Response(serializer.data)
            except Category.DoesNotExist:
                return Response({"message": f"Category with {pk}-ID not found!"})
        return Response({"message": "UPDATE method requires an ID!"})

    def destroy(self, request, pk=None):
        if pk:
            try:
                category = Category.objects.get(pk=pk)
                category.delete()
                return Response({"message": "Successfully deleted!"})
            except Category.DoesNotExist:
                return Response({"message": f"Category with {pk}-ID not found!"})
        return Response({"message": "DELETE method requires an ID"})
    

class IngredientsViewSet(ViewSet):
    def list(self, request):
        ingredients = Ingredient.objects.all()
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        if pk:
            try:
                ingredient = Ingredient.objects.get(pk=pk)
                serializer = IngredientSerializer(ingredient)
                return Response(serializer.data)
            except Ingredient.DoesNotExist:
                return Response({"message": f"Object with {pk}-ID not found!"})
        return Response({"message": "GET method requires an ID!"})
    
    def create(self, request, pk=None):
        if not pk:
            serializer = IngredientSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Successfully created!"}) 
        return Response({"message": "CREATE method does not require an ID!"})

    def update(self, request, pk=None):
        if pk:
            try:
                ingredient = Ingredient.objects.get(pk=pk)
                serializer = IngredientSerializer(ingredient, data=request.data)
                return Response(serializer.data)     
            except Ingredient.DoesNotExist:
                return Response({"message": f"Object with {pk}-ID not found!"})
        return Response({"message": "UPDATE method requires an ID!"})

    def destroy(self, request, pk=None):
        if pk:
            try:
                ingredient = Ingredient.objects.get(pk=pk)
                ingredient.delete()
                return Response({"message": "Successfully deleted!"})
            except Ingredient.DoesNotExist:
                return Response({"message": f"Object with {pk}-ID not found!"})
        return Response({"message": "DELETE method requires an ID"})
    

class RecipeModelViewSet(ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    

