from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    #create the feilds
    name=models.CharField(max_length=250, unique=True)
    #url path of the requested
    slug = models.SlugField(max_length=250, unique=True)
    description= models.TextField(blank=True)
    image=models.ImageField(upload_to='category', blank=True)

#meta class to pass the option to the model
    class Meta:
        ordering = ('name',)
        verbose_name='category'
        verbose_name_plural = 'categories'


  #to return a representation of the model
        def __str__(self):
            return '{}'.format(self.name)
        #   get url function for categories

    def get_url(self):
        return reverse('shop:products_by_category', args=[self.slug])


class Product(models.Model):
    #create the feilds
    name=models.CharField(max_length=250, unique=True)
    #url path of the requested
    slug = models.SlugField(max_length=250, unique=True)
    description= models.TextField(blank=True)
    category= models.ForeignKey(Category, on_delete=models.CASCADE)#if the produt is deleted, any reference of product will be deleted in category
    price=models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='product', blank=True)
    stock = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)#add time stamp
    updated = models.DateTimeField(auto_now=True)#update time stamp

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

        # to return a representation of the model
        def __str__(self):
            return '{}'.format(self.name)

    def get_url(self):
        return reverse('shop:ProdCatDetail', args=[self.category.slug, self.slug])
