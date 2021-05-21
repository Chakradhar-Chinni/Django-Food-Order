from django import forms
from . models import PickBurger

class BurgerSelection(forms.ModelForm): 
    class Meta:
        model = PickBurger
        fields = "__all__"

 
#by default blank field will be true 
#true -> Not Mandatory 
#false -> Mandatory 
 
