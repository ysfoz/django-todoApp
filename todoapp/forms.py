from django import forms
from django.db.models import fields
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title',)
        
class UpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields =('completed',)