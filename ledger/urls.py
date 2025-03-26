from django.urls import path
from .views import RecipesList, RecipesDetail, RecipesAdd, RecipesUpload

urlpatterns = [
    path('recipe/add', RecipesAdd.as_view(), name='recipe-add'),
    path('recipes/list', RecipesList.as_view(), name='recipes-list'),
    path('recipe/<int:pk>', RecipesDetail.as_view(), name='recipe'),
    path('recipe/<int:pk>/add_image', RecipesUpload.as_view(), name='recipe-upload')
]

app_name = 'ledger'
