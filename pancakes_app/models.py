from django.db import models
from datetime import datetime

# Create your models here.

#Category model
class Category(models.Model):
    name = models.CharField(max_length=200)                                 # Name Required. 200 characters or fewer

    def __str__(self):
        return self.name


#Product model
class Product(models.Model):
    name = models.CharField(max_length=200)                                  # Name Required. 200 characters or fewer
    category = models.ForeignKey(Category, on_delete=models.CASCADE)         # Category Required.To define a many-to-one relationship, use ForeignKey:
    price = models.FloatField(default=0.0)                                   # Price
    description = models.TextField(null=True, blank=True)                    # Description
    image = models.ImageField(null=True, blank=True, upload_to='images/')    # ImageField is a FileField with uploads restricted to image formats only
    is_enable = models.BooleanField(default=True)                            # For deletion logically
    created_at = models.DateTimeField(default=datetime.now, blank=True)      # Product created date
    updated_at = models.DateTimeField(default=datetime.now, blank=True)      # Product updated date

    def __str__(self):
        return self.name
