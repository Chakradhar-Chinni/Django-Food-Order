from django import forms

class BurgerSelection:
    class Meta:
        model = PickBurger
        fields = "__all__"


#by default blank field will be true
#true -> Not Mandatory
#false -> Mandatory