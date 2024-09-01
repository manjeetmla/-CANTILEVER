from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product
from import_export.admin import ImportExportModelAdmin
class RecordAdmin(ImportExportModelAdmin):
    list_display = ['product_name', 'image', 'original_price', 'discounts',
                    'discounted_price', 'reviews', 'processor', 'ram', 'os', 'ssd',
                    'display', 'brand']

admin.site.register(Product,RecordAdmin)