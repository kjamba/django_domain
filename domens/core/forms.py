from django import forms
from .models import Domens

class DomensForm(forms.ModelForm):

    class Meta:
        model = Domens
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'