from django.db import models

# Create your models here.
class PickBurger(models.Model):
            CustomerPIN= models.CharField(max_length=10,blank=False)
            #Type = models.TextChoices('Cheese Burger', 'Veg Burger', 'Chilli Burger')
            Quantity = models.Text('1','2','3','4','5','6','7','8','9','10')
            Quantity = models.IntegerField()
            class Meta:
                db_table = "burger_logs"
