from django.db import models
from users.models import User

class Store(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stores')
    store_name = models.CharField(max_length=100)
    store_license = models.CharField(max_length=50)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.store_name

class Product(models.Model):
    PRESCRIPTION_TYPES = (
        ('otc', 'Over the Counter'),
        ('rx', 'Prescription Required'),
    )
    
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='products')
    product_name = models.CharField(max_length=100)
    product_details = models.TextField()
    product_expiration = models.DateField()
    prescription_type = models.CharField(max_length=3, choices=PRESCRIPTION_TYPES)
    time_frame = models.CharField(max_length=50)  # e.g., "Morning, Night"
    duration = models.CharField(max_length=50)   # e.g., "7 days"
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product_name

class Order(models.Model):
    PAYMENT_METHODS = (
        ('cash', 'Cash on Delivery'),
        ('card', 'Credit Card'),
        ('transfer', 'Bank Transfer'),
    )
    
    vendor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vendor_orders')
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_orders')
    assigned_rider = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='rider_orders')
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS)
    vat = models.DecimalField(max_digits=5, decimal_places=2)
    delivery_fee = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_delivered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Order {self.id} - {self.customer.username}"

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_details')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.product.product_name} in Order {self.order.id}"