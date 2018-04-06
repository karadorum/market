from django.db import models
from django.contrib.auth.models import User

# Создаем базовую модель нашего продукта

class Category(models.Model): 
      title = models.CharField(max_length=200)
      description = models.TextField(max_length=5000, blank=True)
      related_name = "products"

      def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000, blank=True)
    category = models.ForeignKey(Category, on_delete='CASCADE', null=True, related_name = "products")
    
    def get_absolute_url(self): 
        return reverse('product_detail', args=[str(self.id)])

    def __str__(self):
        return self.title

class User(models.Model):
    
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=5000, blank=True)

    
    
    
    
          

class Order(models.Model):
    user = models.ForeignKey(User, on_delete='CASCADE', null=True ) 
    product = models.ForeignKey(Product, on_delete = 'CASCADE')
    customer_name = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=200)
    

    

    





      

      


