from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, RecipeModelViewSet, IngredientsViewSet

router = DefaultRouter()
router.register('books', CategoryViewSet, basename='book')
router.register('recipes', RecipeModelViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('ingredient/', IngredientsViewSet.as_view({"get": "list", "post": "create"})),
    path('ingredient/<int:pk>', IngredientsViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}))
]