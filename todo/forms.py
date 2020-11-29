from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add tasks', 'aria-label': 'Add tasks', 'aria-describedby': 'button-addon2'}),
            'complete': forms.CheckboxInput(attrs={'class': 'form-control'})
        }