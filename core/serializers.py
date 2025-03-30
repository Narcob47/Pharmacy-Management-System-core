from rest_framework import serializers
from .models import Store, Product, Order, OrderDetail
from users.models import User

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'
        read_only_fields = ['user', 'is_approved']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['store']

class OrderDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    
    class Meta:
        model = OrderDetail
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    order_details = OrderDetailSerializer(many=True, read_only=True)
    vendor = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(user_type='vendor'))
    customer = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(user_type='customer'))
    assigned_rider = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(user_type='rider'), 
        required=False, 
        allow_null=True
    )
    
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['total_price', 'is_delivered']