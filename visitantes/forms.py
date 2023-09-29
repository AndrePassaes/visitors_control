from django import forms
from visitantes.models import Visitor

class VisitorForm(forms.ModelForm):    
    class Meta:
        model = Visitor
        fields = {
            "full_name", "cpf", "birth_date",
            "house_number", "license_plate", 
        }
