from django import forms
from .models import Set


class AddSetForm:
    setNumber = forms.DecimalField()

    class Meta:
        model = Set
        fields = ["set_number"]
