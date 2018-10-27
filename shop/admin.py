from django.contrib import admin
from .models import Category,Product
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    List_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    List_display = ['name','price', 'stock', 'available','created','updated']
    List_editable = ['price','stock','available']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
admin.site.register(Product,ProductAdmin)
