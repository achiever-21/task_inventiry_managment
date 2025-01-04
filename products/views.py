from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category, StockTransaction
from .serializers import ProductSerializer, CategorySerializer, StockTransactionSerializer
from users.models import User  # Ensure the User model is imported


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        # Admin can create/update/delete products, Manager can only view/edit products
        if self.action in ['create', 'update', 'destroy']:
            self.permission_classes = [IsAdmin]
        elif self.action in ['list', 'retrieve']:
            self.permission_classes = [IsManager]  # Manager and Admin can view products
        return super().get_permissions()


# Stock Transaction ViewSet: Staff can create transactions; Manager and Admin can manage
class StockTransactionViewSet(ModelViewSet):
    queryset = StockTransaction.objects.all()
    serializer_class = StockTransactionSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            self.permission_classes = [IsManager | IsStaff]  # Staff and Manager can perform stock transactions
        elif self.action in ['list', 'retrieve']:
            self.permission_classes = [IsStaff]  # Staff and Admin can view transactions
        return super().get_permissions()

