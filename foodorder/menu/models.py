from django.db import models

# Create your models here.
class PickBurger(models.Model):
            CustomerPIN= models.CharField(max_length=10,blank=False)
        
        
            Quantity = models.IntegerField()
            class Meta:
                db_table = "burger_logs"
