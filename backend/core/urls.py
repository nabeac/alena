from django.contrib import admin
from django.urls import path

from .views import home
from .views.product_views import category, unit, product

app_name = "core"

urlpatterns = [
    path('', home.HomeView.as_view(), name="home" ),
    path('category/', category.CategoryListView.as_view(), name="category_list" ),
    path('category/create/', category.CategoryCreateView.as_view(), name="category_create" ),
    path('category/update/<int:category_id>', category.CategoryUpdateView.as_view(), name="category_update" ),
    path('category/delete/<int:category_id>', category.CategoryDeleteView.as_view(), name="category_delete" ),
    
    path('unit/', unit.UnitListView.as_view(), name="unit_list" ),
    path('unit/create/', unit.UnitCreateView.as_view(), name="unit_create" ),
    path('unit/update/<int:unit_id>', unit.UnitUpdateView.as_view(), name="unit_update" ),
    path('unit/delete/<int:unit_id>', unit.UnitDeleteView.as_view(), name="unit_delete" ),

    path('product/', product.ProductListView.as_view(), name="product_list" ),
    path('product/create/', product.ProductCreateView.as_view(), name="product_create" ),
    path('product/update/<int:product_id>', product.ProductUpdateView.as_view(), name="product_update" ),
    path('product/delete/<int:product_id>', product.ProductDeleteView.as_view(), name="product_delete" ),
]
