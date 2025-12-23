from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=16, verbose_name='название категории')
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=128, verbose_name='название товара')
    product_description = models.TextField(verbose_name='описание товара')
    product_count = models.IntegerField(verbose_name='кол-во товара')
    product_price = models.IntegerField(verbose_name='цена товара')
    product_photo = models.ImageField(upload_to='media', verbose_name='фото товара')
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return self.product_name

class Cart(models.Model):
    user_id = models.IntegerField()
    user_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_pr_amount = models.IntegerField()

    class Meta:
        verbose_name = 'корзину'
        verbose_name_plural = 'корзины'

    def __str__(self):
        return f'Корзина пользователя с ID {self.user_id}'
