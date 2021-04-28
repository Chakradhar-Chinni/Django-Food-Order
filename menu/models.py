from django.db import models

# Create your models here.
class PickBurger(models.Model):
            Name = models.CharField(max_length=100,blank=False)
            CustomerPIN= models.CharField(max_length=10,blank=False)
            Quantity = models.IntegerField()
            Message = models.CharField(max_length=1000,blank=True)  #True -> Optional Field'
            class Meta:
                db_table = "burger_logs" #currently all orders are stored in this table only

class Meta:
