from django.contrib import admin
from django.urls import path

from .views import home
from .views.product_views import category

app_name = "core"

urlpatterns = [
    path('', home.HomeView.as_view(), name="home" ),
    path('category/', category.CategoryListView.as_view(), name="category_list" ),
    path('category/create/', category.CategoryCreateView.as_view(), name="category_create" ),
    path('category/update/<int:category_id>', category.CategoryUpdateView.as_view(), name="category_update" ),
    path('category/delete/<int:category_id>', category.CategoryDeleteView.as_view(), name="category_delete" ),
]
