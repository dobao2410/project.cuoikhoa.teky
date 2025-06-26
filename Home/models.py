from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField()
    
    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=200, null=False ,blank=True)
    description = models.TextField()
    price = models.IntegerField()
    price_sale = models.IntegerField()
    img = models.FileField(upload_to='static/images/')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class CartOrder(models.Model):
    name = models.CharField(max_length=255, null=False, blank=True)
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=255)
    method_payment = models.IntegerField() 
    # 0: Thanh toán khi nhận hàng, 1: Thanh toán bằng CK, 2: Thanh toán bằng thẻ tí dụng
    method_shipping = models.IntegerField()
    # 0: Vận chuyển nhanh, 1: Vận chuyển tiết kiệm, 2: Vận chuyển hàng cồng kềnh, dễ vỡ
    shipping_price = models.IntegerField()
    total_money = models.IntegerField()
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    cart_order_id = models.ForeignKey(CartOrder,  on_delete=models.CASCADE)
    price = models.IntegerField()
    def __str__(self):
        return self.product_id, self.quantity
    

    