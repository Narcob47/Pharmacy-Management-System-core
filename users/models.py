from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('customer', 'Customer'),
        ('rider', 'Rider'),
        ('vendor', 'Vendor'),
    )
    
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    
    # Fields specific to riders
    plate_number = models.CharField(max_length=20, blank=True, null=True)
    car_or_motor_photos = models.ImageField(upload_to='rider_vehicles/', blank=True, null=True)
    license_and_registration = models.FileField(upload_to='rider_documents/', blank=True, null=True)

    def __str__(self):
        return self.username