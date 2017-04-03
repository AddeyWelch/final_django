from django import forms


class BounceIntoFun(forms.Form):
    quantity = forms.IntegerField(label='Quantity:', required=True, initial=1)
