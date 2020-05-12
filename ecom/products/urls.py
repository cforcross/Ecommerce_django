from django.urls import path
from .views import (ProductListView, product_list_view, ProductDetailView,
                    product_detail_view, ProductFeatureDetailView,
                    ProductFeaturedListView, ProductDetailSlugView)
app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    # path('products-fbv', product_list_view, name='list'),
    # path('<int:pk>/', ProductDetailView.as_view()),
    path('feature/', ProductFeaturedListView.as_view()),
    path('<int:pk>/', ProductFeatureDetailView.as_view()),
    path('<slug:slug>/', ProductDetailSlugView.as_view(), name='detail'),
    path('products-detail-fbv', product_detail_view, ),
]
