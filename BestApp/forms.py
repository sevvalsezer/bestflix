from django import forms
from BestApp.models import User

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

