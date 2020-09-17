from django.forms import ModelForm
from django import forms
from .models import User_table,Transaction_table


class transactForm(ModelForm):
    class Meta:
        model = Transaction_table
        fields = ['Transfer_from','Transfer_to','credit']
        # widgets = {
        #     'trans_from': forms.TextInput(attrs={'class':'input'}),
        #     'trans_to': forms.TextInput(attrs={'class':'input'}),
        