

# from django.db import models

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     stock = models.PositiveIntegerField()


# # Create your models here.

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    stock_level = models.IntegerField(default=0)
    reorder_point = models.IntegerField(default=0)  # Minimum stock before reorder alert

    def __str__(self):
        return self.name


class StockTransaction(models.Model):
    STOCK_IN = 'in'
    STOCK_OUT = 'out'

    TRANSACTION_TYPE_CHOICES = [
        (STOCK_IN, 'Stock In'),
        (STOCK_OUT, 'Stock Out'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)
    quantity = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.product.name} - {self.quantity}"

