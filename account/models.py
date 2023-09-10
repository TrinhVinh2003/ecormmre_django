from django.db import models
from django.contrib.auth.models import User
from item.models import Item
# Create your models here.
CHOICE_STATE = (("My","VietNam"),("aaa","DDD"))
class InforAccount(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    locality =models.CharField(max_length=200)
    city = models.CharField(choices=CHOICE_STATE ,max_length=50)
    mobile  = models.IntegerField(default=0)
  
    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product  =models.ForeignKey(Item,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.price
    
    

