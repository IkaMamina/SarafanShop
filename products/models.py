from django.conf import settings
from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    """Модель категории"""

    name = models.CharField(max_length=225)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='categories/')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    """Модель подкатегории"""

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Подкатегория')
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='sub_categories/')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.category.name}: {self.name}"


class Product(models.Model):
    """Модель продукта"""

    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='Продукты')
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    small_image = models.ImageField(upload_to='small_images/')
    medium_image = models.ImageField(upload_to='medium_images/')
    large_image = models.ImageField(upload_to='large_images/')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.sub_category.name}: {self.name}"


class CartItem(models.Model):
    """Модель корзины"""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f'{self.user.username}: {self.product.name} ({self.quantity})'




