from django.urls import path
from products.views import (
    product_list_view, product_detail_view,
    product_create_view, product_update_view,
    product_delete_view,
    ProductListView, ProductDetailView,
    ProductCreateView, ProductUdateView,
    ProductDeleteView,
)


app_name = 'products'

urlpatterns = [
    path('<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', ProductUdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='delete'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('', ProductListView.as_view(), name='list'),
]