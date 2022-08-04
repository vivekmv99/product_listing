from django.db import models

# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey(Category, related_name="category_field", on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100,null=True)
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='media/products', null=True)


