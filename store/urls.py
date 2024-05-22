from django.urls import path
from .import views

urlpatterns = [
    path('' , views.store, name = "store"),
    path('<category_slug>/', views.store, name="products_by_category"),
    path('<category_slug>/<product_slug>/', views.product_detail, name="product_detail"),
    
       
]
