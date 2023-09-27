from django import forms
from visitantes.models import Visitor

class VisitorForm(forms.ModelForm):    
    class Meta:
        model = Visitor
        fields = "__all__"
