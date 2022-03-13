from django.urls import path
from .views import *

urlpatterns = [
    path('category/',ListCategory.as_view(),name='category'),
    path('category/<int:pk>/',DetailCategory.as_view(),name='detail-category'),
    path('book/',ListBook.as_view(),name='book'),
    path('book/<int:pk>/',DetailBook.as_view(),name='detail-book'),
    path('category/',ListProduct.as_view(),name='category'),
    path('category/<int:pk>/',DetailProduct.as_view(),name='detail-product'),
]