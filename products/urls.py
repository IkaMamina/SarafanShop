from rest_framework.routers import DefaultRouter

from products.views import CategoryViewSet, SubCategoryViewSet, ProductViewSet, CartItemViewSet, CartInfoViewSet, \
    ClearCartViewSet

from products.apps import ProductsConfig

app_name = ProductsConfig.name
router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'sub_categories', SubCategoryViewSet, basename='sub_category')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'cart_items', CartItemViewSet, basename='cart_item')
router.register(r'cart_info', CartInfoViewSet, basename='cart_info')
router.register(r'clear_cart', ClearCartViewSet, basename='clear_cart')

urlpatterns = router.urls
