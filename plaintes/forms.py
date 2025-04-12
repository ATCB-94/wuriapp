from django import forms
from .models import plainte

class plainteForm(forms.ModelForm):
    class Meta:
        model = plainte
        fields = ['nom', 'email', 'telephone', 'objet', 'message']
        