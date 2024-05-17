from django.urls import path
from products import urls
from .views import ProductsAPI, CategoryAPI



urlpatterns = [
    path('',ProductsAPI.as_view()),
    path('<int:pk>/',ProductsAPI.as_view()),
    path('category/', CategoryAPI.as_view()),
    path('category/<int:pk>/', CategoryAPI.as_view()),
]
