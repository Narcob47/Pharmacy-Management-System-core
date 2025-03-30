from rest_framework import viewsets, permissions
from .models import Store, Product, Order, OrderDetail
from .serializers import StoreSerializer, ProductSerializer, OrderSerializer, OrderDetailSerializer

class StoreViewSet(viewsets.ModelViewSet):
    serializer_class = StoreSerializer
    
    def get_queryset(self):
        if self.request.user.user_type == 'vendor':
            return Store.objects.filter(user=self.request.user)
        return Store.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        store_id = self.request.query_params.get('store_id')
        if store_id:
            return Product.objects.filter(store_id=store_id)
        return Product.objects.all()
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'customer':
            return Order.objects.filter(customer=user)
        elif user.user_type == 'vendor':
            return Order.objects.filter(vendor=user)
        elif user.user_type == 'rider':
            return Order.objects.filter(assigned_rider=user)
        return Order.objects.all()
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

class OrderDetailViewSet(viewsets.ModelViewSet):
    serializer_class = OrderDetailSerializer
    queryset = OrderDetail.objects.all()
    permission_classes = [permissions.IsAuthenticated]