from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from products.models import Category, SubCategory, Product, CartItem
from products.serializers import CategorySerializer, SubCategorySerializer, ProductSerializer, CartItemSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """Представление для категории"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


class SubCategoryViewSet(viewsets.ModelViewSet):
    """Представление для подкатегории"""

    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [permissions.AllowAny]


class ProductViewSet(viewsets.ModelViewSet):
    """Представление для продукта"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]


class CartItemViewSet(viewsets.ModelViewSet):
    """Представление для корзины"""

    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CartInfoViewSet(viewsets.ViewSet):
    """Получаем общую информацию о корзины"""

    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def info(self, request):
        cart_items = CartItem.objects.filter(user=request.user)
        total_quantity = sum(item.quantity for item in cart_items)
        total_cost = sum(item.total_price() for item in cart_items)
        return Response({
            'total_quantity': total_quantity,
            'total_cost': total_cost
        })


class ClearCartViewSet(viewsets.ViewSet):
    """Удаляем корзину"""

    @action(detail=False, methods=['post'])
    def clear_cart(self, request):
        CartItem.objects.filter(user=request.user).delete()
        return Response({'message': 'Корзина успешно очищена'})

