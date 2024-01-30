from django.urls import path

from .views import (
    ShowRecipesWithoutProductView,
)

app_name = 'cookbookapp'

urlpatterns = [
    path('recipes/', ShowRecipesWithoutProductView.as_view(), name='recipes-table'),
]
