from django.urls import path
from users.views import UserViewSet, CustomTokenObtainPairView
from core.views import StoreViewSet, ProductViewSet, OrderViewSet, OrderDetailViewSet

urlpatterns = [
    # Auth
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # Users
    path('users/', UserViewSet.as_view({
        'post': 'create',
        'get': 'list'
    }), name='user-list'),
    path('users/<int:pk>/', UserViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='user-detail'),
    
    # Stores
    path('stores/', StoreViewSet.as_view({
        'post': 'create',
        'get': 'list'
    }), name='store-list'),
    path('stores/<int:pk>/', StoreViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='store-detail'),
    
    # Products
    path('products/', ProductViewSet.as_view({
        'post': 'create',
        'get': 'list'
    }), name='product-list'),
    path('products/<int:pk>/', ProductViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='product-detail'),
    
    # Orders
    path('orders/', OrderViewSet.as_view({
        'post': 'create',
        'get': 'list'
    }), name='order-list'),
    path('orders/<int:pk>/', OrderViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='order-detail'),
    
    # Order Details
    path('order-details/', OrderDetailViewSet.as_view({
        'post': 'create',
        'get': 'list'
    }), name='orderdetail-list'),
    path('order-details/<int:pk>/', OrderDetailViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='orderdetail-detail'),
]