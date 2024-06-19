from django.urls import path
from .import views

urlpatterns = [
    path('' , views.store, name = "store"),
    path('category/<category_slug>/', views.store, name="products_by_category"),
    path('category/<category_slug>/<product_slug>/', views.product_detail, name="product_detail"),
    path('search', views.search, name='search'),
    
       
]
