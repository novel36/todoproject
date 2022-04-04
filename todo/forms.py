from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    
    class Meta:
        model=Todo
        fields=['is_completed']
        # widgets = {
        #     'is_completed': forms.BooleanField(attrs={'cols': 80, 'rows': 20,'class':'novel' }),
        # }
