from django.urls import path
from .views import getRoutes, getProducts, getProduct, getUserProfile
from .views import MyTokenObtainPairView


urlpatterns = [
    path('users/login/', MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('users/profile/', getUserProfile, name='users-profile'),
    path('', getRoutes, name='routes'),
    path('products/', getProducts, name='products'),
    path('products/<str:pk>/', getProduct, name='product'),
]
