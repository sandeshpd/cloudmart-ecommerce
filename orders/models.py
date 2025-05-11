from django.db import models
from users.models import User
from inventory.models import Product

# Create your models here.
class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmend',' Confirmed'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    total_amount = models.DecimalField(max_digits = 10, decimal_places = 2)
    status = models.CharField(max_length = 10, choices = STATUS_CHOICES, default = 'pending')
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Order #{self.id}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete = models.CASCADE, related_name = 'items')
    product =  models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits = 10, decimal_places = 2)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"