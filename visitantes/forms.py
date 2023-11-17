from django import forms
from visitantes.models import Visitor

class VisitorForm(forms.ModelForm):    
    class Meta:
        model = Visitor
        fields = [
            "full_name", "cpf", "birth_date",
            "house_number", "license_plate" 
        ]
        error_messages = {
            "full_name": {
                "required": "Nome completo é obrigatório para o registro."
            },
            "cpf": {
                "required": "CPF é obrigatório para o registro."
            },
            "birth_date": {
                "required": "Data de nascimento é obrigatória para o registro.",
                "invalid": "Por favor, informe um formato válido para data de nascimento (DD/MM/YYYY)."
            },
            "house_number": {
                "required": "Por favor, informe o número da casa a ser visitada."
            }
        }

class VisitorAuthorizationForm(forms.ModelForm):    
    resposible_resident = forms.CharField(required=True)
    
    class Meta:
        model = Visitor
        fields = [
           "responsible_resident"
        ]
        error_messages = {
            "responsible_resident": {
                "required": "Por favor, informe o responsável por autorizar a entrada do visitante."
                }
        }