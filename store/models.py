from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


User = get_user_model()

class Category(models.Model):
    title = models.CharField(max_length=128, unique=True)

    def __str__(self) -> str:
        return f"{self.title}"



class Promotion(models.Model):
    discount = models.DecimalField(max_digits=3, decimal_places=2)
    def __str__(self) -> str:
        return f"{self.discount:%}"



class Product(models.Model):
    title = models.CharField(max_length=128, unique=True)
    price = models.IntegerField()
    categories = models.ManyToManyField(Category, related_name="products")
    promotion = models.ForeignKey(Promotion, on_delete=models.PROTECT, related_name="products", null=True, blank=True)
    is_active = models.BooleanField()

    def __str__(self) -> str:
        return f"{self.title}"




class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    text = models.CharField(max_length=128)
    is_show = models.BooleanField(default=False)
    created = models.DateTimeField()



class Order(models.Model):

    class ShippingChoice(models.TextChoices):
        motor = "motor"
        car = "car"
        truck = "truck"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    shipping = models.CharField(choices=ShippingChoice.choices, max_length=6)
    created = models.DateTimeField()
    is_delivered = models.BooleanField(default=False)


    def __str__(self) -> str:
        return f"{self.id}"




class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="items", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()


    def __str__(self) -> str:
        return f"{self.id}"