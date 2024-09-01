from django.db import models

# Create your models here.


from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_images')
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    discounts = models.CharField(max_length=50)  # Store discounts as a string to include the percentage sign
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    reviews = models.FloatField()  # Use FloatField to match the JSON data type
    processor = models.CharField(max_length=255)
    ram = models.CharField(max_length=50)
    os = models.CharField(max_length=50)
    ssd = models.CharField(max_length=50)
    display = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)

    def __str__(self):
        return self.product_name
