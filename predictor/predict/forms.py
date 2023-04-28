from django import forms

class user_forms(forms.Form):
    Time_hour = forms.IntegerField(max_value=24)
    block_ = forms.CharField(max_length=64)

